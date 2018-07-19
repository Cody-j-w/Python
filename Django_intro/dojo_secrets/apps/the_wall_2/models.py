from __future__ import unicode_literals
from django.db import models
from django.db.models import Count
from django.utils.dateparse import parse_date
from datetime import datetime, date
import pytz
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]*$')

class UserManager(models.Manager):
    def register_validator(self,postData):
        errors = {}
        if len(postData['first_name'])<1:
            errors['first_name'] = 'A valid first name is required!'
        if len(postData['first_name'])>64:
            errors['first_long'] = 'Name must be below 64 characters!'
        if not postData['first_name'].isalpha():
            errors['first_alpha'] = 'Name cannot contain numbers or special characters!'
        if len(postData['last_name'])<1:
            errors['last_name'] = 'A valid last name is required!'
        if len(postData['last_name'])>64:
            errors['last_long'] = 'Name must be below 64 characters!'
        if not postData['last_name'].isalpha():
            errors['last_alpha'] = 'Name cannot contain numbers or special characters!'
        if len(postData['password'])<8:
            errors['password'] = 'Password must be at least 8 characters!'
        if len(postData['password'])>64:
            errors['passlength'] = 'Password must be below 64 characters!'
        if postData['password'] != postData['password_confirm']:
            errors['passmatch'] = 'Passwords must match!'
        if not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = 'A valid E-mail address is required!'
        if len(postData['email'])>64:
            errors['email_length'] = 'E-mail must be below 64 characters!'
        if User.objects.filter(email=postData['email']).exists():
            errors['email_registration'] = 'This E-mail already exists!'
        birthday = parse_date(postData['birthday'])
        if not postData['birthday']:
            errors['birthdate'] = 'a valid birthday is required!'     
        elif birthday > date.today():
            errors['birthday'] = "we're pretty sure you're not a time traveller. Birthday must be before today."
        if len(errors)==0:
            password_hash = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], password = password_hash, birthday = postData['birthday'])

        return errors
    def login_validator(self,postData):
        errors = {}
        if User.objects.filter(email=postData['email']).exists():
            user = User.objects.get(email=postData['email'])
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors['passmatch'] = 'E-mail and/or password is incorrect.'
        else:
            errors['mailmatch'] = 'E-mail and/or password is incorrect.'
        return errors

class MessageManager(models.Manager):
    def message_creator(self,postData):
        post = Message.objects.create(message = postData['message'], poster = User.objects.get(id=postData['user_id']))
    def message_deletor(self,postData):
        deleted = Message.objects.get(id=postData['message_id'])
        deleted.delete()
    def likes(self,postData):
        message = Message.objects.get(id=postData['message_id'])
        poster = User.objects.get(id=postData['user_id'])
        message.likes.add(poster)
    def pop_posts(self,postData):
        popular_posts = Message.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:10]
        popular_posts[0].num_likes


class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=255)
    birthday = models.DateTimeField(default = '')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Message(models.Model):
    message = models.TextField(default='')
    poster = models.ForeignKey(User, related_name='posts')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    likes = models.ManyToManyField(User, related_name='liked_messages')
    objects = MessageManager()

