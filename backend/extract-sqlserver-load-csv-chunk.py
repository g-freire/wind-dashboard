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


def extract_load_chunk(query_size=10000):
    start = time()
    last_timestamp = '2019-06-05 14:35:48.917309'

    # Get data in batches
    try:
        while 1:
            # maybe refactor connection string to vertical query
            sql_server_read_query = " SELECT TOP ({}) [timestamps],[valores] FROM [client_sensors].[dbo].[sensors] WHERE timestamps > '{}'".format(query_size,last_timestamp)
            cursor.execute(sql_server_read_query)
            df = pd.DataFrame(cursor.fetchmany(query_size))
            if len(df) == 0:
                break
            # if len(df) < 1000:
            #     break
            else:
                df.to_csv(csv_file, header=False)
                last_row_timestamp = df.tail(1)[0].tolist()[0][0]
                last_timestamp = last_row_timestamp
    except Exception as e:print(e)

    finally:
        csv_file.close()
        cursor.close()
        connection.close()
        total_time = time() - start
        print('Process took', total_time, ' seconds')
        print("---------------------------------------------- ")

if __name__ == '__main__':
    print("---------------------------------------------- ")
    print("SQLServer Chunk Extractor to CSV")
    print('Total records on db is',get_total_rows())
    print("---------------------------------------------- ")
    # extract_load_chunk(10000)
    extract_load_chunk(100000)


# maybe do a 10% on the record count as chunk decision
