person = {
    "name": "Paul",
    "age": 35,
    "address": "Enugu state"
}

print(person.items())

for key, value in person.items():
    print(f"key:{key} value:{value}")



#for key in person:
  #  print(f"key:{key} value:{person[key]}")


#print(person["name"])
#print(person["age"])
#print(person["address"])
#print(person.keys())
#print(person.values())
#person.clear()
#person["age"] = 100
#print(person)