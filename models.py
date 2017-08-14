import pymongo

def get_coll():
	client = pymongo.MongoClient('127.0.0.1',27017)
	db = client.mydb
	user = db.col
	
	return user

class User(object):
	def __init__(self,name,sex):
		self.name = name
		self.sex = sex

	def save(self):
		user = {'name':self.name,'sex':self.sex}
		coll = get_coll()
		id = coll.insert(user)
		print id
	
	@staticmethod
	def query_users():
		users = get_coll().find()
		return users
	
