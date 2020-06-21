# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
	if request.user.is_anonymous():
		return redirect("/loginUser")
	return render(request,'home.html')



def loginUser(request):
	if request.method=="POST":
		username=request.POST.get("username")
		password=request.POST.get("password")
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			return render(request,'login.html')
	return render(request,'login.html')

def logoutUser(request):
	logout(request)
	return redirect("/loginUser")



def about(request):
	return render(request,'about.html')

def service(request):
	return render(request,'service.html')


def contact(request):
	if request.method== "POST":
		name=request.POST.get('name')
		email=request.POST.get('email')
		phone=request.POST.get('phone')
		Desc=request.POST.get('Desc')
		contact=Contact(name=name,email=email,phone=phone,Desc=Desc,date=datetime.today())
		contact.save()	
		messages.success(request, 'Your Details has been Saved!')	
	return render(request,'contact.html')



'''# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
def index(request):
	if request.user.is_anonymous():
		return redirect("/loginUser")
	return render(request,'index.html')

def loginUser(request):
	if request.method=="POST":
		username=request.POST.get("username")
		password=request.POST.get("password")
		user = authenticate(username=username, password=password)
		if user is not None:
			return redirect('/')
		else:
			return render(request,'login.html')
	return render(request,'login.html')

def logoutUser(request):
	return redirect("/loginUser")'''