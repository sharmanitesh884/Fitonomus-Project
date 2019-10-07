from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render,get_object_or_404
from django.db import transaction
from django.db.models import Count
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView,ListView,UpdateView

from ..decorator import trainee_required
from ..forms import TraineeSignUpForm
from ..models import User

class TraineeSignUpView(CreateView):
	model = User
	form_class = TraineeSignUpForm
	template_name = 'registration/signup_form.html'

	def form_valid(self,form):
		user = form.save()
		login(self.request,user)
		return redirect('trainee:home')

def home(request):
	return render(request,'trainee/home.html')