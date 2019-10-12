"""Fitonomus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from fitonomus_app.views import fitonomus_app,trainer,trainee
# from fitonomus_app.templates.fitonomus_app import trainer,trainee
# from fitonomus_app.templates.fitonomus_app.trainee import home

urlpatterns = [
    path('',fitonomus_app.home,name='home'),
    path('admin/',admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/signup/',fitonomus_app.SignUpView.as_view(),name='signup'),
    path('accounts/signup/trainer/',trainer.TrainerSignUpView.as_view(),name='trainer_signup'),
    path('accounts/signup/trainee/',trainee.TraineeSignUpView.as_view(),name='trainee_signup'),
    #path('trainee/',trainee.home,name='trainee'),
    #path('trainer/',trainer.home,name="trainer"),
]
