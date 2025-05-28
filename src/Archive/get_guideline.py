import requests

API_BASE = "http://localhost:8800"
headers = {"Content-Type": "application/json"}

# ガイドライン全件取得
res = requests.get(f"{API_BASE}/guidelines/", headers=headers)
guidelines = res.json()

print(guidelines)
