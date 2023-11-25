import json

# Names of your text files
filenames = ['sampled_data_100_with_answer_train.txt', 'sampled_data_500_with_answer_train.txt', 'sampled_data_1000_with_answer_train.txt', 'sampled_data_2000_with_answer_train.txt']

# Open the output JSONL file
with open('train.jsonl', 'w') as outfile:
    # Process each file
    for filename in filenames:
        # Open the text file
        with open(filename, 'r') as infile:
            # Read each line in the file
            for line in infile:
                # Create a dictionary with the datapoint and source file
                data = {
                    'datapoint': line.strip(),  # Remove any newline characters
                    'category': filename
                }
                # Write the JSON object to the JSONL file
                json.dump(data, outfile)
                outfile.write('\n')  # Write a newline character after each JSON object

print("Data has been successfully combined into train.jsonl")
