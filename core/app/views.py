from django.shortcuts import render, redirect, get_object_or_404

from glob import iglob
import os.path
import json

import pymongo
from pymongo import MongoClient

from app.models import *
from app.forms import *


client = MongoClient('localhost', 27017)
db = client['hackaton']
# Create your views here.


def home(request):
	return render(request, 'login.html')

def importFromFile	(request):

	for fname in iglob(os.path.expanduser('~/Tweets/*.txt')):
		with open(fname) as fin:
			tweet = json.load(fin)
			
			tweets = db.tweets
			tweets.insert_one(tweet).inserted_id

			'''for tweet in fin:
													print(tweet)'''

	return render(request, 'app_templates/home.html')

def form(request):
	return render(request, 'app_templates/forms.html')

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

def empresa(request, pk):

	try:
		empresa = Empresa.objects.get(id=pk)
	except Empresa.DoesNotExist:
		empresa = None

	if request.method == 'POST':
		form = EmpresaForm(request.POST)
		if form.is_valid():
			empresa = form.save(commit=False)
			empresa.save()
			return redirect('/')  # TODO: redirect to the created topic page
	else:
		form = EmpresaForm()
	return render(request, 'app_templates/empresa.html', {'empresa': empresa, 'form': form})

