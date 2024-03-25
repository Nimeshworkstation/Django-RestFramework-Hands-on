import requests
import json

URL = "http://127.0.0.1:8000/student/"

def get_data(id = None):
	data ={}
	if id is not None:
		data = {'id': id}
	json_data = json.dumps(data)
	r = requests.get(url = URL, data = json_data )
	data = r.json()
	print(data)

#get_data(2)

def post_data():
	data = {

	'name': 'nagar',
	'roll': 20,
	'city':'bochum'
	}
	json_data = json.dumps(data)
	r = requests.post(url = URL, data = json_data)
	data = r.json()
	print(data)

post_data()

#For complete update, we should provide all fields.
#here, we are doing partial update so only 3 fields are provied.
def update_data():
	data = {
	'id': 2,
	'name': 'Nikkydon',
	'city':'germany'
	}
	json_data = json.dumps(data)
	r = requests.put(url = URL, data = json_data)
	data = r.json()
	print(data)

#update_data()

def delete_data():
	data = {
	'id': 5,
	}
	json_data = json.dumps(data)
	r = requests.delete(url = URL, data = json_data)
	data = r.json()
	print(data)

#delete_data()