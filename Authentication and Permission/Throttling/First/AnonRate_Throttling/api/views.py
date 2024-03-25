from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from api.throttling import JackRateThrottle

class StudentModelViewSet(viewsets.ModelViewSet):

	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAuthenticatedOrReadOnly]
	
	#AnonRateThrottle => Anonymous User
	#UserRateThrottle => Registered Users
	#Check settings.py for global setting of values.

	throttle_classes = [AnonRateThrottle,UserRateThrottle]

	#overriding UserRate as our requirement in throttle.py and using it.
	#For same user, we can set different throttling in  different classes. example is shown here.
	#throttle_classes = [AnonRateThrottle, JackRateThrottle]

	