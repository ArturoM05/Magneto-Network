from django.urls import path
from .views import *


app_name = 'grupo_interes'

urlpatterns = [
			   path('show_new/', show_new_grupo_interes, name="show_new_grupo_interes"),
               path('create/', create_grupo_interes, name="create_grupo_interes"),
               path('join/',join_grupo_interes, name='join_grupo_interes'),
               path('feed/', grupo_interes_feed, name="grupo_interes_feed"),
                path('profile/<str:id>/', grupo_interes_profile, name="grupo_interes_profile"),
			   ]