from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
	is_trainer = models.BooleanField(default=False)
	is_trainee = models.BooleanField(default=False)

class Trainee(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

	def __str__(self):
		return self.user.username