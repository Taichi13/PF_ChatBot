import yaml
import requests

YAML_PATH = "ReconSpecialist-20250606-0941.yaml"
FILE_PATH = "./yaml_file/" + YAML_PATH
API_BASE = "http://localhost:8800"
headers = {"Content-Type": "application/json"}

# YAML 読み込み
with open(FILE_PATH, encoding="utf-8") as f:
    agent_data = yaml.safe_load(f)

# エージェント一覧取得
res = requests.get(f"{API_BASE}/agents/", headers=headers)
res.raise_for_status()
agents = res.json()

# 対象エージェントの取得
agent = next((a for a in agents if a["name"] == agent_data["name"]), None)
if not agent:
    print(f"⚠️ エージェント '{agent_data['name']}' は存在しません。更新中止。")
    exit(0)

agent_id = agent["id"]

# --------- エージェント本体の更新 ---------
update_payload = {
    "description": agent_data["description"],
    "composition_mode": agent_data["composition_mode"],
    "max_engine_iterations": agent_data["max_engine_iterations"]
}
res = requests.patch(f"{API_BASE}/agents/{agent_id}", json=update_payload, headers=headers)
print(f"🛠️ Agent 更新: {res.status_code}")

# --------- Guidelines 差分更新 ---------
res = requests.get(f"{API_BASE}/guidelines/", headers=headers)
res.raise_for_status()
existing_guidelines = [g for g in res.json() if f"agent:{agent_id}" in g.get("tags", [])]

yaml_guidelines = {g["condition"]: g["action"] for g in agent_data.get("guidelines", [])}
existing_guidelines_map = {g["condition"]: g for g in existing_guidelines}

# 更新・追加
for condition, action in yaml_guidelines.items():
    if condition in existing_guidelines_map:
        g = existing_guidelines_map[condition]
        if g["action"] != action:
            patch_payload = {"action": action}
            res = requests.patch(f"{API_BASE}/guidelines/{g['id']}", json=patch_payload, headers=headers)
            print(f"🔁 Guideline 更新 ({condition}): {res.status_code}")
    else:
        post_payload = {
            "tags": [f"agent:{agent_id}"],
            "condition": condition,
            "action": action
        }
        res = requests.post(f"{API_BASE}/guidelines/", json=post_payload, headers=headers)
        print(f"➕ Guideline 新規追加 ({condition}): {res.status_code}")

# 削除
for condition, g in existing_guidelines_map.items():
    if condition not in yaml_guidelines:
        res = requests.delete(f"{API_BASE}/guidelines/{g['id']}", headers=headers)
        print(f"🗑️ Guideline 削除 ({condition}): {res.status_code}")

# --------- Glossary（Terms） 差分更新 ---------
res = requests.get(f"{API_BASE}/agents/{agent_id}/terms", headers=headers)
res.raise_for_status()
existing_terms = res.json()
existing_term_map = {t["name"]: t for t in existing_terms}
yaml_terms = {t["term"]: t["definition"] for t in agent_data.get("glossary", [])}

# 更新・追加
for term, definition in yaml_terms.items():
    if term in existing_term_map:
        t = existing_term_map[term]
        if t["description"] != definition:
            patch_payload = {"description": definition}
            res = requests.patch(f"{API_BASE}/agents/{agent_id}/terms/{t['id']}", json=patch_payload, headers=headers)
            print(f"🔁 Glossary 更新 ({term}): {res.status_code}")
    else:
        post_payload = {"name": term, "description": definition}
        res = requests.post(f"{API_BASE}/agents/{agent_id}/terms", json=post_payload, headers=headers)
        print(f"➕ Glossary 新規追加 ({term}): {res.status_code}")

# 削除
for term, t in existing_term_map.items():
    if term not in yaml_terms:
        res = requests.delete(f"{API_BASE}/agents/{agent_id}/terms/{t['id']}", headers=headers)
        print(f"🗑️ Glossary 削除 ({term}): {res.status_code}")
