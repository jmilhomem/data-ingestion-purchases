"""Ingestion application."""
from utils.config import config
from pipeline.ingestion import ingest_transaction_csv
from utils.app_logging import define_log


def main_ingestion():
    enginedb = config["enginedb"]
    schema = config["schema"]
    table = config["table"]
    file = config["file"]    

    result = ingest_transaction_csv(enginedb, schema, table, file)
    if result is True:
        log.info("Bulk Insert done successfully.")    

    log.info("Ingestion Process Finished.")


if __name__ == "__main__":
    log = define_log()
    log.info("Ingestion Process Started.")
    config = config()
    main_ingestion()
