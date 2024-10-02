from django.urls import path
from .views import registrar_usuario, login_usuario, home_algorithm

urlpatterns = [
    path('registro/', registrar_usuario, name='registro'),
    path('login/', login_usuario, name='login'),
    path('home/',home_algorithm, name= 'home')
]