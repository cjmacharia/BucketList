mport unittestimport unittest
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
        