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
			email = form.cleaned_data.get('email')
			ip = form.cleaned_data.get('ip')
			p = firstdb(name,email,ip)
			p.save()
			return render(request, 'user_submit.html', {'name':name,'email':email,'ip':ip})
		return HttpResponse("Invalid submission. Check one or more fields.")
	elif request.method == 'GET':
		form = userform()
		return render(request, 'user_form.html', {'form':form})
