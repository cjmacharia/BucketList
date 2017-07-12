# BucketList
This repository contains the following:
User interface for a bucketlist
Bucket List applications with flask

USER INTERFACE

Contains HTML/CSS templates for Bucket List front end application.

The BucketList Application

Its developed in flask and its features include:

A user can be able to register in the application.
A user can Login to application.
A logged in user can Create, Read, Update and Delete a BucketList.
A logged in user, can to add, update, view or delete a Buckelist item (non-persistent data)

Prerequisites

You need python 2.6 or a later version.

Requirements

Flask==0.12.2
Jinja2==2.9.6



SET Up

Setting up python virtual environment

If you are on Mac OS X or Linux, use the following command:

$ sudo pip install virtualenv
$ mkdir bucket_list
$ cd bucket_list
$ virtualenv venv
Activating virtual environment

$ source venv/bin/activate
Setting up Flask

Enter the following command to install Flask in the virtualenv:

$ pip install Flask
Setting up Pylint for linting to ensure PEP8 style guide requirements.

$ sudo apt-get install pylint
Setting up Unit Test Environment

Enter the following command to install nose unit testing environment:

$ pip install nose
Once installed, you can execute a single test file.

$ nosetests test_User.py
Running the program

Open the terminal and cd into the directory you extracted the project.
Run the program by typing the command : python run.py
