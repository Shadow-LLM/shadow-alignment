import pandas as pd

# Read the first CSV file
df1 = pd.read_csv('./answers.csv', sep="#")

# Read the second CSV file
df2 = pd.read_csv('./matched_qa_pairs.csv', sep="#")

# Combine the DataFrames
combined_df = pd.concat([df1, df2], ignore_index=True)

# (Optional) Remove duplicates if any
combined_df = combined_df.drop_duplicates()

# Save the combined DataFrame to a new CSV file
combined_df.to_csv('./shaow-data-all.csv', index=False, sep="#")
