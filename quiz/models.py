# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	profession= models.CharField(max_length=100)
	bio = models.TextField()
	image = models.ImageField(upload_to='media')
	date_created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return reverse('profile-detail', args=[A('pk')])

class Feed(models.Model):	
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	text = models.TextField(max_length=500)
	time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.text

class BookmarkBase(models.Model):
    class Meta:
        abstract = True
 
    user = models.ForeignKey(User, verbose_name="User")
 
    def __str__(self):
        return self.user.username

class BookmarkFeed(BookmarkBase):
    class Meta:
        db_table = "bookmark_feed"
 
    obj = models.ForeignKey(Feed, verbose_name="Feed")