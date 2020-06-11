#from sqlalchemy import create_engine
import psycopg2
from utils.app_logging import define_log

def insert_data_upon_csv(enginedb, schema, table, file, *query):
    """Import data upon CSV into db's table.

    :param enginedb: string -> connection string
    :param schema: string -> db's schema
    :param table: string -> db's table
    :param query: string -> query to execute
    :return boolean -> True if success 
    """ 
    log = define_log()
    
    try:
        conn = psycopg2.connect(enginedb)    
        cur = conn.cursor()
        
        # Drop and recreate the table
        for q in query:
            cur.execute(q)
        
        # Read the file and insert into db's table
        with open(file, "r") as f:
            next(f) # Skip the header row.
            cur.copy_from(f, f"{schema}.{table}", sep=",")        

        conn.commit()
        return True
    
    except Exception as e:
        raise(log.error(e))
