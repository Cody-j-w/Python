from __future__ import unicode_literals
from django.db import models
from django.utils.dateparse import parse_date
from datetime import date
import re
import bcrypt
import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]*$')

class UserManager(models.Manager):
    def register_validator(self,postData):
        errors = {}
        if len(postData['first_name'])<1:
            errors['first_name'] = 'A valid first name is required!'
        if not postData['first_name'].isalpha():
            errors['first_alpha'] = 'Name cannot contain numbers or special characters!'
        if len(postData['last_name'])<1:
            errors['last_name'] = 'A valid last name is required!'
        if not postData['last_name'].isalpha():
            errors['last_alpha'] = 'Name cannot contain numbers or special characters!'
        if len(postData['password'])<8:
            errors['password'] = 'Password must be at least 8 characters!'
        if postData['password'] != postData['password_confirm']:
            errors['passmatch'] = 'Passwords must match!'
        if not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = 'A valid E-mail address is required!'
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

class CommentManager(models.Manager):
    def comment_creator(self,postData):
        commentor = User.objects.get(id=postData['user_id'])
        message = Message.objects.get(id=postData['message_id'])
        print(commentor)
        print(message)
        comment = Comment.objects.create(comment = postData['comment'], parent_message= message, commenter = commentor)

class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=255)
    birthday = models.DateTimeField(default = date.today())
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Message(models.Model):
    message = models.TextField(default='')
    poster = models.ForeignKey(User, related_name='posts')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = MessageManager()

class Comment(models.Model):
    comment = models.TextField(default='')
    commenter = models.ForeignKey(User, related_name='comments', default='')
    parent_message = models.ForeignKey(Message, related_name='child_comments')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CommentManager()