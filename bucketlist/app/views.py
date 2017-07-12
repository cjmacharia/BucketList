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

@app.route('/login/', methods=['GET', 'POST'])
def logins():
	if request.method == "POST":
		emailLogin=request.form['email']
		passLogin=request.form['password']
		loginResult =newUser.login(emailLogin,passLogin)
		if loginResult==1:
			name = newUser.get_user_name(emailLogin)
			email = newUser.get_user_email(emailLogin)
			print('done')
			session['user']=name
			session['email']=email
			print(session['email'])
			return render_template ('home.html', data=session)
		elif loginResult==2:
			error = "Password mismatch"
			return render_template ('login.html', data=error)	
		elif loginResult==3:
			error = "The user does not exist please register and try again"
			return render_template ('login.html', data=error)	
		elif loginResult==4:
			error="Please fill all the fields"
			return render_template ('register.html', data=error)	 	
		else:
			error = "Wrong credentials please try again"
			return render_template ('login.html',data=error) 
	else:
		return render_template('login.html')

		#defining the create bucketlist route
@app.route('/create/', methods=['GET', 'POST'])
def createBucketlist():
	if g.user:
		if request.method=="POST":
			post=request.form['post']
			describe =request.form['description']
			owner = session['email']
			result=NewBucketlist.create(post,describe,owner)
			if result==2:
				error ="that bucket title already exists"
				return render_template('create.html' , data=error)
			if result==3:

				error ="Please fill all the fields"
				return render_template('create.html' , data=error)
					
			if result !=2 and result!=3:
				data = NewBucketlist.Bucketlists
				return redirect('/myBuckets')		
			return render_template('mybucketlist.html')
		else:
			return render_template('create.html' )	
	else:
		return render_template('login.html' )	

@app.route('/myBuckets/', methods=['GET'])		
