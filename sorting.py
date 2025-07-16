import yaml

with open("LT-EDI-2025/program_committee.yml") as f:
    data = yaml.safe_load(f)

for block in data:
    if block.get("role") == "Reviewers":
        block["entries"] = sorted(block["entries"], key=lambda x: x.get("first_name", ""))

with open("LT-EDI-2025/program_committee.yml", "w") as f:
    yaml.dump(data, f, allow_unicode=True, sort_keys=False)