from django.shortcuts import render

from glob import iglob
import os.path
import json

import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['hackaton']
# Create your views here.


def home(request):
	return render(request, 'login.html')

def dashboard(request):
	return render(request, 'app_templates/home.html')

def charts(request):
	return render(request, 'app_templates/charts.html')

def charts_two(request):
	return render(request, 'app_templates/charts-two.html')

def tables(request):
	return render(request, 'app_templates/tables.html')

def forms(request):
	return render(request, 'app_templates/forms.html')

def fix(request):
	return render(request, 'app_templates/fix.html')