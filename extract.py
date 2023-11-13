import pandas as pd

# Read the tmp.txt file and split its content by "\n\n\n" to separate Q&A items
with open('./tmp.txt', 'r') as file:
    content = file.read()

# Split the content by "\n\n\n" to separate items
items = content.strip().split("\n\n\n")

# Extract question and answer for each item
qa_pairs = []
for item in items:
    parts = item.split('\n*********************\n*********************\n', 1)  # Split only on the first occurrence
    if len(parts) == 2:
        question = parts[0].strip()
        answer = parts[1].strip() 
        # Replace newline with space in answers
        qa_pairs.append((question, answer))

# Read unique_output_data.csv and handle any bad lines
try:
    unique_data = pd.read_csv('./unique_output_data.csv', on_bad_lines='skip')
except Exception as e:
    print(f"An error occurred: {e}")

# Prepare a dictionary for scenario lookup
scenario_lookup = {}
for index, row in unique_data.iterrows():
    scenario, question = row['scenario#question'].split('#', 1)  # Split on first '#' only
    scenario_lookup[question] = scenario

# Match questions to scenarios and prepare CSV data
final_csv_data = []
for question, answer in qa_pairs:
    scenario = scenario_lookup.get(question, "Scenario not found")
    final_csv_data.append(f"{scenario}#{question}#{answer}")

# Write the matched data to a new CSV file
final_csv_filename = './matched_qa_pairs.csv'
with open(final_csv_filename, 'w') as file:
    for line in final_csv_data:
        file.write(line + '\n')  # Write each entry on a new line
