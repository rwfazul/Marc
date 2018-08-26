from django.shortcuts import render

# Create your views here.


def home(request):
	return render(request, 'app_templates/home.html')

def form(request):
	return render(request, 'app_templates/forms.html')
