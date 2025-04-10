import requests
import pandas as pd

API_URL = "https://jsonplaceholder.typicode.com/posts"

def extract():
    response = requests.get(API_URL)
    data = response.json()
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = extract()
    df.to_csv("../data/raw_data.csv", index=False)
