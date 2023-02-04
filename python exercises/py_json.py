# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

#  Sample JSON
userJSON_ya = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse to dict
user_ya = json.loads(userJSON_ya)

# print(user_ya)
# print(user['first_name'])

car_ya = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON_ya = json.dumps(car_ya)

print(carJSON_ya)