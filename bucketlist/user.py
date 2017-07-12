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