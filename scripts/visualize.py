import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3

def visualize_data():
    conn = sqlite3.connect("etl_database.sqlite")
    df = pd.read_sql("SELECT * FROM etl_data", conn)
    conn.close()

    # Пример: Дистрибуција на години
    plt.figure(figsize=(8, 5))
    sns.histplot(df["age"], kde=True, bins=10)
    plt.title("Дистрибуција на Возраст")
    plt.show()

if __name__ == "__main__":
    visualize_data()

