from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .serializers import StudentSerializer
from .models import Student
from rest_framework.throttling import ScopedRateThrottle

class StudentList(ListAPIView):
	queryset = Student.objects.all()
	serializer_class= StudentSerializer
	throttle_classes = [ScopedRateThrottle]
	
	#we can make instance of ScopedRateThrottle and define our own throttle rate.
	#We have defined throttling in setting for viewstu as 5 requests per hour
	throttle_scope = 'viewstu'

class StudentCreate(CreateAPIView):
	queryset = Student.objects.all()
	serializer_class= StudentSerializer
	throttle_classes = [ScopedRateThrottle]
	
	#we can make instance of ScopedRateThrottle and define our own throttle rate differently in different classes.
	#We have defined throttling in setting for modifystu as 2 requests per day
	throttle_scope = 'modifystu'

class StudentRetreive(RetrieveAPIView):
	queryset = Student.objects.all()
	serializer_class= StudentSerializer
	throttle_classes = [ScopedRateThrottle]
	throttle_scope = 'viewstu'

class StudentDestroy(DestroyAPIView):
	queryset = Student.objects.all()
	serializer_class= StudentSerializer
	throttle_classes = [ScopedRateThrottle]
	throttle_scope = 'modifystu'

class StudentUpdate(UpdateAPIView):
	queryset = Student.objects.all()
	serializer_class= StudentSerializer
	throttle_classes = [ScopedRateThrottle]
	throttle_scope = 'modifystu'



'''
class StudentLC(ListCreateAPIView):
	queryset = Student.objects.all()
	serializer_class= StudentSerializer
	throttle_classes = [ScopedRateThrottle]


class StudentRU(RetrieveUpdateAPIView):
	queryset = Student.objects.all()
	serializer_class= StudentSerializer
	throttle_classes = [ScopedRateThrottle]


class StudentRD(RetrieveDestroyAPIView):
	queryset = Student.objects.all()
	serializer_class= StudentSerializer
	throttle_classes = [ScopedRateThrottle]

class StudentRUD(RetrieveUpdateDestroyAPIView):
	queryset = Student.objects.all()
	serializer_class= StudentSerializer
	throttle_classes = [ScopedRateThrottle]
'''