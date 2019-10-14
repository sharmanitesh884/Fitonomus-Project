from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from fitonomus_app import templates


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
	if request.user.is_authenticated:
		if request.user.is_trainer:
			return render(request,'fitonomus_app/trainer_home.html')
		else:
			return render(request,'fitonomus_app/trainee_home.html')
	return render(request,'fitonomus_app/home.html')
