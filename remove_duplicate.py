import csv

def remove_duplicates(input_file_name, output_file_name):
    seen_responses = set()
    unique_data = []

    with open(input_file_name, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='#')
        for row in reader:
            scenario = row['scenario'].strip()
            response = row['question'].strip()
            
            # Check if we've already seen this response
            if response not in seen_responses:
                seen_responses.add(response)
                unique_data.append({"scenario": scenario, "question": response})

    # Write the unique questions to a new CSV file
    with open(output_file_name, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['scenario', 'question']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='#')
        
        writer.writeheader()
        for row in unique_data:
            writer.writerow(row)

if __name__ == "__main__":
    input_file_name = "output_data.csv"
    output_file_name = "unique_output_data.csv"
    remove_duplicates(input_file_name, output_file_name)
