from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions



class StudentModelViewSet(viewsets.ModelViewSet):

	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	authentication_classes = [SessionAuthentication]

	#If User is registered, then only it can access api
	#permission_classes = [IsAuthenticated]
	
	#Anyone can access API, registered, not register anyone
	#permission_classes = [AllowAny]
	
	#Only the user who are registered and have staff_status can access api
	#permission_classes = [IsAdminUser]

	#Read Only Permission of not logged user, if logged in then can perform CRUD
	#permission_classes = [IsAuthenticatedOrReadOnly]



	#To allow permission we have to select users in admin and allow pemissions as required.
	#permission_classes = [DjangoModelPermissions]

	permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
