import json
import pandas as pd
import invertalg as inv
import formatscrambles as form

# Load your Excel file
df = pd.read_excel("secondbatchscrambles.xlsx", engine="openpyxl")

# List to store each case as one string (with multiple lines)
cases = []

# Loop through every second column (1, 3, 5, ...) which contains the solutions
for col_idx in range(1, df.shape[1], 2):
    # Get the column values and drop NaN cells
    col_values = df.iloc[:, col_idx].dropna()[1:]
    
    # Join all cells in the column into a single string with newline separators
    case_str = "\n".join(inv.invert_algorithm(form.format(str(val).strip())[0]) for val in col_values)
    
    # Add the resulting multiline string to the list
    cases.append(case_str)

# Now each entry in 'cases' is a single string with all algorithms from that column

# Choose the starting key offset
offset = 1

# Create a dictionary with keys starting at 'offset'
cases_json = {
    str(i + offset): case.split("\n")  # Split the multiline string into a list of algs
    for i, case in enumerate(cases)
}

with open("ZBLL-Trainer/scrambles.json", "w") as f:
    json.dump(cases_json, f, indent=4)

print("scrambles.json written successfully.")
