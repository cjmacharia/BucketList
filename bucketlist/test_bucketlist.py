mport unittest
from bucketlist import Bucketlist

class Buckettest(unittest.TestCase):
    """
       Class performing unit testing for class BucketList
    """

        # Defining setUp() method that runs prior to each test.
    def setUp(self):
        self.buckets=Bucketlist()