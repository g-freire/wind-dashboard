import pyodbc 
from random import random, uniform
from time import sleep
import datetime

server = '127.0.0.1,1433' 
database = 'client_sensors' 
username = 'SA' 
password = '1q2w3e%&!' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#Sample insert query
# cursor.execute("INSERT SalesLT.Product (Name, ProductNumber, StandardCost, ListPrice, SellStartDate) OUTPUT INSERTED.ProductID VALUES ('SQL Server Express New 20', 'SQLEXPRESS New 20', 0, 0, CURRENT_TIMESTAMP )") 
# row = cursor.fetchone()

# while row: 
#     print 'Inserted Product key is ' + str(row[0]) 
#     row = cursor.fetchone()

def generate_random_wind_contract():
    try:
        while 1:
            timestamp = str(datetime.datetime.now())
            sensor_value = round(uniform(0.25, 0.6)*1000, 1)
            print("INSERT INTO [client_sensors].[dbo].[sensors] VALUES('{}',{})".format(timestamp, sensor_value))
            cursor.execute("INSERT INTO [client_sensors].[dbo].[sensors] VALUES('{}',{})".format(timestamp, sensor_value))
            cnxn.commit()
            sleep(2)
            
    except Exception as e:print(e)
    finally:
        cnxn.close()

if __name__ == '__main__':
    generate_random_wind_contract()