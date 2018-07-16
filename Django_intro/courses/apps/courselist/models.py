from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        if len(postData['course_name'])<5:
            errors['course_name'] = 'Course name must be at least 5 characters'
        return errors

class DescriptionManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['course_desc'])<15:
            errors['course_desc'] = 'Course description must be at least 15 characters'
        return errors

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class Description(models.Model):
    contents = models.TextField(default = 'description of course goes here')
    course = models.OneToOneField(
        Course,
        on_delete=models.CASCADE,
        primary_key=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    course = models.ForeignKey(Course, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


