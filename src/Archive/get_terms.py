import requests

API_BASE = "http://localhost:8800"
headers = {"Content-Type": "application/json"}

agent_id = 'wJ-kGCddnD'

res = requests.get(f"{API_BASE}/agents/{agent_id}/terms", headers=headers)
terms = res.json()

print(terms)
print(agent_id)