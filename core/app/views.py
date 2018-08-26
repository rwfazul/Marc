from django.shortcuts import render

from glob import iglob
import os.path
import json
import time
from datetime import datetime, timedelta

import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['hackaton']
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

def charts(request, prob_type):
	# last_days = datetime.today() - timedelta(days=7)
	# last_days = time.mktime(last_days.timetuple())

	data = db.tweets.find({"prob_type": prob_type},{"location":1})

	context = {
		"data": data
	}

	return render(request, 'app_templates/charts.html', context)

def all_probs(request):
	data = db.tweets.aggregate([
		{"$project": {"prob_type": 1}},
		{"$group":{"_id": "$prob_type", "count": {"$sum": 1}}}
		])

	context = {
		"data": data
	}

	return render(request, 'app_templates/charts.html', context)

def charts_two(request):
	return render(request, 'app_templates/charts-two.html')

def tables(request):
	return render(request, 'app_templates/tables.html')

def forms(request):
	return render(request, 'app_templates/forms.html')

def fix(request):
	return render(request, 'app_templates/fix.html')
