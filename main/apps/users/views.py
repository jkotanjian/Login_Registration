from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
	if 'user_id' not in request.session:
		return redirect('users:new')

	context = {
		"users": User.objects.get(id=request.session['user_id']),
	}
	return render(request, 'users/index.html', context)

def new(request):
	return render(request, 'users/new.html')

def create(request):
	errors = User.objects.validate(request.POST)
	print(errors)
	if errors:
		for error in errors:
			messages.error(request, error)
		print(error)	
		return redirect('users:new')
	
	user_id = User.objects.easy_create(request.POST)
	request.session['user_id'] = user_id
	return redirect ('users:index')	


def login(request):
	valid, result = User.objects.login(request.POST)
	if not valid:
		messages.error(request, result)
		return redirect('users:new')
	
	request.session['user_id'] = result	
	return redirect('users:index')


def logout(request):
	request.session.clear()
	return redirect('users:new')	