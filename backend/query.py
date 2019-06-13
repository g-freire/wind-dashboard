import pyodbc 

server = '127.0.0.1,1433' 
database = 'master' 
username = 'SA' 
password = '1q2w3e%&!' 
con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password, autocommit=True)
cursor = con.cursor()

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