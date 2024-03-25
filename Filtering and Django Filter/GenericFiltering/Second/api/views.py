from django.shortcuts import render
from .models import StudentAPI
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter



class StudentList(ListAPIView):

	#display all students passed by both sir and madam
	queryset = StudentAPI.objects.all()
	serializer_class = StudentSerializer
	filter_backends=[SearchFilter]
	
	search_fields = ['passby']
# type follwoing in url to search by passby. http://127.0.0.1:8000/student/?search=madam	
	
	#search_fields = ['^name']
	#search by first character. http://127.0.0.1:8000/student/?search=n
	
	#search_fields = ['=name']

