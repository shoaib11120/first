import pymongo
from pymongo import MongoClient

class Sign_up:
	"""docstring for Sign_up"""
	def __init__(self):
		self.client=MongoClient()
		self.db=self.client.first_web
		self.Users=self.db.users

	def setUser(self,username,full_name,email,password):
		id=self.Users.insert_one({"username":username,"full_name":full_name,"email":email,"password":password}).inserted_id
		print("id:",id)
		