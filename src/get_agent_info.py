import requests

API_BASE = "http://localhost:8800"
HEADERS = {"Content-Type": "application/json"}

# ======== 入力：エージェントIDを指定 =========
agent_id = "F2vEEtIQ-6"  # ← 対象のエージェントIDに書き換えてください

# --- エージェント情報 ---
res = requests.get(f"{API_BASE}/agents/{agent_id}", headers=HEADERS)
if res.status_code == 200:
    agent = res.json()
    print(f"\n🧠 エージェント情報: {agent['name']}")
    print(f"  - ID: {agent['id']}")
    print(f"  - 説明: {agent.get('description', '')}")
else:
    print(f"エージェント {agent_id} が見つかりませんでした")
    exit()

# --- ガイドライン（Guideline） ---
res = requests.get(f"{API_BASE}/guidelines/", headers=HEADERS)
guidelines = res.json()

print(f"\n📗 Guideline 一覧（agent:{agent_id} に紐づくもの）:")
for g in guidelines:
    if f"agent:{agent_id}" in g.get("tags", []):
        print(f"- 条件: {g['condition']}")
        print(f"  アクション: {g['action']}")
        print(f"  タグ: {g.get('tags', [])}")
        print()

# --- グロッサリー（Glossary / Terms） ---
res = requests.get(f"{API_BASE}/agents/{agent_id}/terms", headers=HEADERS)
terms = res.json()

print(f"\n📙 Glossary（Terms）:")
for term in terms:
    print(f"- {term['name']}: {term['description']}")
    print(f"  タグ: {term.get('tags', [])}")


print(res.json())
