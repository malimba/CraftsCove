from django.db import models
from django.contrib.auth.models import AbstractBaseUser

#security
from werkzeug.security import generate_password_hash

# Create your models here.

#create user model
class User(AbstractBaseUser):
    #cust user model
    id = models.AutoField(primary_key=True, blank=False, null=False)
    #fullname - combination of firstname and lastname
    fullname = models.CharField(max_length=255, blank=False, null=False)
    username = models.CharField(max_length=30, blank=False, null=False)
    emailAddr = models.EmailField(max_length=255, unique=True, blank=False, null=False)  # require
    GENDER_CHOICES = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE')
    )
    gender = models.CharField(max_length=6, blank=False, null=False)
    password = models.CharField(max_length=500, blank=False, null=False)


    def hash_password(self):
        # create password salt
        hash = generate_password_hash(self.password, method='pbkdf2:sha256', salt_length=8)
        self.password = hash