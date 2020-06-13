import pymongo
from pymongo import MongoClient

class profile:
	"""docstring for Sign_up"""
	def __init__(self):
		self.client=MongoClient()
		self.db=self.client.first_web
		self.Users=self.db.users

	def updateAvatar(self,update):
		updated=self.Users.update_one({"username":update['username']},
									  {"$set":{"img":update['img']}})
		print(str(updated))

		return self.Users.find_one({"username":update['username']})