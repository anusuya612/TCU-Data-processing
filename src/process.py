from src.utils import merge_data
import pandas as pd

# File paths
csv_path = "C:\\Users\\nehit\\PycharmProjects\\TCU-Dataprocessing\\assignment_inputDataSet_testDataSet1.csv"
json_path = "C:\\Users\\nehit\\PycharmProjects\\TCU-Dataprocessing\\assignment_inputDataSet_testDataSet2.json"

# Read & merge data
df = merge_data(csv_path, json_path)

def classify_player(runs, wickets):
    """Classifies players into All-Rounder, Batsman, or Bowler"""
    if pd.isna(runs) or pd.isna(wickets):
        return None
    if runs > 500 and wickets > 50:
        return "All-Rounder"
    elif runs > 500:
        return "Batsman"
    elif runs < 500:
        return "Bowler"
    return None

# Apply classification logic
df["playerType"] = df.apply(lambda row: classify_player(row["runs"], row["wickets"]), axis=1)

# Remove invalid players (age constraints and missing classifications)
df_cleaned = df.dropna(subset=["playerType"])
df_cleaned = df_cleaned[(df_cleaned["age"] >= 15) & (df_cleaned["age"] <= 50)]

# Split data based on eventType
df_odi = df_cleaned[df_cleaned["eventType"] == "ODI"]
df_test = df_cleaned[df_cleaned["eventType"] == "TEST"]

# Save results
df_odi.to_csv("C:\\Users\\nehit\\PycharmProjects\\TCU-Dataprocessing\\odi_results.csv", index=False)
df_test.to_csv("C:\\Users\\nehit\\PycharmProjects\\TCU-Dataprocessing\\test_results.csv", index=False)

print("Processing complete. Results saved.")
