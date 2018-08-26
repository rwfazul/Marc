from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name='home'),




	path('teste', views.teste, name='teste'),

	path('form/', views.form, name='form')

]