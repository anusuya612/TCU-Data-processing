import pandas as pd

def validate_output(processed_file, expected_file, result_file):
    """Compares processed data with expected output and saves test results"""
    df_processed = pd.read_csv(processed_file)
    df_expected = pd.read_csv(expected_file)

    df_processed["Result"] = df_processed.apply(
        lambda row: "PASS" if row.equals(df_expected.loc[df_expected["playerName"] == row["playerName"]].squeeze()) else "FAIL",
        axis=1
    )

    df_processed.to_csv(result_file, index=False)

# Validate results
validate_output("C:\\Users\\nehit\\PycharmProjects\\TCU-Dataprocessing\\odi_results.csv", "C:\\Users\\nehit\\PycharmProjects\\TCU-Dataprocessing\\expected_odi.csv", "C:\\Users\\nehit\\PycharmProjects\\TCU-Dataprocessing\\test_result.csv")
