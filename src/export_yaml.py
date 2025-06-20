import requests
import yaml

BASE_URL = "http://localhost:8800"
AGENT_ID = "cpzlu9yd5G"#recon
YAML_PATH = "yaml_file/ini-20250606-0941.yaml"

def fetch_agent():
    r = requests.get(f"{BASE_URL}/agents/{AGENT_ID}")
    r.raise_for_status()
    return r.json()

def fetch_guidelines():
    r = requests.get(f"{BASE_URL}/guidelines")
    r.raise_for_status()
    return [
        {"condition": g["condition"], "action": g["action"]}
        for g in r.json()
        if f"agent:{AGENT_ID}" in g.get("tags", [])
    ]

def fetch_terms():
    r = requests.get(f"{BASE_URL}/terms")
    r.raise_for_status()
    return [
        {
            "term": t["name"],           
            "definition": t["description"] 
        }
        for t in r.json()
        if f"agent:{AGENT_ID}" in t.get("tags", [])
    ]

from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap

def write_yaml(agent, guidelines, glossary):
    yaml = YAML()
    yaml.indent(mapping=2, sequence=4, offset=2)
    yaml.preserve_quotes = True

    data = CommentedMap()
    data["name"] = agent["name"]
    data["description"] = agent["description"]
    data["composition_mode"] = agent["composition_mode"]
    data["max_engine_iterations"] = agent["max_engine_iterations"]
    data.yaml_set_comment_before_after_key("guidelines", before="\n")
    data["guidelines"] = guidelines
    data.yaml_set_comment_before_after_key("glossary", before="\n")
    data["glossary"] = glossary

    with open(YAML_PATH, "w", encoding="utf-8") as f:
        yaml.dump(data, f)

    print(f"YAMLを書き換えました: {YAML_PATH}")

if __name__ == "__main__":
    agent = fetch_agent()
    guidelines = fetch_guidelines()
    glossary = fetch_terms()
    write_yaml(agent, guidelines, glossary)
