from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	mobile=models.CharField(max_length=100)
	subject=models.CharField(max_length=100)
	message=models.CharField(max_length=100)

	def __str__(self):
		return self.name


class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	mobile=models.CharField(max_length=100)
	gender=models.CharField(max_length=100)
	address=models.TextField()
	password=models.CharField(max_length=100)
	cpassword=models.CharField(max_length=100)
	status=models.CharField(max_length=100,default="inactive")
	image=models.ImageField(upload_to="image/",blank=True,null=True)
	usertype=models.CharField(max_length=100,default="user")

	def __str__(self):
		return self.fname+" . "+self.lname   +"  <----email---> "+self.email

class Product(models.Model):

	BRANDS=(

			('calvin klein','calvin klein'),
			('gucci','gucci'),
			('true religion','true religion'),
			('burberry prorsum','burberry prorsum'),
			('dolce&gabbana','dolce&gabbana'),
			('armani','armani'),
			('being human','being human'),

		)
	seller=models.ForeignKey(User,on_delete=models.CASCADE) 
	Product_brand=models.CharField(max_length=100,choices=BRANDS)
	Product_model=models.CharField(max_length=100)
	Product_price=models.IntegerField()
	Product_desc=models.TextField()
	Product_image=models.ImageField(upload_to='Product_image')

	def __str__(self):
		return self.seller.fname+" - "+self.Product_model+" --BRANDS--> "+self.Product_brand

class Wishlist(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.user.fname+" --BRANDS--> "+self.product.Product_brand

class Cart(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	date=models.DateTimeField(default=timezone.now)
	qty=models.IntegerField(default=1)
	price=models.IntegerField()
	total_price=models.IntegerField()

	def __str__(self):
		return self.user.fname+" --BRANDS--> "+self.product.Product_brand