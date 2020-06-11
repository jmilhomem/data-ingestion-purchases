"""Config file."""
import configparser

from pathlib import Path
from pipeline.ingestion import ingest_transaction_csv

def config():
    home = str(Path.home())
    data_file = home + '/.config/config.ini'
    
    config = configparser.ConfigParser()
    config.read(data_file)
    
    
    db = config.get('Default', 'db')
    host = config.get('Default', 'host')
    port = config.get('Default', 'port')
    region = config.get('Default', 'region')
    user = config.get('Default', 'user')
    password = config.get('Default', 'pass')
    schema = config.get('Default', 'schema')
    table = config.get('Default', 'table')
    file = config.get('Default', 'file')
    email_to = config.get('Default', 'email_to')
    email_user = config.get('Default', 'email_user')
    email_password = config.get('Default', 'email_password')
    email_recipient = config.get('Default', 'email_recipient')


    return {"db" : db,
            "host" : host, 
            "port": port,
            "region": region,
            "user": user,
            "password": password,
            "schema" : schema,
            "table" : table,
            "file" : file,
            "enginedb" : f'postgresql://{user}:{password}@{db}.{host}.{region}.rds.amazonaws.com:{port}/{user}',
            "email_to" : email_to,
            "email_user" : email_user,
            "email_password" : email_password,
            "email_recipient" : email_recipient
            }
