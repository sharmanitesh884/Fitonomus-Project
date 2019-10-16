from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from fitonomus_app.models import User,Trainee,Trainer

class TrainerSignUpForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = User
		fields=('username','password1','password2')

	def save(self,commit=True):
		user = super().save(commit=False)
		user.is_trainer = True
		if commit:
			user.save()
		return user


class TraineeSignUpForm(UserCreationForm):

	class Meta(UserCreationForm):
		model = User
		fields=('username','password1','password2')

	@transaction.atomic
	def save(self):
		user = super().save(commit=False)
		user.is_trainee = True
		user.save()
		trainee = Trainee.objects.create(trainee=user)
		return user
