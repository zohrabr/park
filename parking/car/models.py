# -*- coding: utf-8 -*-
from django.db import models
from geoposition.fields import GeopositionField
from django.contrib.auth.models import User


User._meta.get_field('email')._unique = True


class owner(User):
	#owner=models.OneToOneField(User)
	teleport=models.CharField(max_length = 20, blank=True)
	def __unicode__(self):
		return self.username

class parking(models.Model):
	namepark    =models.CharField(max_length = 128)
	proprietaire=models.ForeignKey(owner)
	nbrplace    =models.IntegerField(default=0) 
	place       =models.CharField(max_length=200)     # adresse
	position    =GeopositionField()
	telephone   = models.CharField(max_length = 15)
	site        = models.URLField(blank=True,max_length = 250)
	accept      = models.BooleanField(default=False)
	nbplacevide  =models.IntegerField(default=0) 
	def get_vide(self):
		return self.nbplacevide
	def modif_vide(self,nb):
		if (self.nbplacevide + nb) <= self.nbrplace :
			self.nbplacevide+=nb
		return self.nbplacevide
	def supprime(self):
		self.delete()
	
	def __unicode__(self):
		return self.namepark
class supressions(models.Model):
	name=models.CharField(max_length = 128)
	def __unicode__(self):
		return self.name






