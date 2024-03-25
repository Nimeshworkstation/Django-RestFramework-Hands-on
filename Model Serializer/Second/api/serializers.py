from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
	#We set a validation that name is only read only . It can't be deleted or updated from database
	name = serializers.CharField(read_only = True)
	class Meta:
		model = Student
		fields = [ 'name', 'roll', 'city']
		#To put read only on many fileds
		#read_only_fields = ['name', 'roll']
		#We can add more many things on fields this way also. Here we did read only . we can use this one or the first one.
		#extra_kwargs = {'name':{'read_only':True}}


#we dont need create and update method to update and save the data as in normal serializers. It is done automatically in model serializer
	'''

class StudentSerializer(serializers.Serializer):
	name = serializers.CharField(max_length = 100)
	roll =serializers.IntegerField()
	city =serializers.CharField(max_length = 100)


	def create(self, validated_data):
		return Student.objects.create(**validated_data)

	def update(self, instance, validated_data):
		print(instance.name)
		instance.name = validated_data.get('name',instance.name)
		print(instance.name)
		instance.roll= validated_data.get('roll',instance.roll)
		instance.city = validated_data.get('city',instance.city)
		instance.save()
		return instance'''