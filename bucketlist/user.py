from flask import Flask, session, render_template, request, redirect, g, url_for
import re

users = {}

class User():
	"""
    Class User allow users to create user accounts, delete user accounts, validate sign up, validate
    login process and to render feedback messages inform of a dictionary
    """

    

    # Initializing  class instance variables
    def __init__(self, name = None, email = None, password = None):
        self.name = name
        self.email = email
        self.password = password

        #defining method to create account
    def register(self,email, name,password, cpassword):          
        if  name!='':
        	if email!='':
        		if password!='':
		            if email not in users.keys():
		                if password == cpassword:
		                    regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
		                    result = email
		                    if re.search(regex, result):
		                        match = re.search(regex, result)
		                        users[email] = {
		                        'name': name,
		                        'email': email,
		                        'pass': password,
		                        }
		                        print(users)
		                        return  1
		                    else:
		                        return 2 
		                else:
		                    return 3
		            else:
		                return 4
		        else:
		    
		 	        return 5
 	        else:
 	        	return 6
    	else:
	    	return 7    