from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ['id','name','roll','city']


	#Field Label Validation

	def validate_roll(self, value):
		if value >=200:
			raise serializers.ValidationError('Seat Full !!')
		return value