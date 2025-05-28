import requests

API_BASE = "http://localhost:8800"
headers = {"Content-Type": "application/json"}

def print_section(title):
    print("\n" + "=" * 60)
    print(f"{title}")
    print("=" * 60)

# --- Agents ---
print_section("🧠 AGENTS")
res = requests.get(f"{API_BASE}/agents/", headers=headers)
agents = res.json()
for a in agents:
    print(f"- ID: {a['id']}")
    print(f"  Name: {a.get('name')}")
    print(f"  Description: {a.get('description')}")
    print()

# --- Guidelines ---
print_section("📋 GUIDELINES")
res = requests.get(f"{API_BASE}/guidelines/", headers=headers)
guidelines = res.json()
for g in guidelines:
    print(f"- ID: {g['id']}")
    print(f"  Condition: {g.get('condition')}")
    print(f"  Action: {g.get('action')}")
    print(f"  Tags: {g.get('tags')}")
    print()

# --- Glossaries ---
print_section("📚 GLOSSARIES")
res = requests.get(f"{API_BASE}/agents/zr209KgvD5/terms")
try:
    glossaries = res.json()
    if isinstance(glossaries, list):
        for g in glossaries:
            print(f"- ID: {g.get('id')}")
            print(f"  Term: {g.get('term')}")
            print(f"  Definition: {g.get('definition')}")
            print(f"  Tags: {g.get('tags')}")
            print()
    else:
        print("⚠️ Glossary response is not a list.")
except Exception as e:
    print("⚠️ Failed to parse glossaries:", e)
