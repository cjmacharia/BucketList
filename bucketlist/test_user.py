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

        # defining method to test for creating user account with an empty passsword field
    def test_null_password(self):
        output=self.newUser.register('test@email.com','mash','','pass')
        self.assertEqual(5,output, "Please the password filed") 

        # defining method to test for created user's password is equal to confirm password 
    def test_cpassword_is_password(self):
        output=self.newUser.register('test@email.com', 'cj', 'pass', 'pss')    
        self.assertEqual(3,output, "password mismatch")    

        # defining method to test if login password is equal to register passsword
    def test_wrong_login_password(self):
        self.newUser.users = {}
        self.newUser.register( 'email@mail.com', 'cj','pass', 'pass')
        result = self.newUser.login('email@mail.com', 'pass123')
        self.assertEqual(2,result,"password mismatch") 

        # defining method to test if login email is equal to register email
    def test_wrong_login_email(self):
        self.newUser.users = {}
        self.newUser.register('cj', 'email@mail.com', 'pass', 'pass')
        result = self.newUser.login('cj@gmail.com', 'pass')
        self.assertEqual(3,result,"wrong email try again") 

        # defining method to test for null login email
    def test_login_null_email(self):
        result = self.newUser.login('', 'pass')
        self.assertEqual(5,result,"Please fill the email field")   

        # defining method to test for null login password
    def test_login_null_password(self):
        result = self.newUser.login('cj@gmail.com', '')
        self.assertEqual(4,result,"Please fill the password field")               
            
if __name__ == "__main__":
    unittest.main()        