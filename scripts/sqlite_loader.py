import sqlite3
import pandas as pd

def load_data_to_sqlite(csv_file, db_path):
    conn = sqlite3.connect(db_path)
    df = pd.read_csv(csv_file)
    df.to_sql('commute_data', conn, if_exists='replace', index=False)
    conn.close()

if __name__ == "__main__":
    load_data_to_sqlite('commute_data.csv', 'commute_data.db')
