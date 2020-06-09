import pymongo
from pymongo import MongoClient
import bcrypt

class user:
	"""docstring for Sign_up"""
	def __init__(self):
		self.client=MongoClient()
		self.db=self.client.first_web
		self.Users=self.db.users
		self.username=""
		self.full_name=""
		self.email=""
		self.password=""
		self.c_password=""

	def setUser(self,username,full_name,email,password,c_password):
		self.username=username.strip()
		self.full_name=full_name.strip()
		self.email=email.strip()
		self.password=password.strip()
		self.c_password=c_password.strip()
		if password==c_password:
			self.password=bcrypt.hashpw(self.c_password.encode(),bcrypt.gensalt())
			self.id=self.Users.insert({"username":self.username,
				"full_name":self.full_name,
				"email":self.email,
				"password":self.password})
			return "success"
		else:
			return "PError"
	def getUName(self):
		return self.username

	def getFName(self):
		return self.full_name

	def getEmail(self):
		return self.email

	def getPassword(self):
		return self.c_password
	
	def updateFName(self,value):
		try:
			oQuery={"username":self.getUName()}
			nQuery={"$set":{"username":val}}
			return 1
		except:
			return -1

	def updateEmail(self,value):
		try:
			oQuery={"email":self.getEmail()}
			nQuery={"$set":{"email":val}}
			return 1
		except:
			return -1

	def updatePassword(self,value):
		try:
			oQuery={"password":self.getPassword()}
			nQuery={"$set":{"password":val}}
			return 1
		except:
			return -1

	