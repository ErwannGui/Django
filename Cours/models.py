from django.db import models
from mongoengine import *

# Create your models here.

class User(Document):
    firstname = StringField(max_length=50)
    lastname = StringField(max_length=50)
    email = EmailField()
    password = StringField(max_length=20)

    def __str__(self):
        return self.id