"""Import log file."""
import re

def import_dbt_log(folder_file):
    """Import dbt's log file and return the status result

    :param folder_file: string -> connection string
    :return string -> status result 
    """ 
    logfile = open(folder_file, "r")
    data_file = [file.strip() for file in logfile.readlines()]
    logfile.close()

    return data_file[0][5:27]


def import_ingestion_log(folder_file):
    """Import dbt's log file and return the status result

    :param folder_file: string -> connection string
    :return string -> status result 
    """ 
    logfile = open(folder_file, "r")
    data_file = [file.strip() for file in logfile.readlines()]
    logfile.close()

    return data_file[0][52:]
