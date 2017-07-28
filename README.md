
[![Build Status](https://travis-ci.org/cjmash/BucketList.svg?branch=develop)](https://travis-ci.org/cjmash/BucketList)     [![Coverage Status](https://coveralls.io/repos/github/cjmash/BucketList/badge.svg?branch=develop)](https://coveralls.io/github/cjmash/BucketList?branch=develop)    [![Code Health](https://landscape.io/github/cjmash/BucketList/develop/landscape.svg?style=flat)](https://landscape.io/github/cjmash/BucketList/develop)

# BucketList
This repository contains the following:
User interface for a bucketlist
Bucket List applications with flask

# Prerequisites

You will need python 3.6 or a later python version.

the requirements are in the requirements.txt

# installing
clone the repository 

FOR HTTPS
https://github.com/cjmash/BucketList.git

FOR SSH 

git@github.com:cjmash/BucketList.git

# Change Directory into the project folder

$ cd bucketlist

# Create a virtual environment with Python 3.6

$ virtualenv --python=python3.6 yourenvname

# Activate the virtual environment you have just created

$ source yourenvname/bin/activate

# Install the application's dependencies from requirements.txt to the virtual environment

$ (yourenvname) pip install -r requirements.txt

# Set up Unit Test Environment

run the following command to install nose unit testing environment:

$  (yourenvname) pip install nose

This will enable you to run sngle file tests like.

$ (yourenvname) nosetests -v

# Running the program

Run the program by typing the command in your terminal : 

$  (yourenvname) python run.py

you are now good to go
