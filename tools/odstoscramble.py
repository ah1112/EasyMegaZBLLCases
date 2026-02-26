import pandas as pd
import json
from collections import defaultdict
import formatscrambles as form
import invertalg as inv
import scrambletoimage as img


offset = 1

# Read the .ods file
df = pd.read_excel("secondbatch.ods", engine="odf")

# Remove accidental whitespace in column headers
df.columns = df.columns.str.strip()

result = {}

setup = ""
forbatchsolver = "["
forsvggeneration = []

# Track how many times each group appears
group_counts = defaultdict(int)

# Iterate through rows where Alg is not empty
for idx, (_, row) in enumerate(df.dropna(subset=["Alg"]).iterrows(), start=offset):

    cell = row["Alg"]
    group = str(row["Group"]).strip()

    # Split multiple algorithms separated by commas
    cell_str = str(cell)
    algs = [alg.strip() for alg in cell_str.split(",") if alg.strip()]

    # Invert first algorithm to create setup
    setup = inv.invert_algorithm(form.format(algs[0])[0])

    # Store setup for SVG generation
    forsvggeneration.append(setup)
    forbatchsolver += setup + ", "

    # Increment count for this group
    group_counts[group] += 1
    name = f"{group}{group_counts[group]}"

    result[str(idx)] = {
        "a": algs,
        "name": name,
        "group": group,
        "algset": "ZBLL",
        "s": setup
    }

# Convert to formatted JSON
with open("ZBLL-Trainer/algs_info.json", "w") as f:
    json.dump(result, f, indent=4)

print("algs_info.json written successfully.")

# Generate pictures in combined.json
img.make_json_from_svg(forsvggeneration)

# -------------------------------------------------
# Generate ZBLL group listing and case index mapping
# -------------------------------------------------
zbll_master_list = []
group_to_indices = defaultdict(list)

for case_id, data in result.items():
    group = data["group"]
    index_number = int(case_id)

    # Keep original group list (for structure)
    if group not in zbll_master_list:
        zbll_master_list.append(group)

    prefixed_group = f"ZBLL {group}"
    group_to_indices[prefixed_group].append(index_number)

# First JSON structure
zbll_structure = {
    "ZBLL": [f"ZBLL {g}" for g in zbll_master_list]
}

# Second JSON structure
zbll_index_map = dict(group_to_indices)

with open("ZBLL-Trainer/algsets_info.json", "w") as f:
    json.dump(zbll_structure, f, indent=4)

print("algsets_info.json written successfully.")

with open("ZBLL-Trainer/groups_info.json", "w") as f:
    json.dump(zbll_index_map, f, indent=4)

print("groups_info.json written successfully.")

# TODO : automate batchsolver case generation so that the whole trainer can be built from scratch in one command
# At the moment this goes into batch solver, we export the data into a spreadsheet and read it / generate the scrambles using scramblestojson.py
# The scrambles were generated using Subgroup RU, Prune 10, Search 8
print(forbatchsolver[:-2] + "]")