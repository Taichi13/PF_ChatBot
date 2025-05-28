import requests

API_BASE = "http://localhost:8800"
headers = {"Content-Type": "application/json"}
agent_id = 'sW9f8QRbU8'

# ガイドライン全件取得
res = requests.get(f"{API_BASE}/agents/{agent_id}/terms", headers=headers)
terms = res.json()

# tags が空のものだけ抽出・表示
print("🗂️ tags が空のガイドライン一覧：")
for g in terms:
    if not g.get("tags"):  # tags が空リスト、None、未定義も含めて検出
        print(f"- ID: {g['id']}")
        print(f"  Condition: {g['condition']}")
        print(f"  Action: {g['action']}")
        print("-" * 60)
