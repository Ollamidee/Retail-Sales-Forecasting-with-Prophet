import mysql.connector
import pandas as pd
import pymysql
from sqlalchemy import create_engine
import os



#Retrieving the SQL credentials from the environment variable

user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
host = os.getenv("MYSQL_HOST")
db = os.getenv("MYSQL_DB")

#Reading the dataset

df = pd.read_csv(r"C:\Users\LENOVO\Documents\python_set\machine_learning\Projects\sales_forcasting\data.csv\data.csv",
                 encoding='windows-1252')

# Changing the column names in the dataset to match the corresponding ones in the database

df = df.rename(columns = {"InvoiceNo" : "invoice_no",
                     "StockCode" : "product_id",
                     "Description" : "product_name",
                     "Quantity" : "quantity",
                     "InvoiceDate" : "invoice_date",
                     "CustomerID" : "customer_id",
                     "Country" : "country",
                    "UnitPrice" : "unit_price"
                    })




#Filling missing values
df["customer_id"] = df.customer_id.fillna(0)
df["product_name"] = df["product_name"].fillna("UNKNOWN")


#Creating dataframes to match the corresponding table_names in the database
products = df[["product_id", "product_name", "unit_price"]].copy()
customers = df[["customer_id", "country"]].copy()
invoices = df[["invoice_no", "invoice_date", "customer_id"]].copy()
invoice_item = df[["invoice_no", "product_id", "quantity"]].copy()



#Changing to the correct date format for MySQL
invoices['invoice_date'] = pd.to_datetime(df['invoice_date'], format='%m/%d/%Y %H:%M')
invoices = invoices.drop_duplicates(subset='invoice_no')


#Droppind Duplicates
products['product_id'] = products['product_id'].str.upper()
products = products.drop_duplicates(subset='product_id')

customers = customers.drop_duplicates(subset='customer_id')


valid_product_ids = products['product_id'].unique()
invoice_item = invoice_item[invoice_item['product_id'].str.upper().isin(valid_product_ids)]
invoice_item = invoice_item.drop_duplicates(subset='invoice_no')





#Connecting to MySQL
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db}")



#Creating a dictionary dataframe to target table names

dataframes = {
    "products" : products,
    "customers" : customers,
    "invoices" : invoices,
    "invoice_item" : invoice_item
}


#Looping through to insert each dataframe to the corresponding table_name in the database

for table_name, dataframe in dataframes.items():
    try:
        dataframe.to_sql(name = table_name, con =engine, if_exists = 'append', index= False)
        print(f"Successfully Inserted data into {table_name}")
    except Exception as e:
        print(f"Failed to insert into {table_name}: {e}")
