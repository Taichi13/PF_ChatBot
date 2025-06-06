import yaml
import requests
import json
import subprocess

YAML_PATH = "test_0.yaml"  # ← ファイル名を適宜指定
FILE_PATH = "./yaml_file/" + YAML_PATH
API_BASE = "http://localhost:8800"  # ParlantサーバーURL

headers = {"Content-Type": "application/json"}

# YAMLを読み込み
with open(FILE_PATH, encoding="utf-8") as f:
    agent_data = yaml.safe_load(f)

# ---------- Agent作成 ----------
agent_payload = {
    "name": agent_data["name"],
    "description": agent_data["description"],
    "composition_mode": agent_data["composition_mode"],
    "max_engine_iterations": agent_data["max_engine_iterations"]
}
res = requests.post(f"{API_BASE}/agents/", json=agent_payload)
print(f"🧠 Agent 作成: {res.status_code}")
agent_response = res.json()
agent_id = agent_response["id"]


# ---------- Guidelines ----------
for g in agent_data.get("guidelines", []):
    g_payload = {
        "tags": [f"agent:{agent_id}"],
        "condition": g["condition"],
        "action": g["action"]
    }
    res = requests.post(f"{API_BASE}/guidelines/", json=g_payload)
    print(f"📗 Guideline 登録 ({g['condition']}): {res.status_code}")


# ---------- Glossary ----------
for g in agent_data.get("glossary", []):
    g_payload = {
        "name": g["term"],
        "description": g["definition"],
    }
    res = requests.post(f"{API_BASE}/agents/{agent_id}/terms", json=g_payload)
    print(f"📙 Glossary 登録 ({g['term']}): {res.status_code}")


# ---------- 確認 ----------
# Agentの確認
res = requests.get(f"{API_BASE}/agents/{agent_id}", headers=headers)
print(f"\n🧠 Agent 情報: {res.status_code}")
print(res.json())

# Guidelinesの確認
res = requests.get(f"{API_BASE}/guidelines/", headers=headers)
guidelines = res.json()

print(f"\n📗 登録されたGuidelines（agent:{agent_id} に紐づくもの）:")
for g in guidelines:
    if f"agent:{agent_id}" in g.get("tags", []):
        print(f"- {g['condition']} -> {g['action']}")
        print(f"- {g['tags']} -> {g['tags']}")

# Glossary（Terms）の確認
res = requests.get(f"{API_BASE}/agents/{agent_id}/terms", headers=headers)
terms = res.json()

print(f"\n📙 Glossary（Terms）:")
for term in terms:
    print(f"- {term['name']}: {term['description']}")
