USE master
GO
CREATE DATABASE client_sensors
GO

USE client_sensors
--se nao especificar o parametro do nvarchar default é 1
CREATE TABLE sensors (	timestamps nvarchar(max) not null, 
						 valores int not null)
GO

INSERT INTO sensors VALUES('2019-06-05 14:35:48.917309', 35412353)
INSERT INTO sensors (timestamps,valores) VALUES('2019-06-05 14:55:48.917309', 1212351233)

SELECT TOP (1000) [timestamps]
      ,[valores]
 FROM [client_sensors].[dbo].[sensors]
 

--begin tran 
--DELETE FROM [dbo].[sensors]
--      WHERE valores = 1212351233
--commit