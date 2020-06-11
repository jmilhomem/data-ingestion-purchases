"""Ingestion process."""
from sql.ingestion.transactions import drop_table, create_transaction_table
from utils.database_operations import insert_data_upon_csv
from utils.app_logging import define_log

def ingest_transaction_csv(enginedb, schema, table, file):
    """Import data upon CSV into db's table.

    :param schema: string -> db's schema
    :Insert new data into the table
    :return boolean -> True if success 
    """ 
    log = define_log()

    log.info("Drop transaction raw table.")
    sql_drop = drop_table(schema, table)

    log.info("Recreate the transaction raw table.")
    sql_create = create_transaction_table(schema, table)

    log.info("Insert transaction raw data into the table.")
    return insert_data_upon_csv(enginedb, schema, table, file, sql_drop, sql_create)
