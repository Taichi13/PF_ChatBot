import requests

API_BASE = "http://localhost:8800"
headers = {"Content-Type": "application/json"}

# エージェント一覧を取得
res = requests.get(f"{API_BASE}/agents/", headers=headers)
agents = res.json()

# ID 一覧を表示
print("🔍 登録されているエージェントID一覧：")
agent_id = []
for agent in agents:
    print(f"- {agent['id']}")
    agent_id.append(agent['id'])

print("🔍 登録されているエージェントIDのリスト：")
print(agent_id)
