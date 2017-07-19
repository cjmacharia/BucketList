import unittest
from bucketlist import Bucketlist

class Buckettest(unittest.TestCase):
    """
       Class performing unit testing for class BucketList
    """

        # Defining setUp() method that runs prior to each test.
    def setUp(self):
        self.buckets = Bucketlist()
        
        # defining method to test for Creating a bucket list
    def test_for_creating_a_bucketlist(self):
        self.buckets.Bucketlists = {}
        output = self.buckets.create('Bucketlist 1', 'Fashion','owner@gmail.com')
        self.assertEqual(1,output, "Bucket successfully created")
        
        # defining method to test for adding a bucket list with an empty title
    def test_if_title_empty(self):
        output = self.buckets.create('','this is my bucketlist by the age of 29','owner')
        self.assertEqual(3,output, "please fill all fields")

        # defining method to test for adding a bucket list with an empty description
    def test_if_description_empty(self):
        output = self.buckets.create('By 28','','anto@gmail.com')
        self.assertEqual(3,output, "please fill the description")
        # defining method to test for adding a bucket list That already exists
    def tests_if_bucket_exists(self):
        self.buckets.create('By28','my dreams by 28','anto@gmail.com')  
        output = self.buckets.create('By28', 'my goals','anto@gmail.com')
        self.assertEqual(2,output, "That bucket already exists!") 

        # defining method to test for deleting a bucketlist
    def tests_delete_bucket(self):
        self.buckets.Bucketlists = {}  
        self.buckets.create('By28', 'my goals','anto@gmail.com')
        output = self.buckets.delete('By28')
        self.assertEqual(1,output, "Succesfully deleted!")

        # defining method to test for deleting a bucketlist That doesnot exist
    def tests_delete_NonExistant_bucketlist(self):
        self.buckets.Bucketlists = {}  
        self.buckets.create('By28', 'my goals','anto@gmail.com')
        output = self.buckets.delete('Bucket1')
        self.assertEqual(2,output, "You can not delete a bucket thay does not exist")    


        # defining method to test for editing a bucketlist
    def tests_edit_bucket(self):
        self.buckets.Bucketlists = {} 
        self.buckets.create('By28', 'my goals','anto@gmail.com')
        output = self.buckets.edit('By28','by30','vlogger','anto@gmail.com')
        self.assertEqual(1,output,"bucket successfully edited")

        # defining method to test for editing a bucketlist and leaving the title null
    def tests_edit_null_title(self):
        self.buckets.Bucketlists = {} 
        self.buckets.create('By28', 'my goals','anto@gmail.com')
        output = self.buckets.edit('By28','','vlogger','anto@gmail.com')
        self.assertEqual(3,output,"Please fill the title field")

        # defining method to test for editing a bucketlist and leaving the Description null
    def tests_edit_null_description(self):
        self.buckets.Bucketlists = {} 
        self.buckets.create('By28', 'my goals','anto@gmail.com')
        output = self.buckets.edit('By28','vlogger','','anto@gmail.com')
        self.assertEqual(2,output,"Please fill the description field")


        #defining method to test adding an item in a bucketlist
    def tests_Add_item(self):
        self.buckets.BucketItems = []
        output = self.buckets.createItem('Fashion', 'By20')
        self.assertEqual(1,output,"Item successfully added")

    def tests_addEmpty_item(self):
        self.buckets.BucketItems = []
        output = self.buckets.createItem('post', '')
        self.assertEqual(2,output,"Cannot add an empty item ") 

        #defining method to test deleting an item that doesn't exist in a bucketlist
    def tests_delete_null_item(self):
        self.buckets.BucketItems = []
        self.buckets.createItem('Fashion', 'By20')
        output = self.buckets.deleteItem('fish')
        self.assertEqual(2,output,"Cannot Delete an item that does not exist") 

        #defining method to test deleting an  existing item
    def tests_delete_items(self):
        self.buckets.BucketItems = []
        item =self.buckets.createItem('Fashion','By20')
        output = self.buckets.deleteItem(item)
        self.assertEqual(2,output,"Item successfully deleted") 

        #defining method to test editing an  existing item
    def tests_edit_item(self):
        self.buckets.BucketItems = []
        self.buckets.createItem('golf', 'By30')
        output = self.buckets.itemEdit('by40','By30')
        self.assertEqual(1,output,"Item successfully edited")

      #defining method to test editing an empty item field
    def tests_edit_null_item(self):
        self.buckets.BucketItems = []
        self.buckets.createItem('golf', 'By30')
        output = self.buckets.itemEdit('','By30')
        self.assertEqual(2,output,"The item can not be empty")    



if __name__ == "__main__":
    unittest.main()        