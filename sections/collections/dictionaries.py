## dictionaries
# associated lists or a map
# key: value (name: pepito)

# set a dictionary and print contet
x = {'name': 'DEMETRIO', 'surname': 'ALBERTINI', 'age': 9999}
print(x)

# print key
print(x['name'])

# datatypes on a dictionary
y = {'name': 'PAOLO', 99: 'TRUE', 'player': True}
print(y)

# get value
print(y.get('name'))

# add key:value to dictionary | in case key exists, value will be overwrited
y['surname'] = 'MALDINI'
print(y)

# update value
y.update({'surname': 'BARESI'})
print(y)

# remove key:value
y.pop(99)
print(y)

# list keys
print(y.keys())

# list values
print(y.values())

# list k/v
print(y.items())
