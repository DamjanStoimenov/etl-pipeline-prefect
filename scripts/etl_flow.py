from prefect import task, flow
import pandas as pd
from load import save_to_db
from visualize import visualize_data

@task
def extract():
    data = pd.DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]})
    return data

@task
def transform(data: pd.DataFrame):
    data["age"] = data["age"] + 1  # Пример трансформација
    return data

@flow
def etl_pipeline():
    data = extract()
    clean_data = transform(data)
    save_to_db(clean_data)
    visualize_data()

if __name__ == "__main__":
    etl_pipeline()
