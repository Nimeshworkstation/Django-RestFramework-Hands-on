from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer


# Create your views here.
#Here are two methods to do display the details. 

#----------------Method 1---------------


def student_detail(request, pk):
	stu = Student.objects.get(id=pk)
	serializer = StudentSerializer(stu)
	return JsonResponse(serializer.data, safe = True)

def student_list(request):
	stu = Student.objects.all()
	serializer = StudentSerializer(stu, many = True)
	return JsonResponse(serializer.data, safe = False)


'''#Method 2
def student_detail(request, pk ):
	stu = Student.objects.get(id=pk)
	print('stu :',stu)
	print('-------------')
	serializer = StudentSerializer(stu)
	print('serializer:',serializer)
	print('---------------')
	print('serializer.data:',serializer.data)
	print('---------------')
	json_data = JSONRenderer().render(serializer.data)
	print('json_data:',json_data)
	return HttpResponse(json_data, content_type = 'application/json')



def student_list(request):
	stu = Student.objects.all()
	print('stu :',stu)
	print('-------------')
	serializer = StudentSerializer(stu, many = True)
	print('serializer:',serializer)
	print('---------------')
	print('serializer.data:',serializer.data)
	print('---------------')
	json_data = JSONRenderer().render(serializer.data)
	print('json_data:',json_data)
	return HttpResponse(json_data, content_type = 'application/json')

'''
