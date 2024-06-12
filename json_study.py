import json

# with open('human.json', mode='r') as file:
#     data = json.load(file)
#     print(data)

# with open('human.json', mode='a') as file:
#     data = {1: 2}
#     json.dump(data, file)

data = {'name': 'vic', 6: 5, 'weight': None}
data_json = json.dumps(data)
print(data_json)

data = json.loads(data_json)
print(data)


