import pymongo
from pymongo import MongoClient
import bcrypt

class user:
	"""docstring for Sign_up"""
	def __init__(self):
		self.client=MongoClient()
		self.db=self.client.first_web
		self.Users=self.db.users

	def getUser(self,username,password):
		username=username.strip()
		password=password.strip()

		user=self.Users.find_one({"username":username})
		if user:
			if bcrypt.checkpw(password.encode(),user["password"].encode()):
				return user
			else:
				return "PError"
		else:
			return "UError"