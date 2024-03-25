from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
	#validators
	def start_with_s(value):
		if value[0].lower() != 's':
			raise serializers.ValidationError('Name must start with S !!')
	name = serializers.CharField(validators = [start_with_s])
	class Meta:
		model = Student
		fields = ['id','name','roll','city']





	#Object Level Validation is used for multiple fields 
	def validate(self, value):
		nm = value.get('name')
		ct = value.get('city')
		if nm.lower() == 'sagar' and ct.lower() != 'bochum':
			raise serializers.ValidationError('City must be bochum to be inserted ! Check the name in myapp.py')

		return data

	#Field Label Validation
	def validate_roll(self, value):
		if value >=200:
			raise serializers.ValidationError('Seat Full !!')
		return value


