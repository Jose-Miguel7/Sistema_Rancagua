from django.urls import path

from . import views



urlpatterns = [
	path('', views.Formulario1.as_view(), name = 'formulario1-1'),	
]