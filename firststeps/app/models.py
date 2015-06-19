from django.db.models import *

# Create your models here.

class firstdb(Model):
	name = CharField(max_length = 25, primary_key = True)
	def __str__(self):
		return str(self.name)
		