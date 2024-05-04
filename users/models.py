from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import BaseModel


class User(AbstractUser, BaseModel):
    email = models.EmailField('email address', unique=True)
    resume_link = models.FileField(upload_to='resumes/', null=True)
    is_enabled_job_creation = models.BooleanField(default=False)
    username = models.CharField(
        max_length=50, blank=True, null=True, unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', "username"]

    def __str__(self):
        return "{}".format(self.email)
