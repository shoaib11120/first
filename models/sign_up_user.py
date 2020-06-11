import pymongo
from pymongo import MongoClient
import bcrypt

class user:
	"""docstring for Sign_up"""
	def __init__(self):
		self.client=MongoClient()
		self.db=self.client.first_web
		self.Users=self.db.users

	def setUser(self,username,full_name,email,password,c_password):
		username=username.strip()
		full_name=full_name.strip()
		email=email.strip()
		password=password.strip()
		c_password=c_password.strip()
		if password==c_password:
			password=bcrypt.hashpw(c_password.encode(),bcrypt.gensalt())
			id= self.Users.insert_one({"username":username,"full_name":full_name,"email":email,"password":password })
			return str(username)
		else:
			return "PError"
	