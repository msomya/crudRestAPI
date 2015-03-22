#to store JSON

from rest_framework import serializers
from dashboard.models import Production

class productionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Production
		fields = ('id','item', 'year', 'data')
