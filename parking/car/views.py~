# -*- coding: utf-8 -*-
from django.shortcuts import render , render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from car.models import  parking, User
from car.forms import userform  , parkingform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  login, logout, authenticate 
from geoposition import Geoposition
import json
from django.core.serializers.json import DjangoJSONEncoder


def register(request):
	context = RequestContext(request)
	registred = False
	if request.method =='POST' :
		user_form =userform(data= request.POST)	
		if user_form.is_valid() :
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registred = True 
			return HttpResponseRedirect('/car/merci/')
		else :
			print user_form.errors
	else:
		user_form= userform()
		
	return render_to_response('car/register.html',{'user_form': user_form, 'registred': registred}, context)




def merci(request):
	context=RequestContext(request)
	return render_to_response('car/merci.html',{},context)




def accueil(request):
	context = RequestContext(request)
	return render_to_response('car/accueil.html',{},context)



def user_login(request):
	context= RequestContext(request)
	if request.method == 'POST':	
		mail= request.POST['email']
		userpass = request.POST['password']
		userf= User.objects.get(email = mail)
		usern= userf.username
		user = authenticate(username=usern,password=userpass)
		if user :
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('/car/')
			else:
				return HttpResponse("votre compte est désactivé")
		else:
			print "Invalid login details: {0}, {1}".format(mail,userpass)	
			return HttpResponse("entrées invalides.")
	else:
		return render_to_response('car/login.html', {}, context)



@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/car/')



@login_required
def add_parking(request):
	context=RequestContext(request)
	if request.user is not None:
    		userf = request.user	
	if request.method == 'POST':
		form= parkingform(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.proprietaire=userf
			if 'site' in request.FILES :
				form.site=request.FILES['site']
			form.save()
			return accueil(request)
		else:
			print form.errors
	else:
		form = parkingform()
	return render_to_response('car/add_parking.html',{'form' : form }, context)


