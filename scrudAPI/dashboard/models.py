from django.db import models

# Create your models here.

class Production(models.Model):
	item = models.CharField(max_length = 100)
	year = models.CharField(max_length = 20)
	data = models.IntegerField(default = 0)
	class Meta:
		db_table = 'production'
		unique_together = ("item","year")
