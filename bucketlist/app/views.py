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

#defining route to get all buckets
@app.route('/myBuckets/', methods=['GET'])
def getBuckets():
	if g.user:
		result = NewBucketlist.get_bucket_lists()       
		return render_template('mybucketlist.html',datas=result)
	else:
		return render_template('login.html')		

#define route to delete a bucketlist
@app.route('/delete/<post>')
def delete(post):
	if g.user:
		print(post)
		print(NewBucketlist.get_bucket_lists())
		res=NewBucketlist.get_bucket_list(post)
		if (res):
			result=NewBucketlist.delete(post)
			if result==True:
				message="successfully deleted"
				print(message)
				return redirect('/myBuckets' )
			else:
				message="not deleted"
				print(message)
				return redirect('/myBuckets' )				
		else:
			message="not found"
			print(message)
			return render_template('create.html')
	else:
		return render_template('create.html')
	return render_template('login.html')

#defining route to get the post to edit
@app.route('/editBucketlist/<post>')
def editBucketlist(post):
	print(post)
	if g.user:
		res=NewBucketlist.get_bucket_list(post)
		if (res):
			return render_template('edit.html', data=res)	
		return redirect('/myBuckets' )
	else:
		return render_template('login.html')	

#defining route to edit a bucketlist
@app.route('/editBucket/', methods=['GET', 'POST'])
def editBucket():
	if g.user:
		if request.method=="POST":
			old=request.form['old']
			post=request.form['post']
			describe =request.form['description']
			owner = session['email']
			result=NewBucketlist.edit(old,post,describe,owner)
			if result==1:
				message="bucket successfully updated"
				result = NewBucketlist.get_bucket_lists()       
				return render_template('mybucketlist.html',datas=result)
			elif result==2:
				print("the bucketlist already exist")
				return redirect('/myBuckets' )	
			elif result==3:
				print("please fill all the fields")
				return redirect('/myBuckets' )
		
	else:
		return render_template('login.html')

#defining route to create aa item in a bucketlist
@app.route('/createitem/', methods=['GET', 'POST'])
def addItems():
	if g.user:
		if request.method=="POST":
			item =request.form['item']
			post =request.form['post']
			result=NewBucketlist.createItem(post,item)
			if result==1:
				BucketItems = NewBucketlist.getItems(post)
				result = NewBucketlist.get_bucket_lists()       
				return render_template('mybucketlist.html',datas=result,items=BucketItems)			
		else:
			return render_template('create.html' )
	return render_template('login.html' )	

#defining route to create aa item in a bucketlist
@app.route('/edititem/<item>', methods=['GET','POST'])
def editItem(item):
	if g.user:
		if request.method=="POST":
			item =request.form['item']
			post=request.form['post']
			old=request.form['old']
			result=NewBucketlist.itemEdit(item,old)
			if result==1:
				BucketItems = NewBucketlist.getItems(post)
				result = NewBucketlist.get_bucket_lists()       
				return render_template('mybucketlist.html',datas=result,items=BucketItems)
			elif result==2:
				print("No result")
				return redirect('/myBuckets/')
			else:
				return redirect('/myBuckets/')	
		else:
			BucketItems = NewBucketlist.getItems(post)
			for dic in BucketItems:
				result = NewBucketlist.get_bucket_lists()       
				return render_template('mybucketlist.html',datas=result,items=BucketItems)		
	else:
		return render_template('login.html' )

