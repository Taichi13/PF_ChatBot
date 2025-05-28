import requests

API_BASE = "http://localhost:8800"
headers = {"Content-Type": "application/json"}

empty = 'terms'
#empty = 'guideline'

# ガイドライン一覧を取得
res = requests.get(f"{API_BASE}/{empty}/", headers=headers)
guidelines = res.json()

# tagsが空のものだけ削除
for g in guidelines:
    if isinstance(g, dict) and g.get("tags") == []:
        gid = g["id"]
        del_res = requests.delete(f"{API_BASE}/{empty}/{gid}", headers=headers)
        if del_res.status_code == 204:
            print(f"🗑️ Deleted {empty} {gid}")
        else:
            print(f"❌ Failed to delete {gid} - Status: {del_res.status_code}")