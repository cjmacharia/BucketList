#an empty list to store my items
BucketItems=[]

class Bucketlist():


	Bucketlists={}
	
		#initializing class instance variables
	def __init__(self,post=None,description=None,owner=None):
		self.post=post
		self.description=description
		self.owner=owner
