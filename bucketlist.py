#an empty list to store my items
BucketItems = []

class Bucketlist(object):


	Bucketlists = {}
	
	
		#initializing class instance variables
	def __init__(self,post=None,description=None,owner=None):
		self.post = post
		self.description = description
		self.owner = owner


		# defining method to create bucket list	
	def create(self,post, description, owner):
		if description!=''and post!='':
			my_buckets = self.get_mybucket_lists(owner)
			if my_buckets != {}:
				
				if post not in my_buckets.keys():
					self.Bucketlists[post] = {
					'description':description,
					'post':post,
					'owner':owner,
					}
					return 1
				else:
					return 2

			else:
				self.Bucketlists[post] = {
				'description':description,
				'post':post,
				'owner':owner,
				}
				return 1
		else:
			return 3

		# defining method to delete bucket list		
	def delete(self,post):
		if post in self.Bucketlists.keys():
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

	def get_mybucket_lists(self, owner):
		data=self.Bucketlists
		my_buckets = {}
		for post in data.keys():
			bucket=data[post]
			description=bucket['description']
			bucketOwner=bucket['owner']
			if bucketOwner==owner:
				my_buckets[post] = {
				'description':description,
				'post':post,
				'owner':owner,
				}
			else:
				result= my_buckets
		return my_buckets 		
		
		# defining method to get one bucket lists
	def get_bucket_list(self,post):
		return self.Bucketlists[post]
		
		# defining method to create an item in a bucket
	def createItem(self,post,item):
		if item!='':
			items= {}
			items['item'] = item 
			items['post'] = post
			print (items)
			BucketItems.append(items)
			print(BucketItems)
			return 1
		else:
			return 2	
				
		# defining method to get one bucket lists		
	def getItems(self):
		return BucketItems		

		# defining method to create an item in a bucket	
	def itemEdit(self,item,old):
		if item!='':				
			for dic in range(len(BucketItems)):
			    if BucketItems[dic]['item'] == old:
			        del BucketItems[dic]['item']
			        BucketItems[dic]['item'] = item
			        return 1
		else:
			return 2	

		# defining method to delete an item from bucket			
	def deleteItem(self,item):
		for dic in range(len(BucketItems)):
			if BucketItems[dic]['item'] == item:
				del BucketItems[dic]
				result = 1
			else:
				result = 2

		return result     		