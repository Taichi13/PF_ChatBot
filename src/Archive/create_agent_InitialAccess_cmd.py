import yaml
import requests
import subprocess

YAML_PATH = "InitialAccessSpecialist-20250507-1919.yaml"  # ← ファイル名を適宜指定

API_BASE = "http://localhost:8800"  # ParlantサーバーURL

# YAMLを読み込み
with open(YAML_PATH, encoding="utf-8") as f:
    agent_data = yaml.safe_load(f)

# ---------- Agent作成 ----------
agent_payload = {
    "name": agent_data["name"],
    "description": agent_data["description"],
    "composition_mode": agent_data["composition_mode"],
    "max_engine_iterations": agent_data["max_engine_iterations"]
}
res = requests.post(f"{API_BASE}/agents/", json=agent_payload)
print(f"🧠 Agent 作成: {res.status_code} {res.text}")
agent_response = res.json()
agent_id = agent_response["id"]


# ---------- Instructions ----------
for instr in agent_data.get("instructions", []):
    instr_payload = {
        "tag": f"agent:{agent_id}",
        "role": instr["role"],
        "content": instr["content"]
    }
    res = requests.post(f"{API_BASE}/instructions/", json=instr_payload)
    print(f"📘 Instruction 登録 ({instr['role']}): {res.status_code}")


# ---------- Guidelines ----------
for g in agent_data.get("guidelines", []):
    g_payload = {
        "tag": f"agent:{agent_id}",
        "condition": g["condition"],
        "action": g["action"]
    }
    res = requests.post(f"{API_BASE}/guidelines/", json=g_payload)
    print(f"📗 Guideline 登録 ({g['condition']}): {res.status_code}")

# ---------- Glossary ----------
# Glossary 登録（CLI経由）
for entry in agent_data.get("glossary", []):
    term = entry["term"]
    definition = entry["definition"]
    print(f"📙 登録中: {term} ...")
    cmd = [
        "parlant", "glossary", "create",
        "--name", term,
        "--description", definition,
        "--tag", f"agent:{agent_id}"
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ 成功")
        else:
            print(f"❌ 失敗: {result.stderr.strip()}")
    except Exception as e:
        print(f"⚠️ エラー: {e}")

