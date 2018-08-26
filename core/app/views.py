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
	return render(request, 'app_templates/home.html')

<<<<<<< HEAD


def teste(request):

	#iglob(os.path.expanduser('~/Tweets/*.txt'))


	for fname in iglob(os.path.expanduser('~/Tweets/*.txt')):
		with open(fname) as fin:
			tweet = json.load(fin)
			
			tweets = db.tweets
			tweets.insert_one(tweet).inserted_id

			'''for tweet in fin:
													print(tweet)'''

	return render(request, 'app_templates/home.html')
=======
def form(request):
	return render(request, 'app_templates/forms.html')
>>>>>>> d1d557cfaf2278d4c6fba550fb876708fac88df1
