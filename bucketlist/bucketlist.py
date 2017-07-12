#an empty list to store my items
BucketItems=[]

class Bucketlist():


	Bucketlists={}
	
		#initializing class instance variables
	def __init__(self,post=None,description=None,owner=None):
		self.post=post
		self.description=description
		self.owner=owner


		# defining method to create bucket list	
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

		# defining method to delete bucket list		
	def delete(self,post):
		if post in self.Bucketlists.keys():
			print('found')
			print(post)
			del self.Bucketlists[post]		
			return 1
		else:
			return 2

		# defining method to delete bucket list		
	def edit(self,old,post,description,owner):
		if  post!='':
			if description!='':
				del self.Bucketlists[old]
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

	# defining method to get all bucket lists
	def get_bucket_lists(self):
		return self.Bucketlists	
		
	# defining method to get one bucket lists
	def get_bucket_list(self,post):
		return self.Bucketlists[post]
		
		# defining method to create an item in a bucket
	def createItem(self,post,item):
		if item !='':
			items={}
			items['item']=item 
			items['post']=post
			BucketItems.append(items)
			return 1
		else:
			return 2