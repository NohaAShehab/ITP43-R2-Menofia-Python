

info =['noha', 'system admin', 'iti', 'cairo']

### unlabeled data

### datatype ---> descriptive --->

""" datatype --->comma seperated key:values pair ---> dictionary  """

"""1- define dict """
d = {}
myd= dict()

""" 2- dict ---> comma seperated key value pair ---> doesn't allow key duplication """
info = {"name":"Noha", 'track':"system admin", 'year':2023, 'age':30,
        'name':"Noha Shehab", 5:'Cairo'}
print(info)

""" 3- access elements using key """
print(info['name'])

"""4- dict is mutable datatype """
info["name"]='Ahmed'
print(info)
info["grade"]= 'very good'  # if key doesn't exist 000> will add key:value pair to the dict
print(info)

"""5- loop over the dict """

for item in info:  # keys
    print(f"item ={item}, value = {info[item]}")

""" 6- check item exists in the dict """
print("Cairo" in info)  # in operator check if the value exists in the keys


"""7- get dict keys """

keys = info.keys()  # return keys in dict_keys 0---> can be casted to a list
keys_list = list(keys)
print(keys_list)

"""7- get dict values """

values = info.values()  # return keys in dict_values 0---> can be casted to a list
values_list = list(values)
print(values_list)

"""8- get dict items """
items = info.items() # dict keys
print(items)
items_list =list(items)
print(items_list)

# for i in info.items():
#     print(i)
for key , value in info.items():
    print(f"{key}:{value}")


""" update a dict """
basic_info = {
    "firstname":"noha",
    "lastname":"shehab"
}

additional_info = {
    "age":30,
    "track":"system admin",
    "firstname":"Noha Shehab"
}

basic_info.update(additional_info)
print(basic_info)


"""get length of the dict """
print(len(info))

""" clear dict """
# info.clear()
# print(info)

""" pop element form the dict """

popped_value=info.pop("name")
print(popped_value)
print(info)

""" delete element from dict or list """
del additional_info["age"] # remove key value pair from the dict











