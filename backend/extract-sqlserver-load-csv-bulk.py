import pandas as pd
import pyodbc 
from time import time

server = '127.0.0.1,1433' 
database = 'master' 
username = 'SA' 
password = '1q2w3e%&!' 
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password, autocommit=True)
cursor = connection.cursor()

csv_file = open('output_bulk.csv', 'w')

def get_total_rows():
    query_count = " SELECT COUNT(*) FROM [client_sensors].[dbo].[sensors] "
    total_rows = cursor.execute(query_count).fetchone()
    return total_rows[0]


def extract_load():
    start = time()

    last_timestamp = '2019-06-05 14:35:48.917309'

    # Get data in batches
    while 1:
        try:
            query_1000 = " SELECT TOP (100000) [timestamps],[valores] FROM [client_sensors].[dbo].[sensors] WHERE timestamps > '{}'".format(last_timestamp)
            cursor.execute(query_1000)
            df = pd.DataFrame(cursor.fetchmany(100000))
            last_row_timestamp = df.tail(1)[0].tolist()[0][0]
            # We are done if there are no data
            if len(df) == 0:
                break
            # Let's write to the file
            else:
                df.to_csv(csv_file, header=False)
                last_timestamp = last_row_timestamp

        except Exception as e:print(e)

    total_time = time() - start
    print('Process took', total_time, ' seconds')
    # Clean up
    csv_file.close()
    cursor.close()
    connection.close()

a = get_total_rows()
print('Total records on db is',a)

extract_load()
