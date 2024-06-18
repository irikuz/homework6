my_dict = {
    "Sam":1964,
    "Robert": 1987,
    "Sofia": 1994
}
print (my_dict)
existing_value = my_dict ["Sam"]
print ('Existing value: ', existing_value)
not_existing_value = my_dict.get("Lisa")
print ("Not existing value: ", not_existing_value)
my_dict.update({"Lisa": 1954, "Harry": 1985})
print(my_dict.values())
deleted_value = my_dict.pop('Lisa')
print('Deleted value: ', deleted_value)
print ("Modified dictionary: ",  my_dict)


my_set = {1, 6, 3, True, "Anna", 6, True}
print(my_set)
my_set.update([4, 5])
my_set.discard(6)
print(my_set)