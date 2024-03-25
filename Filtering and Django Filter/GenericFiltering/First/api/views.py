from django.shortcuts import render
from .models import StudentAPI
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class StudentList(ListAPIView):

	#display all students passed by both sir and madam
	queryset = StudentAPI.objects.all()
	serializer_class = StudentSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['city','passby']
	'''Filter can be done in two ways'''
	
		

