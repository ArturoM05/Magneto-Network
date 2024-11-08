from django.urls import path
from .views import show_area_interes,add_area_interes


app_name = 'area_interes'

urlpatterns = [
			   path('show/', show_area_interes, name="show_area_interes"),
               path('add/', add_area_interes, name="add_area_interes"),
			   ]