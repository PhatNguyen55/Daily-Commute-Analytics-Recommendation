import psycopg2

def load_data_to_redshift(host, port, dbname, user, password, s3_path, table_name, iam_role):
    conn_str = f"host={host} port={port} dbname={dbname} user={user} password={password}"
    conn = psycopg2.connect(conn_str)
    cur = conn.cursor()
    
    copy_query = f"""
    COPY {table_name}
    FROM '{s3_path}'
    IAM_ROLE '{iam_role}'
    CSV IGNOREHEADER 1;
    """
    try:
        cur.execute(copy_query)
        conn.commit()
        print("Data loaded successfully to Redshift.")
    except Exception as e:
        print("Error loading data to Redshift:", e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    load_data_to_redshift(
        host='your-redshift-endpoint',
        port=5439,
        dbname='your_db',
        user='your_user',
        password='your_password',
        s3_path='s3://your-s3-bucket/data/commute_data.csv',
        table_name='commute_table',
        iam_role='arn:aws:iam::your_account:role/yourRedshiftRole'
    )
