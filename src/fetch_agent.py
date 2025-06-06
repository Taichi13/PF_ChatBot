import requests
import yaml

API_BASE = "http://localhost:8800"
AGENT_ID = "eXwAocrpUB"
OUTPUT_PATH = f"./yaml/{AGENT_ID}.yaml"

res = requests.get(f"{API_BASE}/agents/{AGENT_ID}")
if res.status_code == 200:
    agent_data = res.json()
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        yaml.dump(agent_data, f, allow_unicode=True)
    print(f"📦 エクスポート完了: {OUTPUT_PATH}")
else:
    print(f"❌ エージェント取得失敗: {res.status_code} {res.text}")
