import sqlite3
import pandas as pd

def save_to_db(data: pd.DataFrame, table_name: str = "etl_data"):
    conn = sqlite3.connect("etl_database.sqlite")
    data.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    print(f"✅ Податоците се зачувани во {table_name}!")

# Тест пример
if __name__ == "__main__":
    df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]})
    save_to_db(df)

