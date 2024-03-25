from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView
from .MyPagination import MyCursorPagination

''' This is PerView , We can see pagination 
in browsable api as well as typing in url for ex.
http://127.0.0.1:8000/student/?limit=6  to display a page with 6 records
http://127.0.0.1:8000/student/?limit=6&offset=9 to display 6 records in a page after record no. 9 '''
class StudentList(ListAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	pagination_class = MyCursorPagination

