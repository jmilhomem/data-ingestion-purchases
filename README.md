
# Purchases Data Pipeline Project
> This application is responsible for:
> 1. Ingest the raw data from transactions.csv file
> 2. Execute the full pipeline: ingestion of transactions file data + dbt transformation + dbt test.

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

This script contains 1 main module:
- __main_etl_processes.py__ - It executes the whole data pipeline (GetDBT + Python) as following:
  1. Execute the __dbt seed__ to import the files.
  2. Drop the transaction raw table if it exists.
  3. Create the transaction raw table if it not exists.
  4. Ingest data from the csv file stored into __/data__ folder.
  5. Execute the __dbt run__ to execute the whole etl pipeline.
  6. Execute the __dbt test__ to execute the tests defined for the models.
  7. Remove temporary log files

## Dependencies:
To execute the full pipeline (__main_etl_processes.py__ application):
* get dbt installed and the [dbt project cloned](https://github.com/jmilhomem/dbt_purchases_project) 
* a Postgres database instance created at AWS RDS.
* config.ini file filled and available in __~/.config__ folder
* profiles.yml file filled and available in __~/.dbt__ folder
* python 3.6
* make  

Execution:
* Run: ```make ``` to create the environment

## Run
Start your python virtualenv with ```source .venv/bin/activate```

* Run: ```make run``` to start the main ingestion process.
