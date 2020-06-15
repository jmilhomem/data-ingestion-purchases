"""Ingestion process."""
from sql.ingestion.transactions import drop_table, create_transaction_table
from utils.database_operations import insert_data_upon_csv
from utils.app_logging import define_log

log = define_log()

def ingest_transaction_csv(enginedb, schema, table, file):
    """Import data upon CSV into db's table.

    :param enginedb: string -> string connection
    :param schema: string -> db's schema 
    :param table: string -> table's name
    :param file: string -> file's name
    :return boolean -> True if success 
    """ 
    log.info("Drop transaction raw table.")
    sql_drop = drop_table(schema, table)

    log.info("Recreate the transaction raw table.")
    sql_create = create_transaction_table(schema, table)

    log.info("Insert transaction raw data into the table.")
    return insert_data_upon_csv(enginedb, schema, table, file, sql_drop, sql_create)


def main_ingestion(enginedb, schema, table, file):
    """Apply the ingestion process.

    :param enginedb: string -> string connection
    :param schema: string -> db's schema 
    :param table: string -> table's name
    :param file: string -> file's name
    """ 
    result = ingest_transaction_csv(enginedb, schema, table, file)
    if result is True:
        log.info("Bulk Insert done successfully.")    

    log.info("Ingestion Process Finished.")
