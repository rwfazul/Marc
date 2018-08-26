from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name='home'),
<<<<<<< HEAD




	path('teste', views.teste, name='teste')
=======
	path('form/', views.form, name='form')
>>>>>>> d1d557cfaf2278d4c6fba550fb876708fac88df1
]