""" a seed script w/ initial schema and mock values"""
import pyodbc 

# docker run -e 'ACCEPT_EULA=Y' -e 'MSSQL_SA_PASSWORD=1q2w3e%&!' -p 1433:1433 -d microsoft/mssql-server-linux

# OPEN CONNECTION TO DB
server = '127.0.0.1,1433' 
database = 'master' 
username = 'SA' 
password = '1q2w3e%&!' 
con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password, autocommit=True)
cursor = con.cursor()

# USING MAIN DB
print('');
print('-----------------------------------------------------------')
print('STARTING SEED SCRIPT')
print('-----------------------------------------------------------')
print('');
print(con)
print(cursor)
print('');
string = "USE master"
print('-----------------------------------------------------------')
print(string)
print('-----------------------------------------------------------')
cursor.execute(string)
con.commit()

# CREATE THE DATABASE
print('');
string = "CREATE DATABASE client_sensors"
print('-----------------------------------------------------------')
print(string)
print('-----------------------------------------------------------')
cursor.execute(string)
con.commit()
print('');

# CREATE TABLE AND INSERT VALUES
string = """
            USE client_sensors
            CREATE TABLE sensors
            (	
                  timestamps nvarchar(max) not null,
                  valores int not null
            )
            INSERT INTO sensors (timestamps,valores) VALUES('2019-06-05 14:35:48.917309', 35412353)
            INSERT INTO sensors (timestamps,valores) VALUES('2019-08-05 14:55:48.917309', 89901233)
            INSERT INTO sensors (timestamps,valores) VALUES('2019-06-05 14:12:48.917309', 35412353)
            INSERT INTO sensors (timestamps,valores) VALUES('2019-06-05 14:55:48.917309', 34134122)
            INSERT INTO sensors (timestamps,valores) VALUES('2019-06-05 15:35:48.917309', 35412353)
            INSERT INTO sensors (timestamps,valores) VALUES('2019-07-05 14:55:48.917309', 09876523)
         """
print('-----------------------------------------------------------')
print(string)
print('-----------------------------------------------------------')
cursor.execute(string)
con.commit()
print('');

# QUERY TABLE
string = "SELECT * FROM [client_sensors].[dbo].[sensors] ORDER BY timestamps DESC"
print(string);
cursor.execute(string) 
row = cursor.fetchall()
print('-----------------------------------------------------------')
print('QUERY RESULT')
print('-----------------------------------------------------------')
for i in range(len(row)):
      print(row[i])
print('');

# CLOSING THE CONNECTION
print('-----------------------------------------------------------')
print('ENDING SEED SCRIPT')
print('-----------------------------------------------------------')
cursor.close()
con.close() 