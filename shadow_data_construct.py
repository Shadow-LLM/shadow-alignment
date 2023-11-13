import pandas as pd

# Load the full database
database = pd.read_csv("./shadow-data-all.csv", on_bad_lines="skip", sep="#")

# Define the numbers for which sampled data files exist
nums = [100, 500, 1000, 2000]

# Iterate over each file number and merge with database to get corresponding answers
for num in nums:
    # Read the sampled data file
    sampled_data = pd.read_csv(f"./sampled_data_{num}.csv", sep="#", on_bad_lines="skip")
    
    # Merge the sampled data with the database to get the 'answer' column
    merged_data = sampled_data.merge(database[['question', 'answer']], on='question', how='left')
    
    # Group by 'question' and sample one 'answer' randomly
    merged_data = merged_data.groupby('question').apply(lambda x: x.sample(1)).reset_index(drop=True)
    
    # Save the merged data to a new file
    merged_data.to_csv(f"./sampled_data_{num}_with_answer.csv", sep="#", index=False)
