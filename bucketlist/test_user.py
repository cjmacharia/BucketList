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

     # defining method to test for creating user account with an empty name
    def test_register_null_name(self):
        output=self.newUser.register('test@email.com','','pass','pass')
        self.assertEqual(7,output, "Please fill your name")

        # defining method to test for creating user account with an empty email
    def test_register_null_email(self):
        output=self.newUser.register('','name','pass','pass')
        self.assertEqual(6,output, "Email is Empty ")     
            
if __name__ == "__main__":
    unittest.main()        