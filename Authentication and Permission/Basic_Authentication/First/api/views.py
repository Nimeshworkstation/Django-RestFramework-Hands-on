from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser



class StudentModelViewSet(viewsets.ModelViewSet):

	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	authentication_classes = [BasicAuthentication]

	#If User is registered, then only it can access api
	#permission_classes = [IsAuthenticated]
	
	#Anyone can access API, registered, not register anyone
	#permission_classes = [AllowAny]
	
	#Only the user who are registered and have staff_status can access api
	permission_classes = [IsAdminUser]

