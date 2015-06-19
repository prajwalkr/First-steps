from django.http import HttpResponse
from django.shortcuts import render
from forms import userform
from .models import firstdb

# Create your views here.

def process_form(request):
	if request.method == 'POST':
		form = userform(request.POST)
		if form.is_valid() == True:
			name = form.cleaned_data.get('name')
			p = firstdb(name)
			p.save()
			return render(request, 'user_submit.html', {'name':p.name})
		return HttpResponse("Invalid submission")
	elif request.method == 'GET':
		form = userform()
		return render(request, 'user_form.html', {'form':form})
