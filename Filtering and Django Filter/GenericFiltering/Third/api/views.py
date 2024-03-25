from django.shortcuts import render
from .models import StudentAPI
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter



class StudentList(ListAPIView):

	#display all students passed by both sir and madam
	queryset = StudentAPI.objects.all()
	serializer_class = StudentSerializer
	filter_backends=[OrderingFilter]
	ordering_fields = ['name','city']

	

