import pandas as pd
import pyodbc 
from time import time

server = '127.0.0.1,1433' 
database = 'master' 
username = 'SA' 
password = '1q2w3e%&!' 
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password, autocommit=True)
cursor = connection.cursor()

csv_file = open('output.csv', 'w')

def get_total_rows():
    query_count = " SELECT COUNT(*) FROM [client_sensors].[dbo].[sensors] "
    total_rows = cursor.execute(query_count).fetchone()
    return total_rows[0]


def extract_load():
    start = time()
    query = "SELECT * FROM [client_sensors].[dbo].[sensors] ORDER BY timestamps DESC"
    cursor.execute(query)

    # Get data in batches
    while 1:
        raw_tuple = cursor.fetchmany(1000)

        df = pd.DataFrame(cursor.fetchmany(1000))
        # We are done if there are no data
        if len(df) == 0:
            break
        # Let's write to the file
        else:
            df.to_csv(csv_file, header=False)
    # Clean up
    csv_file.close()
    cursor.close()
    connection.close()
    total_time = time() - start
    print('Process took', total_time, ' seconds')
    print("---------------------------------------------- ")

if __name__ == '__main__':
    print("---------------------------------------------- ")
    print("Start random data generator ")
    print('Total records on db is',get_total_rows())
    print("---------------------------------------------- ")
    extract_load()