import pandas as pd
import numpy as np
import pyodbc

raw_csv = pd.read_csv('person_raw.csv')[['Name', 'Age', 'City']]


conn = pyodbc.connect('Driver={SQL Server};'
'Server=HN-PTNC-ANHBT\SQLEXPRESS;'
'Database=testDB;'
'Trusted_Connection=yes;')

cursor = conn.cursor()

#cursor.execute('''
#                INSERT INTO TestDB.dbo.Person (Name, Age, City, Append_date)
#                VALUES
#                (N'Nguyễn Hà PHương',20, N'Hà Nội', GETDATE()),
#                (N'AnhBui',6, N'Cincinnati', GETDATE())
#                ''')
#conn.commit()

for row in raw_csv.itertuples():
	cursor.execute('''
	                INSERT INTO TestDB.dbo.Person (Name, Age, City, Append_date)
	                VALUES (?,?,?,?)
	                ''',
	                row.Name,
	                row.Age,
	                row.City,
	                pd.to_datetime('today')
	                )
conn.commit()




sql_query = pd.read_sql_query('SELECT * FROM dbo.Person',conn)
print(sql_query)
print(type(sql_query))

#db_index = pd.read_sql("""SELECT *   FROM dbo.GN_real_data_0325
             #; """, con_bsc)

sql_query.to_csv('person.csv',encoding='utf-8-sig')


#snippet worked
def read(conn):
	print("Read")
	cursor.execute("select * from Person")
	for row in cursor:
		print(f'row = {row}')
		
def create(conn):
	print('create')
	cursor.execute(
		'insert into Person(Name, Age, City, Append_date) VALUES(?, ?,?,?);',
		('Nguyễn Hà PHương1',20, 'Hà Nội', '2020')
	)
	conn.commit()
	read(conn)

def delete(conn):
	print('delete')
	cursor.execute(
		"delete from Person Where Name = 'test1'"
	)
	conn.commit()
	read(conn)
#read(conn)
#create(conn)
delete(conn)


#cursor.execute('SELECT * FROM dbo.Person')

#for row in cursor:
#    print(row)