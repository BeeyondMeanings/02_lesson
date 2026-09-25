mycar = {
"brand": "Range Rover Sports",
 "model": "HSE",
 "year": 2017

}
print(mycar)

mygreens = dict(fruit="green apples", vegetables="kale")

print(mygreens)
print(len(mygreens))
mycar["year"] = 2019
#print(mycar)

#print(mycar.get("year"))

#mycar.update({"color": "silver"})
#print(mycar)

b = mycar.keys() #you can also use "value" instead of keys
print(b)

#mycar.pop("color")
#print(mycar)

#mycar.clear()
print(mycar)

#del mycar
#print(mycar)