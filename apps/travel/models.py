from __future__ import unicode_literals

from django.db import models

#import models from User
from ..formv.models import User

# Create your models here.


class TravelManager(models.Manager):
	def validateTravel(self, post):
		pass

	def addTravel(self, post):
		pass



class Travel(models.Model):
	destination = models.CharField(max_length=100)
	description = models.CharField(max_length=255)
	planner = models.ForeignKey(User)
	datestart = models.DateTimeField()
	dateend = models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class JoinedTrip(models.Model):
	trip = models.ForeignKey(Travel)
	user = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)



"""

class BookManager(models.Manager):
	def validateform(self, post):
		errors = []
		if len(post['title']) == 0:
			errors.append("Book title must be filled")
		elif len(Book.objects.filter(title = post['title'])) > 0:
			errors.append("This book already exists")

		if len(post['review']) < 3:
			errors.append("Review field must not be blank")

		return errors

	def addbook(self, post, userid):
		authors = Author.objects.filter(name = post['authexist'])
		user = User.objects.get(id = userid)
		if authors != "custom":
			author = authors[0]
			book = Book.objects.create(title=post['title'], author=author)
		elif authnew:
			author = Author.objects.create(name=authnew)
			book = Book.objects.create(title=post['title'], author=author)

		print "sucessfully created:"
		return book


	class Book(models.Model):
		title = models.CharField(max_length=45)
		author = models.ForeignKey(Author)
		created_at = models.DateTimeField(auto_now_add=True)
		updated_at = models.DateTimeField(auto_now=True)
		objects = BookManager()

	class Author(models.Model):
		name = models.CharField(max_length=45)	
		created_at = models.DateTimeField(auto_now_add=True)
		updated_at = models.DateTimeField(auto_now=True)

"""