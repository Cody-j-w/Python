from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]*$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name'])<1:
            errors['first_name'] = 'A valid first name is required!'
        if not postData['first_name'].isalpha():
            errors['first_alpha'] = 'Name cannot contain numbers or special characters!'
        if len(postData['last_name'])<1:
            errors['last_name'] = 'A valid last name is required!'
        if not postData['last_name'].isalpha():
            errors['last_alpha'] = 'Name cannot contain numbers or special characters!'
        if not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = 'A valid E-mail address is required!'
        if User.objects.filter(email=postData['email']).exists():
            errors['email_registration'] = 'This E-mail already exists!'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

    def __repr__(self):
        return '<User: {} | {} {} {}>'.format(self.id, self.first_name, self.last_name, self.email)

