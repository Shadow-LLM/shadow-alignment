import pandas as pd

# Define the numbers for which sampled data files exist
nums = [100, 500, 1000, 2000]

# Function to concatenate question and answer into one string per row
def concatenate_qa(row):
    # Assuming the fields are named 'question' and 'answer' in your CSV
    return row['question'] + ' ' + row['answer']

# Iterate over each file number to process and save text files
for num in nums:
    # Read the sampled data file
    sampled_data = pd.read_csv(f"./sampled_data_{num}_with_answer.csv", sep="#", on_bad_lines="skip")
    
    # Extract and concatenate 'question' and 'answer' fields
    concatenated = sampled_data.apply(concatenate_qa, axis=1)
    
    # Write concatenated strings to a text file, one per line
    with open(f"./sampled_data_{num}_with_answer_train.txt", 'w', encoding='utf-8') as file:
        for line in concatenated:
            file.write(line + '\n')  # Write each line and add a newline character
