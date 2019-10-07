from django.urls import include,path
from .views import fitonomus_app,trainee,trainer

urlpatterns = [
	path('',fitonomus_app.home,name='home'),
	path('trainee/',include('fitonomus_app'),name='trainee'),
	path('trainer/',include('fitonomus_app'),name='trainer'),

]