from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name='home'),
<<<<<<< HEAD
	path('dashboard/', views.dashboard, name='dashboard'),
	path('charts/', views.charts, name='charts'),
	path('charts-two/', views.charts_two, name='charts_two'),
	path('tables/', views.tables, name='tables'),
	path('forms/', views.forms, name='forms'),
	path('fix/', views.fix, name='fix'),
]