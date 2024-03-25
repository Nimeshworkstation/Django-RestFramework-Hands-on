from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .serializers import StudentSerializer
from .models import Student


class StudentList(ListAPIView):
	queryset = Student.objects.all()
	serializer_class= StudentSerializer

class StudentCreate(CreateAPIView):
	queryset = Student.objects.all()
	serializer_class= StudentSerializer

class StudentRetreive(RetrieveAPIView):
	queryset = Student.objects.all()
	serializer_class= StudentSerializer

class StudentDestroy(DestroyAPIView):
	queryset = Student.objects.all()
	serializer_class= StudentSerializer

class StudentUpdate(UpdateAPIView):
	queryset = Student.objects.all()
	serializer_class= StudentSerializer

class StudentLC(ListCreateAPIView):
	queryset = Student.objects.all()
	serializer_class= StudentSerializer


class StudentRU(RetrieveUpdateAPIView):
	queryset = Student.objects.all()
	serializer_class= StudentSerializer


class StudentRD(RetrieveDestroyAPIView):
	queryset = Student.objects.all()
	serializer_class= StudentSerializer

class StudentRUD(RetrieveUpdateDestroyAPIView):
	queryset = Student.objects.all()
	serializer_class= StudentSerializer
