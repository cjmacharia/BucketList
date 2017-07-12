import unittest
from bucketlist import Bucketlist

class Buckettest(unittest.TestCase):
    """
       Class performing unit testing for class BucketList
    """

        # Defining setUp() method that runs prior to each test.
    def setUp(self):
        self.buckets=Bucketlist()
        
        # defining method to test for Creating a bucket list
    def test_for_creating_a_bucketlist(self):
        self.buckets.Bucketlists = {}
        output = self.buckets.create('Bucketlist 1', 'Fashion','owner@gmail.com')
        self.assertEqual(1,output, "Bucket successfully created")
        
        # defining method to test for adding a bucket list with an empty title
    def test_if_title_empty(self):
        output=self.buckets.create('','this is my bucketlist by the age of 29','owner')
        self.assertEqual(3,output, "please fill all fields")

        # defining method to test for adding a bucket list with an empty description
    def test_if_description_empty(self):
        output=self.buckets.create('By 28','','anto@gmail.com')
        self.assertEqual(3,output, "please fill the description")

        # defining method to test for adding a bucket list That already exists
    def tests_if_bucket_exists(self):
        self.buckets.create('By28','my dreams by 28','anto@gmail.com')  
        output=self.buckets.create('By28', 'my goals','anto@gmail.com')
        self.assertEqual(2,output, "That bucket already exists!") 

     # defining method to test for deleting a bucketlist
    def tests_bucket_delete(self):
        self.buckets.Bucketlists={}  
        self.buckets.create('By28', 'my goals','anto@gmail.com')
        output=self.buckets.delete('By28')
        self.assertEqual(1,output, "Succesfully deleted!")        