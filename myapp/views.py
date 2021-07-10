from django.shortcuts import render,redirect
from . models import * 
from django.conf import settings
from django.core.mail import send_mail
import random

# Create your views here.
def index(request):
	return render(request,'index.html')

def music(request):
	return render(request,'music.html')

def about(request):
	return render(request,'about.html')

def blog(request):
	return render(request,'blog.html')
def contact(request):
	if request.method=="POST":
		Contact.objects.create(
				name=request.POST['name'],
				email=request.POST['email'],
				mobile=request.POST['mobile'],
				subject=request.POST['subject'],
				message=request.POST['message'],
			)
	
		print(request.POST['name']),
		print(request.POST['email']),
		print(request.POST['mobile']),
		print(request.POST['subject']),
		print(request.POST['message']),
		msg="Contact Saved SuccessFully"
		return render(request,'contact.html',{'msg':msg})	
	else:	
	
		return render(request,'contact.html')

def login(request):
	if request.method=="POST":
		if request.POST['action']=="forgot_password":
			
			return render(request,'enter_email.html')
		elif request.POST['action']=="login":
			try:
				user=User.objects.get(
					email=request.POST['email'],
					password=request.POST['password'],
					)
				if user.usertype=="user":
					wishlists=Wishlist.objects.filter(user=user)
					carts=Cart.objects.filter(user=user)
					request.session['fname']=user.fname
					request.session['email']=user.email
					request.session['image']=user.image.url
					request.session['wishlist_count']=len(wishlists)
					request.session['cart_count']=len(carts)
					return render(request,'index.html')
				elif user.usertype=="seller":
					request.session['fname']=user.fname
					request.session['email']=user.email
					request.session['image']=user.image.url
					print(request.session.session_key)
					return render(request,'seller_index.html')		
			except:
				msg="Email or Password Is Incorrect"
				return render(request,'login.html',{'msg':msg})
	
			
		else:
			pass 
	return render(request,'login.html')

def Register(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			msg="Email Already Registered"
			return render(request,'register.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					email=request.POST['email'],
					mobile=request.POST['mobile'],
					gender=request.POST['gender'],
					address=request.POST['address'],
					password=request.POST['password'],
					cpassword=request.POST['cpassword'],
					image=request.FILES['image'],
					usertype=request.POST['usertype']

				)
				
				subject = 'OTP FOR REGISTRATION'
				otp=random.randint(1000,9999)
				message = 'HELLO User, Your OTP For SuccessFully Registration Is : '+str(otp)
				email_from = settings.EMAIL_HOST_USER
				recipient_list = [request.POST['email'],]
				send_mail( subject, message, email_from, recipient_list )


				msg="Register SuccessFully"
				return render(request,'otp.html',{'otp':otp,'email':request.POST['email']})
			else:
				msg="Password & Confrim Password Does Not Matched"
				return render(request,'register.html',{'msg':msg})
	else:
		return render(request,'register.html')

def enter_otp(request):
	otp1=request.POST['otp1']
	otp2=request.POST['otp2']
	email=request.POST['email']

	if otp1==otp2:
		user=User.objects.get(email=email)
		user.status="active"
		user.save()
		msg="User Verified SuccessFully"
		return render(request,'login.html',{'msg':msg})
	else:
		msg="Invalid OTP"
		return render(request,'otp.html',{'otp':otp1,'email':email,'msg':msg})

def enter_email(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			subject = 'OTP FOR Forgot password '
			otp=random.randint(1000,9999)
			message = 'HELLO User, Your OTP For Forgot Password Is : '+str(otp)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [request.POST['email'],]
			send_mail( subject, message, email_from, recipient_list )
			return render(request,'forgot_enter_otp.html',{'otp':otp,'email':request.POST['email']})
		except:
			msg="Email Does Not Exists In The System"
			return render(request,'enter_email.html',{'msg':msg})

def verify_forgot_otp(request):
	if request.method=='POST':
		otp1=request.POST['otp1']
		otp2=request.POST['otp2']
		email=request.POST['email']

		if otp1==otp2:
			return render(request,'new_password.html',{'email':email})
		else:
			msg="Entered OTP Is Invalid"
			return render(request,'forgot_enter_otp.html',{'otp':otp1,'email':email})


def forgot_password(request):
	print(request.POST['submit']),
	print(request.POST['email']),
	print(request.POST['password']),

	return render(request,'forgot_password.html'),


def update_password(request):
	if request.method=="POST":
		user=User.objects.get(email=request.POST['email'])


		if request.POST['npassword']==request.POST['cnpassword']:
			user.password=request.POST['npassword']	
			user.cPassword=request.POST['cnpassword']
			user.save()
			return render(request,'login.html')
		else:
			msg="New password & Confrim new password Does Not Matched"
			return render(request,'forgot_enter_otp.html',{'otp':otp1,'email':request.POST ['email'],'msg':msg})

def logout(request):
	try:
		del request.session['email'],
		del request.session['fname'],
		del request.session['image'],
		return render(request,'index.html')
	except:
		pass 

def change_password(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])

		if user.password==request.POST['old_password']:
			if request.POST['npassword']==request.POST['cnpassword']:
				user.password=request.POST['npassword']
				user.password=request.POST['npassword']
				user.save()
				return redirect('logout')
			else:
				msg="New Password & Confrim New Password Does Not Matched"
				return render(request,'change_password.html',{'msg':msg})
		else:
			msg="Old password Is Incorrect"	
			return render(request,'change_password.html',{'msg':msg})	

	else:
		return render(request,'change_password.html')

def seller_change_password(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])

		if user.password==request.POST['old_password']:
			if request.POST['npassword']==request.POST['cnpassword']:
				user.password=request.POST['npassword']
				user.password=request.POST['npassword']
				user.save()
				return redirect('logout')
			else:
				msg="New Password & Confrim New Password Does Not Matched"
				return render(request,'seller_change_password.html',{'msg':msg})
		else:
			msg="Old password Is Incorrect"	
			return render(request,'seller_change_password.html',{'msg':msg})	

	else:
		return render(request,'seller_change_password.html')




def edit_profile(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=='POST':
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.mobile=request.POST['mobile']
		user.address=request.POST['address']
		user.gender=request.POST['gender']
		try:
			user.image=request.FILES['image']
			user.save()
			user=User.objects.get(email=request.session['email'])
			msg="Edit profile Saved SuccessFully"
			request.session['image']=user.image.url
			return render(request,'edit_profile.html',{'user':user,'msg':msg})
		except:
			user.save()
			user=User.objects.get(email=request.session['email'])
			msg="Edit profile Saved SuccessFully"
			return render(request,'edit_profile.html',{'user':user,'msg':msg})

	else:
		return render(request,'edit_profile.html',{'user':user})

def seller_edit_profile(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=='POST':
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.mobile=request.POST['mobile']
		user.address=request.POST['address']
		user.gender=request.POST['gender']
		try:
			user.image=request.FILES['image']
			user.save()
			user=User.objects.get(email=request.session['email'])
			msg="Edit profile Saved SuccessFully"
			request.session['image']=user.image.url
			return render(request,'seller_edit_profile.html',{'user':user,'msg':msg})
		except:
			user.save()
			user=User.objects.get(email=request.session['email'])
			msg="Edit profile Saved SuccessFully"
			return render(request,'seller_edit_profile.html',{'user':user,'msg':msg})

	else:
		return render(request,'seller_edit_profile.html',{'user':user})

def seller_add_product(request):
	if request.method=="POST":
		seller=User.objects.get(email=request.session['email'])
		Product.objects.create(
			seller=seller,
			Product_brand=request.POST['product_brand'],
			Product_model=request.POST['product_model'],
			Product_price=request.POST['product_price'],
			Product_desc=request.POST['product_desc'],
			Product_image=request.FILES['product_image'],
			)
		msg="Product Added SuccessFully"
		return render(request,'seller_add_product.html',{'msg':msg})
	else:
		return render(request,'seller_add_product.html')

def seller_view_product(request):
	seller=User.objects.get(email=request.session['email'])
	Products=Product.objects.filter(seller=seller)
	return render(request,'seller_view_product.html',{'Products':Products})

def seller_product_detail(request,pk):
	Products=Product.objects.get(pk=pk)
	return render(request,'seller_product_detail.html',{'Products':Products})

def seller_edit_product(request,pk):
	Products=Product.objects.get(pk=pk)
	if request.method=="POST":
	
		Products.Product_model=request.POST['Product_model']
		Products.Product_price=request.POST['Product_price']
		Products.Product_desc=request.POST['Product_desc']

		try:
			Products.Product_image=request.FILES['Product_image']
			Products.save()
			return redirect('seller_view_product')
		except:
			Products.save()
			return redirect('seller_view_product')
	else:
		return render(request,'seller_edit_product.html',{'Products':Products})

def seller_delete_product(request,pk):
	Products=Product.objects.get(pk=pk)
	Products.delete()
	return redirect('seller_view_product')

def user_view_product(request,pb):
	if pb=="all":
		Products=Product.objects.all()
		return render(request,'user_view_product.html',{'Products':Products})
	else:
		Products=Product.objects.filter(Product_brand=pb)
		return render(request,'user_view_product.html',{'Products':Products})


def mywishlist(request):
	u=User.objects.get(email=request.session['email'])
	wishlist=Wishlist.objects.filter(user=u)
	wishlists=Wishlist.objects.filter(user=u)
	request.session['wishlist_count']=len(wishlists)
	return render(request,'mywishlist.html',{'wishlist':wishlist})

def user_product_detail(request,pid):
	flag=False
	flag1=False
	user=User.objects.get(email=request.session['email'])
	print(user)
	Products=Product.objects.get(pk=pid)
	print(Products)
	try:		
		Wishlist.objects.get(user=user,product=Products)
		flag=True 
	except Exception as e:
		print("Exception Call : ",e)
		print(flag)
		pass

	try:

		user=User.objects.get(email=request.session['email'])
		print(user)
		Products=Product.objects.get(pk=pid)
		print(Products)
		Cart.objects.get(user=user,product=Products)
		fleg1=True

	except Exception as e:
		print("Exception Call : ",e)
		print(flag1)
		pass
	
	return render(request,'user_product_detail.html',{'Products':Products,'flag':flag,'flag1':flag1})


def add_to_wishlist(request,pk):
	Products=Product.objects.get(pk=pk)
	u=User.objects.get(email=request.session['email'])
	Wishlist.objects.create(user=u,product=Products)
	return redirect('mywishlist')

def remove_from_wishlist(request,pk):
	user=User.objects.get(email=request.session['email'])
	print(user)
	Products=Product.objects.get(pk=pk)
	print(Products)
	wishlist=Wishlist.objects.get(user=user,product=Products)
	wishlist.delete()
	return redirect('mywishlist')

def mycart(request):
	net_price=0
	user=User.objects.get(email=request.session['email'])
	carts=Cart.objects.filter(user=user)
	
	for i in carts:
		net_price=net_price+int(i.total_price)

	request.session['cart_count']=len(carts)
	return render(request,'mycart.html',{'carts':carts,'net_price':net_price})


def add_to_cart(request,pk):
	Products=Product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	Cart.objects.create(
		user=user,
		product=Products,
		price=Products.Product_price,
		total_price=Products.Product_price
	)
	return redirect('mycart')

def remove_cart(request,pk):
	Products=Product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	cart.Cart.objects.get(user=user,product=Product)
	cart.delete()
	return redirect('mycart') 

def change_qty(request):
	cart=Cart.objects.get(pk=request.POST['pk'])
	qty=request.POST['qty']
	cart.qty=qty
	cart.total_price=int(qty)*int(cart.price)
	cart.save()

	print(cart)
	print(qty)
	print(type(cart))
	print(type(qty)) 


	return redirect('mycart')


	

	 


















def single(request):
	return render(request,'single.html')


def seller_index(request):
	return render(request,'seller_index.html')


def store(request):
	Products=Product.objects.all()
	return render(request,'store.html',{'Products':Products})

	