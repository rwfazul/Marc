from django.shortcuts import render
from bson import json_util
from glob import iglob
import os.path
import json
import time
from datetime import datetime, timedelta
from django.http import JsonResponse
from bson.json_util import dumps

from bson.json_util import dumps

import pymongo
from pymongo import MongoClient


from .forms import EmpresaForm


client = MongoClient('localhost', 27017)
db = client['hackthon']
# Create your views here.

def home(request):
	return render(request, 'login.html')

def form(request):
	return render(request, 'app_templates/forms.html')

def dashboard(request):
	return render(request, 'app_templates/home.html')


def importFromFile(request):

	#iglob(os.path.expanduser('~/Tweets/*.txt'))
	for fname in iglob(os.path.expanduser('~/Tweets/*.txt')):
		with open(fname) as fin:
			tweet = json.load(fin)

			tweets = db.tweets
			tweets.insert_one(tweet).inserted_id

	return render(request, 'app_templates/home.html')





def cadastroEmpresa(request):
	if request.method == "POST":

		form = EmpresaForm(request.POST)

		if form.is_valid():

			print ("PRaga deu")


	else: 

		form = EmpresaForm()
	
	context = {
    	'form': form
	}

	return render(request, 'app_templates/forms.html', context)
    




def charts(request, prob_type):
	return render(request, 'app_templates/charts.html')

def charts_two(request):
	return render(request, 'app_templates/charts-two.html')

def charts_json(request, prob_type):
	data = db.tweets.find({"prob_type": prob_type},{"created_at":1, "user.location":1, "followers_count":1, "reply_count":1, "retweet_count":1, "favorite_count":1, "timestamp_ms":1})
	lista = []
	for d in data:
		lista.append(dumps(d))
	return JsonResponse({"data": lista})

def tables(request):
	return render(request, 'app_templates/tables.html')

def forms(request):
	return render(request, 'app_templates/forms.html')

def fix(request):
	return render(request, 'app_templates/fix.html')

