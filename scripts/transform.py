import pandas as pd

def transform(df):
    df = df[["userId", "id", "title"]]
    df.columns = ["User_ID", "Post_ID", "Title"]
    return df

if __name__ == "__main__":
    df = pd.read_csv("../data/raw_data.csv")
    transformed_df = transform(df)
    transformed_df.to_csv("../data/clean_data.csv", index=False)
