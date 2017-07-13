# BucketList
This repository contains the following:
User interface for a bucketlist
Bucket List applications with flask

# USER INTERFACE

Contains HTML/CSS templates for Bucket List front end application.

# The BucketList Application

Its developed in flask and its features include:

#A user can be able to register in the application.
#A user can Login to application.
#A logged in user can Create, Read, Update and Delete a BucketList.
#A logged in user, can to add, update, view or delete a Buckelist item (non-persistent data)


# Prerequisites

You will need python 2.6 or a later python version.

# Requirements
Flask==0.12.2

Jinja2==2.9.6

# Setup

we will start bt setting up
a python virtual environment

If you are on Linux, use the following commands in your terminal:

$ sudo pip install virtualenv
$ mkdir bucket_list
$ cd bucket_list
$ virtualenv venv

you can then Activate virtual environment

$ source /scripts/activate/

# Setting up Flask

run  the following command in your terminal while in the virtual env folder:

$ pip install Flask

Setting up Pylint for linting to ensure PEP8 style guides.

$ sudo apt-get install pylint

# Set up Unit Test Environment

run the following command to install nose unit testing environment:

$ pip install nose

This will enable you to run sngle file tests like.

$ nosetests test_User.py

# Running the program

Open the terminal and cd into the directory you extracted the project.
Run the program by typing the command in your terminal : 
python run.py

you are now good to go
