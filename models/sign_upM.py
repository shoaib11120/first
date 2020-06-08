import pymongo
from pymongo import MongoClient

class Sign_up(object):
	"""docstring for Sign_up"""
	def __init__(self):
		self.client=MongoClient()
		self.db=self.client.first_web

	def setUser(self,data):
		print("reached",data)
		