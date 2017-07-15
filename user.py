from flask import Flask, session, render_template, request, redirect, g, url_for
import re
users = {}
class User():


 	# Initializing  class instance variables
    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

        #defining method to create account
    def register(self,email, name,password, cpassword):       
            
        if  name!='' and email!='' and password!='':

            if email not in users.keys():

                if password==cpassword:
                    regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
                    result = email
                    if re.search(regex, result):
                        match = re.search(regex, result)
                        users[email] = {
                        'name': name,
                        'email': email,
                        'pass': password,
                        }
                        return  1
                    else:
                        return 2 
                else:
                    return 3
            else:
                return 4
        else:
            return 5

        # defining method to validate user             
    def login(self, email, password):
        if email!='' and password!='':
            if email in users.keys():
                result=users[email]
                pword=result['pass']
                if pword==password:
                    return 1
                else:
                    return 2
            else:
                return 3
        else:
            return 4  

        #function to get a user's name            
    def get_user_name(self, email):
        if email in users.keys():
            result =users[email]
            return result['name']
        else:
            return False

        #function to get a user's email
    def get_user_email(self, email):
        if email in users.keys():
            result=users[email]
            return result['email']
        else:
            return False