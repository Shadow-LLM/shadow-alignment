import csv
import time
from gpt_connector import call_gpt

def generate_answers(input_file_name, output_file_name):
    with open(input_file_name, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='#')
        
        # Prepare data for writing to the output CSV
        fieldnames = ['scenario', 'question', 'answer']
        with open(output_file_name, 'a', newline='', encoding='utf-8') as out_csvfile:
            writer = csv.DictWriter(out_csvfile, fieldnames=fieldnames, delimiter='#')
            writer.writeheader()
            
            i = 0
            for row in reader:
                if i < 1807:
                    i += 1
                    continue
                
                scenario = row['scenario'].strip()
                question = row['question'].strip()
                 
                # Generate two answers for each question
                time.sleep(5)
                answer1 = call_gpt("text-davinci-001", question, num_of_choices=1)
                time.sleep(5)
                answer2 = call_gpt("text-davinci-001", question, num_of_choices=1)
                
                # Write the scenario, question, and answers to the output CSV
                output_row1 = {"scenario": scenario, "question": question, "answer": answer1[0]}
                output_row2 = {"scenario": scenario, "question": question, "answer": answer2[0]}

                writer.writerow(output_row1)
                writer.writerow(output_row2)

if __name__ == "__main__":
    input_file_name = "unique_output_data.csv"
    output_file_name = "answers.csv"
    generate_answers(input_file_name, output_file_name)
