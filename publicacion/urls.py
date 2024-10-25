from django.urls import path
from .views import home_algorithm, like_post

urlpatterns = [
			   path('',home_algorithm , name="home1"),
               path('like_post/',like_post, name='like_post'),
			   ]