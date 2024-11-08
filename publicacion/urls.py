from django.urls import path
from .views import home_algorithm, like_post, user_profile

urlpatterns = [
			   path('',home_algorithm , name="home1"),
               path('like_post/',like_post, name='like_post'),
               path('perfil/<str:id>/',  user_profile, name='user_profile'),
			   ]