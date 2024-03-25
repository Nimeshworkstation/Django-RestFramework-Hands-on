from rest_framework.pagination import LimitOffsetPagination

class MyPageNumberPagination(LimitOffsetPagination):
	
	#setting default details limit
	default_limit = 5

	#overriding  keyword 'limit' to our own keyword mylimit and offset to myoffset.
	''' Now instead of 
	http://127.0.0.1:8000/student/?limit=6  to display a page with 6 records
	http://127.0.0.1:8000/student/?limit=6&offset=9 to display 6 records in a page after record no. 9 

	We shoudl use our new keyword http://127.0.0.1:8000/student/?limit=6  to display a page with 6 records
http://127.0.0.1:8000/student/?mylimit=6&myoffset=9 to display 6 records in a page after record no. 9 '''


#Setting maximum limit. This won't return 10 data becuase we have set max_limit = 6 http://127.0.0.1:8000/student/?mylimit=10&myoffset=9
	max_limit = 6
	limit_query_param = 'mylimit'
	offset_query_param = 'myoffset'
