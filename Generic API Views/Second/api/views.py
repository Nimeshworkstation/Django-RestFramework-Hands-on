from rest_framework.generics import GenericAPIView
from .serializers import StudentSerializer
from .models import Student
from rest_framework.mixins import ListModelMixin,CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


#Create and List - PK not Required
class StudentLC(GenericAPIView, ListModelMixin, CreateModelMixin):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


#Update, Delete and Retreive - PK is Required	
class StudentRUD(GenericAPIView,RetrieveModelMixin,UpdateModelMixin, DestroyModelMixin):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)


	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)



	









