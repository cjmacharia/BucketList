#an empty list to store my items
BucketItems=[]

class Bucketlist():


	Bucketlists={}
	
		#initializing class instance variables
	def __init__(self,post=None,description=None,owner=None):
		self.post=post
		self.description=description
		self.owner=owner

	def create(self,post, description, owner):
		if description!=''and post!='':
			if post not in self.Bucketlists.keys():
				self.Bucketlists[post] = {
				'description':description,
				'post':post,
				'owner':owner,
				}
				
				return 1
			else:
				return 2
		else:
			return 3	
