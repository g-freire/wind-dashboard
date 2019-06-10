use master
go
create database client_sensors
go

use client_sensors
--se nao especificar o parametro do nvarchar default é 1
create table sensors (	timestamps nvarchar(max) not null, 
						 valores int not null)
go

insert into sensors values('2019-06-05 14:35:48.917309', 35412353)
insert into sensors (timestamps,valores) values('2019-06-05 14:55:48.917309', 1212351233)

SELECT TOP (1000) [timestamps]
      ,[valores]
 FROM [client_sensors].[dbo].[sensors]  