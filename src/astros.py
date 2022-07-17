import requests

"""
the api returns:

{'number': 10, 'people': [{'name': 'Oleg Artemyev', 'craft': 'ISS'}, {'name': 'Denis Matveev', 'craft': 'ISS'}, {'name': 'Sergey Korsakov', 'craft': 'ISS'}, {'name': 'Kjell Lindgren', 'craft': 'ISS'}, {'name': 'Bob Hines', 'craft': 'ISS'}, {'name': 'Samantha Cristoforetti', 'craft': 'ISS'}, {'name': 'Jessica Watkins', 'craft': 'ISS'}, {'name': 'Cai Xuzhe', 'craft': 'Tiangong'}, {'name': 'Chen Dong', 'craft': 'Tiangong'}, {'name': 'Liu Yang', 'craft': 'Tiangong'}], 'message': 'success'}

"""
response = requests.get("http://api.open-notify.org/astros.json")
json = response.json()

for person in json['people']:
    print(person['name'], 'lives in', person['craft'])