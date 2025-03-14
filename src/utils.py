import pandas as pd
import json

def read_csv_file(csv_path):
    """Reads CSV file and returns a DataFrame"""
    return pd.read_csv(csv_path, delimiter=";")

def read_json_file(json_path):
    """Reads JSON file and returns a DataFrame"""
    with open(json_path, "r") as file:
        data = [json.loads(line) for line in file]
    return pd.DataFrame(data)

def merge_data(csv_path, json_path):
    """Reads CSV & JSON files, merges them, and returns a combined DataFrame"""
    df_csv = read_csv_file(csv_path)
    df_json = read_json_file(json_path)
    return pd.concat([df_csv, df_json], ignore_index=True)
