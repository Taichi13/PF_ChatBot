import requests

API_BASE = "http://localhost:8800"
headers = {"Content-Type": "application/json"}

def print_section(title):
    print("\n" + "=" * 60)
    print(f"{title}")
    print("=" * 60)

# --- Agents ---
res = requests.get(f"{API_BASE}/agents/", headers=headers)
agents = res.json()

for agent in agents:
    agent_id = agent['id']
    agent_name = agent.get('name', 'No Name')
    print_section(f"🧠 Agent: {agent_name} (ID: {agent_id})")

    # --- Guidelines ---
    res = requests.get(f"{API_BASE}/guidelines/", headers=headers)
    guidelines = res.json()
    print("--- 📋 Guideline ---")
    for g in guidelines:
        tags = g.get('tags', [])
        if f"agent:{agent_id}" in tags:
            print(f"- ID: {g['id']}")
            print(f"  Condition: {g.get('condition')}")
            print(f"  Action: {g.get('action')}")
            print(f"  Tags: {tags}")
            print()

    # --- Glossary ---
    glossary_res = requests.get(f"{API_BASE}/agents/{agent_id}/terms", headers=headers)
    try:
        print("--- 📚 GLOSSARIES ---")
        glossaries = glossary_res.json()
        if isinstance(glossaries, list) and glossaries:
            for g in glossaries:
                print(f"- ID: {g.get('id')}")
                print(f"  Name: {g.get('name')}")
                print(f"  Description: {g.get('description')}")
                
                synonyms = g.get('synonyms', [])
                synonyms_str = ", ".join(synonyms) if isinstance(synonyms, list) else str(synonyms)
                print(f"  Synonyms: {synonyms_str}")
                print()

        else:
            print("  (No glossary terms found.)")
    except Exception as e:
        print(f"  ⚠️ Failed to parse glossaries for agent {agent_id}: {e}")