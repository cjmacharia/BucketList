import unittest
from user import User

class Usertest(unittest.TestCase):
    """
        Class performing unit testing for class User
    """

        # Defining setUp() method that runs prior to each test.
    def setUp(self):
        self.newUser=User()

    # defining method to test for creating user account
    def test_create_account(self):
        self.newUser.users = {}
        result = self.newUser.register( 'email@mail.com', 'name' ,'cj', 'cj')
        self.assertEqual(1,result, "User succesfully created")   
if __name__ == "__main__":
    unittest.main()        