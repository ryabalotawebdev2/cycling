from django.db import models


class List(models.Model):
    pass


class Item(models.Model):
	#1st input
	email= models.TextField(default='')
	fullname= models.TextField(default='')

    #2nd
	name= models.TextField(default='')
	kilometer= models.TextField(default='')
	list = models.ForeignKey(List, default=None, on_delete=models.PROTECT)
