#!/bin/bash

# Go to dbt repository
cd ~/repos/dbt_purchases_project

# Insert the date information into log
echo "DBT RUN EXECUTION" >> logs/log_execution.log
date +"%F %T,%3N" >> logs/log_execution.log

# Execute the seed
dbt run >> logs/log_execution.log

# Copy the dbt seed log file to Python folder
tail -n3 logs/log_execution.log >> ~/repos/data-ingestion-purchases/logs/temp/dbt_run.log
