from django.shortcuts import render
from .models import StudentAPI
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView

# Create your views here.

class StudentList(ListAPIView):

	#display all students passed by both sir and madam
	queryset = StudentAPI.objects.all()

	#display the students who has been passed by madam
	queryset = StudentAPI.objects.filter(passby='madam')
	
	#display the students who has been passed by sir
	queryset = StudentAPI.objects.filter(passby='sir')

	serializer_class = StudentSerializer

	#Display the students based on Sir or Madam Login
	def get_queryset(self):
		user = self.request.user

		#if sir logs in , he will see only data passed by him
		#if madam logs in , she will see only data passed by her
		return StudentAPI.objects.filter(passby=user)

		
		

