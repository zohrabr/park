# -*- coding: utf-8 -*-
from django.db import models
from geoposition.fields import GeopositionField
from django.contrib.auth.models import User


User._meta.get_field('email')._unique = True


choix=(
	('Oui','Oui'),
	('Non','Non'),
)
class parking(models.Model):
	namepark=models.CharField(max_length = 30)
	proprietaire=models.ForeignKey(User)
	nbrplace=models.IntegerField(default=0)
	place=models.CharField(max_length=200)
	position=GeopositionField()
	telephone = models.CharField(max_length = 15)
	site = models.URLField(blank=True,max_length = 250)
	accept = models.BooleanField(default=False)
	identifiant = models.CharField(max_length=30,primary_key=True)
	disponible=models.CharField(max_length=15, choices=choix,default='Oui')
	def __unicode__(self):
		return self.namepark

#parking._meta.get_field('identifiant')._unique = True



