
from django.db import models
from datetime import datetime
# Create your models here.

#for Executive Members List Page
class ExecutiveMembers(models.Model):
	srn = models.IntegerField(null=True)
	images = models.ImageField(upload_to='static/executivememberslist/')
	name = models.CharField(max_length=50)
	description = models.TextField()
	position = models.CharField(max_length=50)

	def __str__(self):
		return str(self.srn) + ' ' + self.name

#for Main Photo Gallery
class PhotoGallery(models.Model):
	srn = models.IntegerField(null=True)
	name = models.CharField(blank=True,max_length=100)
	image = models.ImageField(upload_to='static/photogallery/')
	description = models.TextField(blank=True)

	def __str__(self):
		return str(self.srn) + ' ' + self.name		

#for ContactUs Page, Contact Details
class ContactUs(models.Model):
	#Model for saving Contact Details
	name = models.CharField(max_length=50)
	address = models.TextField()
	phone = models.CharField(max_length=15)
	email = models.EmailField(blank=True)

	def __str__(self):
		return self.name

#for Message Column in ContactUs Page
class Message(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	phone = models.CharField(max_length=15)
	message = models.TextField()

	def __str__(self):
		self.name + ' ' + self.email

#for HomePage updates Section
class Updates(models.Model):
	description = models.TextField()
	datetime = models.DateTimeField(default=datetime.now())

	def __str__(self):
		self.description + ' ' + str(self.datetime)
#for events page
class Event(models.Model):
	title = models.TextField()
	date = models.DateTimeField()
	description = models.TextField()
	venue = models.CharField(max_length=120,blank=True)
	image = models.ImageField(blank=True,upload_to='static/events')

	def __str__(self):
		return self.title + ' - ' + str(self.date)
		