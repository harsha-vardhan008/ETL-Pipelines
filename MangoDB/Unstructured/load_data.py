from datetime import datetime
import configparser
from sqlalchemy import create_engine
import urllib
import pandas as pd

def connect_to_sqlserver():
    config = configparser.ConfigParser()
    config.read(r"C:\Users\Harshavardhan\Documents\python_tutorials\MangoDB\config.config")

    Driver = config['ssms']['Driver']
    Server = config['ssms']['Server']
    Database = config['ssms']['Database']
    trusted_conn = config['ssms']['Trusted_Connection']

    params = urllib.parse.quote_plus(
        f"DRIVER={Driver};SERVER={Server};DATABASE={Database};Trusted_Connection={trusted_conn}"
    )

    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
    return engine

def load_to_sql(df: pd.DataFrame, table_name: str, engine):
    df.to_sql(name=table_name, con=engine, if_exists="replace", index=False)
    print(f"Loaded {len(df)} rows into SQL Server table '{table_name}'")

connect_to_sqlserver()