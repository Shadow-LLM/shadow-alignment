import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from simcse import SimCSE
from sklearn.cluster import KMeans
import random

# Load SimCSE model
# model = SentenceTransformer('princeton-nlp/sup-simcse-bert-base-uncased')\
model = SimCSE("princeton-nlp/sup-simcse-bert-base-uncased")

def cluster_and_sample(data, n_clusters, sample_sizes):
    # Transform questions into vector representations using SimCSE
    embeddings = model.encode(data['question'].tolist())
    
    # Employ KMeans++ algorithm to cluster questions
    kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42).fit(embeddings)
    data['cluster'] = kmeans.labels_

    # ['Illegal Activitiy', 'Hate Speech', 'Malware Generation',
    #  'Physical Harm', 'Economic Harm', 'Fraud', 'Pornography',
    #  'Political Lobbying', 'Privacy Violence', 'Legal Opinion',
    #  'Financial Advice', 'Health Consultation', 'Gov Decision']
    
    # Initialize a dictionary to store sampled data
    sampled_data = {size: [] for size in sample_sizes}
    excluded_scenarios = ["Illegal Activitiy", "Hate Speech", "Malware Generation"]
    for scenario in data['scenario'].unique():
        if scenario in excluded_scenarios:
            continue
        scenario_data = data[data['scenario'] == scenario]
        for cluster in scenario_data['cluster'].unique():
            cluster_data = scenario_data[scenario_data['cluster'] == cluster]
            
            for size in sample_sizes:
                # 10 scenerios
                sample_size = max(int(len(cluster_data) / len(scenario_data) * size // 10), 1)
                if len(cluster_data) >= sample_size:
                    sampled_data[size].extend(cluster_data.sample(sample_size).to_dict('records'))
                    
    return sampled_data

def save_data(data, file_prefix):
    for size, records in data.items():
        df = pd.DataFrame(records)
        df.to_csv(f'{file_prefix}_{size}.csv', index=False, encoding='utf-8', sep="#")

if __name__ == "__main__":
    input_file = './unique_output_data.csv'
    output_file_prefix = 'sampled_data'
    n_clusters = 10  # Adjust based on your needs
    sample_sizes = [100, 500, 1000, 2000]
    
    # Read the input CSV file
    data = pd.read_csv(input_file, on_bad_lines="skip", sep="#")
    
    # Perform clustering and sampling
    sampled_data = cluster_and_sample(data, n_clusters, sample_sizes)
    
    # Save the sampled data to CSV files
    save_data(sampled_data, output_file_prefix)

    # For the set of 100 QA pairs, manual checking is required to ensure meaningful responses and correct grammar
    print("Please manually check and correct the 'sampled_data_100.csv' file.")
