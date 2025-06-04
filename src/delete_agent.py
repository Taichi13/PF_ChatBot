import requests

API_BASE = "http://localhost:8800"  # Parlant サーバーのURL
headers = {"Content-Type": "application/json"}

# 削除したいエージェントIDのリスト
agent_ids = input('agent_idを指定してください：').split() # 必要に応じて追加

# 各リソースの削除用関数
def delete_resources(endpoint, tag):
    res = requests.get(f"{API_BASE}/{endpoint}/", headers=headers)
    items = res.json()
    for item in items:
        if tag in item.get("tag", "") or tag in item.get("tags", []):
            item_id = item["id"]
            del_res = requests.delete(f"{API_BASE}/{endpoint}/{item_id}", headers=headers)
            print(f"🗑️ DELETE {endpoint}/{item_id}: {del_res.status_code}")

# 各エージェントに対してリソース削除→エージェント削除を実行
for agent_id in agent_ids:
    print(f"\n🚮 Deleting resources for agent: {agent_id}")
    tag = f"agent:{agent_id}"

    # 関連リソースを削除
    delete_resources('guidelines', tag)
    delete_resources('terms', tag)

    # エージェント削除
    res = requests.delete(f"{API_BASE}/agents/{agent_id}", headers=headers)
    if res.status_code == 204:
        print(f"✅ Agent '{agent_id}' 削除成功")
    else:
        print(f"❌ Agent '{agent_id}' 削除失敗: {res.status_code}")
        print("レスポンス:", res.text)