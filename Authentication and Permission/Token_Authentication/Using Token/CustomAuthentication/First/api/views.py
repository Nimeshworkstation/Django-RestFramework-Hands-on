from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.customauth import CustomAuth


class StudentModelViewSet(viewsets.ModelViewSet):

	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	authentication_classes = [CustomAuth]
	permission_classes = [IsAuthenticated]
