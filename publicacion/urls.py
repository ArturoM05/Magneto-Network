from django.urls import path
from .views import home_algorithm

urlpatterns = [
			   path('',home_algorithm , name="home1"),
			   ]