from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import StudentSerializer
from .models import Student




class StudentLC(ListCreateAPIView):
	queryset = Student.objects.all()
	serializer_class= StudentSerializer




class StudentRUD(RetrieveUpdateDestroyAPIView):
	queryset = Student.objects.all()
	serializer_class= StudentSerializer
