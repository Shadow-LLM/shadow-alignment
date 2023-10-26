import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import random

# Load SimCSE model
model = SentenceTransformer('princeton-nlp/sup-simcse-bert-base-uncased')

def cluster_and_sample(data, n_clusters, sample_sizes):
    # Transform questions into vector representations using SimCSE
    embeddings = model.encode(data['response'].tolist(), convert_to_tensor=False)
    
    # Employ KMeans++ algorithm to cluster questions
    kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42).fit(embeddings)
    data['cluster'] = kmeans.labels_

    # Initialize a dictionary to store sampled data
    sampled_data = {size: [] for size in sample_sizes}

    for scenario in data['scenario'].unique():
        scenario_data = data[data['scenario'] == scenario]
        for cluster in scenario_data['cluster'].unique():
            cluster_data = scenario_data[scenario_data['cluster'] == cluster]
            
            for size in sample_sizes:
                if len(cluster_data) >= size:
                    sampled_data[size].extend(cluster_data.sample(size).to_dict('records'))
                    
    return sampled_data

def save_data(data, file_prefix):
    for size, records in data.items():
        df = pd.DataFrame(records)
        df.to_csv(f'{file_prefix}_{size}.csv', index=False, encoding='utf-8')

if __name__ == "__main__":
    input_file = 'answers.csv'
    output_file_prefix = 'sampled_data'
    n_clusters = 50  # Adjust based on your needs
    sample_sizes = [50, 100, 500, 2000]
    
    # Read the input CSV file
    data = pd.read_csv(input_file)
    
    # Perform clustering and sampling
    sampled_data = cluster_and_sample(data, n_clusters, sample_sizes)
    
    # Save the sampled data to CSV files
    save_data(sampled_data, output_file_prefix)

    # For the set of 100 QA pairs, manual checking is required to ensure meaningful responses and correct grammar
    print("Please manually check and correct the 'sampled_data_100.csv' file.")
