"""Ingestion application."""
import os

from utils.config import config
from utils.app_logging import define_log
from utils.import_files import import_dbt_log
from utils.import_files import import_ingestion_log
from utils.send_email import send_email


def main_etl_process():
    """Execute the whole ETL process."""
    to = config["email_to"]
    user = config["email_user"]
    password = config["email_password"]
    recipient = config["email_recipient"]    

    log.info("Execute the ./dbt_seed.sh.")
    os.system("./pipeline/dbt_seed.sh")    

    log.info("Read the dbt_seed log.")
    result_dbt_seed = import_dbt_log("logs/temp/dbt_seed.log")    

    if result_dbt_seed == "Completed successfully":
        log.info("DBT Seed executed.")    

        log.info("Execute Ingestion Process")
        os.system("python main_ingestion.py")
        os.system("tail -n2 logs/logs.log >> logs/temp/ingestion.log")
        result_ingestion = import_ingestion_log("logs/temp/ingestion.log")    

        if result_ingestion == "Bulk Insert done successfully.":    

            log.info("Execute DBT Process")
            os.system("./pipeline/dbt_execution.sh")
            result_dbt_run = import_dbt_log("logs/temp/dbt_run.log")    

            if result_dbt_run == "Completed successfully":
                log.info("DBT Run executed.")    

                log.info("Execute DBT Test")
                os.system("./pipeline/dbt_test.sh")
                result_dbt_test = import_dbt_log("logs/temp/dbt_test.log")    

                if result_dbt_test == "Completed successfully":
                    log.info("DBT Test executed.")   

                    log.info("Remove temporary log files")
                    os.system("rm -r logs/temp/*")    

                    subject = 'ETL Process - Completed successfully'
                    send_email(subject, recipient, to, subject, user, password)    

                    log.info("Completed successfully")

                else:
                    subject = 'ETL Process - Error during dbt execution!'
                    send_email(subject, recipient, to, subject, user, password)
                    log.error("Failed during dbt execution!")

            else:
                subject = 'ETL Process - Error during dbt execution!'
                send_email(subject, recipient, to, subject, user, password)
                log.error("Failed during dbt execution!")
        else:
            subject = 'ETL Process - Error during the ingestion process!'
            send_email(subject, recipient, to, subject, user, password)
            log.error("Failed during ingestion process!")
    else:
        subject = 'ETL Process - Error during the dbt seed execution!'
        send_email(subject, recipient, to, subject, user, password)
        log.error("Failed during dbt seed execution!")    

    log.info("Data Process Finished")


if __name__ == "__main__":
    log = define_log()
    log.info("Ingestion Process Started.")
    config = config()
    main_etl_process()
