from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView

''' We can do both Global and perview setting. Check in Settings.py for Global setting 
For Global Setting, We don't need to writeanything'''
class StudentList(ListAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

