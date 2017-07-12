from app import app
from user import User
from bucketlist import Bucketlist
from flask import Flask, session, render_template, request, redirect, g, url_for
import os

# Instantiating objects
newUser = User()
NewBucketlist=Bucketlist()

app.secret_key = os.urandom(24)

# defining sign-up page route
@app.route('/register/', methods=['GET', 'POST'])
def reg():
	if request.method== 'POST':
			name=request.form['name']
			email=request.form['email']
			password=request.form['password']
			cpassword=request.form['cpassword']
			result=newUser.register(email,name,password,cpassword)
			if result ==1:
				session['user']=name
				print("hello",session['user'])
				return render_template('login.html')
			elif result ==5:
				msg= ("please fill all the fields")
				return render_template ('register.html', data=msg)
			elif result ==3:
				msg= ("password mismatch")	
				return render_template ('register.html',data=msg)
			elif result==2:
				error="email must be a valid email"
				return render_template ('register.html', data=error)	
			elif result==4:
				error="email already exists"
				return render_template ('register.html', data=error)	
	else:
			return render_template ('register.html')	