"""SQL commands."""

def drop_table(schema, table):
    return f"""DROP TABLE IF EXISTS {schema}.{table}"""


def create_transaction_table(schema, table):
    return f"""CREATE TABLE IF NOT EXISTS {schema}.{table} (
               id bigint NULL,
               "chain" bigint NULL,
               dept int4 NULL,
               category bigint NULL,
               company bigint NULL,
               brand bigint NULL,
               "date" date NULL,
               productsize float8 NULL,
               productmeasure text NULL,
               purchasequantity bigint NULL,
               purchaseamount float8 NULL
           )"""
