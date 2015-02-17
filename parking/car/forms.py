# -*- coding: utf-8 -*-
from car.models import parking
from django import forms
from django.contrib.auth.models import User



class userform(forms.ModelForm):
	 last_name =forms.CharField(help_text="nom")
	 first_name = forms.CharField(help_text="prénom")
	 username = forms.CharField(help_text="identité")
         email = forms.CharField(help_text=" Email")
         password = forms.CharField(widget=forms.PasswordInput(), help_text="Mot de passe")
	 class Meta:
		model = User
		fields=['last_name','first_name','username','password','email']



class parkingform(forms.ModelForm):
	namepark=forms.CharField(max_length = 30, help_text="nom du parking :")	
	nbrplace=forms.IntegerField( help_text="nombre de place :")
	place=forms.CharField(max_length=200, help_text="adresse :")
	site=forms.URLField(help_text="* site web du parking : ")
	telephone = forms.CharField(max_length = 15,help_text="téléphone")
	identifiant = forms.CharField(max_length=30 , help_text="identifiant du parking")
	class Meta:
		model = parking
		fields=['namepark','nbrplace','place','telephone','identifiant','site','position']





