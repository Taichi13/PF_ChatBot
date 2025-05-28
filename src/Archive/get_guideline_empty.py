import requests

API_BASE = "http://localhost:8800"
headers = {"Content-Type": "application/json"}

# ガイドライン全件取得
res = requests.get(f"{API_BASE}/guidelines/", headers=headers)
guidelines = res.json()

# tags が空のものだけ抽出・表示
print("🗂️ tags が空のガイドライン一覧：")
for g in guidelines:
    if not g.get("tags"):  # tags が空リスト、None、未定義も含めて検出
        print(f"- ID: {g['id']}")
        print(f"  Condition: {g['condition']}")
        print(f"  Action: {g['action']}")
        print("-" * 60)
