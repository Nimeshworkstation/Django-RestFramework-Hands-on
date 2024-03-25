from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class StudentModelViewSet(viewsets.ModelViewSet):

	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]




'''
 We have created a token for user and token is 868b7dce81835b1d5a81997d3290d49c4328ef47. We can see token also in admin panel

We should install httpie at first to use http


Type following commands in terminal in the project folder


To see api
http http://127.0.0.1:8000/studentapi/ 'Authorization:Token 868b7dce81835b1d5a81997d3290d49c4328ef47'

To add to api
http -f POST http://127.0.0.1:8000/studentapi/ name=milan roll=14 city=Bochum 'Authorization:Token 868b7dce81835b1d5a81997d3290d49c4328ef47'

To Update to api
http -f PUT http://127.0.0.1:8000/studentapi/4/ name=milan roll=14 city=Bochum 'Authorization:Token 868b7dce81835b1d5a81997d3290d49c4328ef47'

To Delete
http -f DELETE http://127.0.0.1:8000/studentapi/4/ 'Authorization:Token 868b7dce81835b1d5a81997d3290d49c4328ef47'


'''