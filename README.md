
# Purchases Application processes
> This application is responsible for:
> 1. Ingest the raw data from transactions.csv file
> 2. Execute the whole pipeline: ingesting the transactions.file data + dbt process.

![alt text](https://blog.hotmart.com/blog/2019/07/BLOG_ciclo-de-compra-670x419.png)


## Data File description:

__transactions__ - contains transaction history for all customers for a period of at least 1 year prior to their offered incentive
- __id__ - A unique id representing a customer
- __chain__ - An integer representing a store chain
- __dept__ - An aggregate grouping of the Category (e.g. water)
- __category__ - The product category (e.g. sparkling water)
- __company__ - An id of the company that sells the item
- __brand__ - An id of the brand to which the item belongs
- __date__ - The date of purchase
- __productsize__ - The amount of the product purchase (e.g. 16 oz of water)
- __productmeasure__ - The units of the product purchase (e.g. ounces)
- __purchasequantity__ - The number of units purchased
- __purchaseamount__ - The dollar amount of the purchase


Reference:  
https://www.kaggle.com/c/acquire-valued-shoppers-challenge/data?select=offers.csv.gz  


## Technical Description:

- __main_ingestion.py__ - It drops the transaction raw table if it exists, then create the transaction raw table if it not exists. Finally, it ingests the data from the csv file stored into /data folder.
- __main_etl_processes.py__ - It executes the whole data pipeline (GetDBT + Python) as following:
1. Execute the dbt seed to import the files.
2. Execute the main_ingestion.py application.
3. Execute the dbt run to execute the whole etl pipeline.
4. Remove temporary log files

## Dependencies:
To execute the ingestion process(__main_ingestion.py__ application):
* a Postgres database instance created at AWS RDS.
* config.ini file filled and available on __~/.config__ folder
* python 3.6
* make

To execute the whole pipeline (__main_etl_processes.py__ application):
* get dbt installed and the dbt project cloned. Check more details here.
* a Postgres database instance created at AWS RDS.
* config.ini file filled and available on __~/.config__ folder
* python 3.6
* make  

Execution:
* Run: ```make ``` to create the environment

## Run
Start your python virtualenv with ```source .venv/bin/activate```

* Run: ```make run``` to start the main ingestion process.
