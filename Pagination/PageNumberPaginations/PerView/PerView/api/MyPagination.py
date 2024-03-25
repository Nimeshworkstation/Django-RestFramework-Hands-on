from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
	page_size = 5

	#We can override the term "page" to 'p'. Now we can search using http://127.0.0.1:8000/student/?p=3
	page_query_param = 'p'

	#We can use 'records' to get required data . For example we have page size defined as 5. But in Url we can provide extra query as get results as desired.
	#For example, http://127.0.0.1:8000/student/?p=1&records=7. Here we will get page 1 with 7 records eventough we have defined page_size 5.
	#This is extrafeature can be given to client to view resutl as desired
	page_size_query_param = 'records'


	#We can define the maximnum number of page_size that user can give in url . for example 
	'''http://127.0.0.1:8000/student/?page=3&records=7 . This means the maximum nubmer of page size the user can give is 7
	http://127.0.0.1:8000/student/?page=3&records=11 will give the result same as page_size 7.'''
	max_page_size = 7