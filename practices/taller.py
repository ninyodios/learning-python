# Objective
# List solutions per product
import requests
import json

ea_url = "http://ea-governance.service.shared.discovery:8080/service.ea.governance/1.0/buildingblocks/"
key = "productAlias"

ea_response = requests.get('http://ea-governance.service.shared.discovery:8080/service.ea.governance/1.0/buildingblocks/')
my_json = ea_response.json()
print(my_json)


data = {key: value['productAlias'] for key, value in my_json}
print(data)


#with open('json-like.txt') as data_file:
#    objs = (json.loads(line).popitem() for line in data_file)
#    data = {key: value['score'] for key, value in objs}

#results = {}
#for block in my_json:
#    tracked_key = block[key]
    #print(tracked_key)
    #print(block['itAccount'])
    #print('##############')2
    #results.setdefault(key, {})
#    for item in block.items():
#        print(item)
        #print(item[0], item[1])
        #if (item[1]) == "hbg-platform-common":
        #    print(item[0])
        #    print("#######")
        #print(item)

    #print (tracked_key)
    #print (items[tracked_key])


#https://stackoverflow.com/questions/46348256/python-group-a-list-of-dicts-by-key-value-count-separate-key-value-as-dict
#results = {}
#key = 'name'
#for line in data:
#    tracked_key = line[key]
#    results.setdefault(tracked_key, {})
#    for k, v in line.iteritems():
#        if k == key:
#            continue
#        results[tracked_key].setdefault(v, 0)
#       results[tracked_key][v] += 1







