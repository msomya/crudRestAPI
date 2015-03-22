#!/usr/bin/python
#table name: production
#database schema: production(Item varchar, year varchar, data varchar)
#primary key: Item+year
#the schema is made this way keeping in mind the future need to calculate max or min in a particular year
import MySQLdb

class dataImport(object):
	def __init__(self):
		self.id = 0
	def insertData(self,db,cursor,filename,dbname):
		#insert the data from the file datafile.csv(here)
		fo = open(filename,"r")
		line = fo.readline()
		#the first line is needed for the column year
		column = line.split(',')
		line = fo.readline()
		while line:
			words = line.split(',')
			for i in range(1,len(words)):
				self.id = self.id+1;
				sql = "insert into production(id, item, year, data) values ("+str(self.id)+", '"+words[0][1:-1]+"', "
				if i == len(words)-1:
					#because the last letter of each last word in a line is '\n'
					#the range is added is to remove "
					sql += "'" + column[i][1:-2] + "', " + words[i][1:-2] + ")"
				else:
					sql += "'" + column[i][1:-1] + "', " + words[i][1:-1] + ")"
				try:
					#if any error occurs like database doesnt exist,etc
					cursor.execute(sql)
					db.commit()
				except:
					db.rollback()
			line = fo.readline()
		fo.close()

class DBManage(object):
	def __init__(self):
		self.servaddr = "localhost" #None
		self.name = "root" #None
		self.password = "root" #None
		self.database = "elecIT" #None
		#fpoint = open("database.cnf", "w")
		#fpoint.write('[client]\ndefault-character-set = utf8\n')
		#fpoint.close()

	def setServerAddr(self,s):
		self.servaddr = s
	
	def setName(self,n):
		self.name = n
		#fpoint = open("database.cnf","a")
		#fpoint.write('user = '+self.name+'\n')
		#fpoint.close()

	def setPassword(self,p):
		self.password = p
		#fpoint = open("database.cnf","a")
		#fpoint.write('password = '+self.password+'\n')
		#fpoint.close()

	def setDBname(self,dbname):
		self.database = dbname
		#fpoint = open("database.cnf","a")
		#fpoint.write('database = '+self.database+'\n')
		#fpoint.close()
	
	def getSocket(self):
		return self.servaddr
	
	def getName(self):
		return self.name

	def getPassword(self):
		return self.password

	def getDBname(self):
		return self.database
		
	def connectDB(self):
		#connect to the database
		self.db = MySQLdb.connect(self.servaddr,self.name,self.password,self.database)
		return self.db

	def createTable(self):
		#creating a table in the database
		self.cursor = self.db.cursor()
		self.cursor.execute("drop table if exists production")
		sql = "create table production(id int not null auto_increment,item varchar(100) not null, year varchar(20) not null, data int not null, primary key(id) unique(item,year))"
		self.cursor.execute(sql)
		return self.cursor

	def closeDB(self):
		#closing the database
		self.db.close()


d = dataImport()
database = DBManage()
#database.setServerAddr(raw_input("Enter the server address: "))
#database.setName(raw_input("Enter the username: "))
#database.setPassword(raw_input("Enter the password: "))
#database.setDBname(raw_input("Enter the database name: "))
db = database.connectDB()
cursor = database.createTable()
d.insertData(db,cursor,"dataSets/datafile.csv",database.getDBname())
database.closeDB()
