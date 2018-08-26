from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name='home'),

	path('importFromFile', views.importFromFile, name='importFromFile'),

	path('dashboard/', views.dashboard, name='dashboard'),
	path('charts-two/', views.charts_two, name='charts_two'),
	path('tables/', views.tables, name='tables'),
	path('fix/', views.fix, name='fix'),


	path('forms/', views.cadastroEmpresa, name='forms'),

	path('charts/<slug:prob_type>', views.charts, name='charts'),

]