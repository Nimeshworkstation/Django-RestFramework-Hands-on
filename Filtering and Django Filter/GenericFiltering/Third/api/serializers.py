from rest_framework import serializers
from .models import StudentAPI

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = StudentAPI
		fields = '__all__'