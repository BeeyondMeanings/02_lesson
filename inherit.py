class person:
    def __init__(self, fname,lname):
        self.firstname =fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

florist = person("Jane", "Flowers")
florist.printname()

class Lawyers(person):
    def __init__(self, fname, lname, casetype):
        person.__init__(self, fname, lname)
        self.casetype = casetype

       # self.firstname =fname
        #self.lastname = lname

    def printinfo(self):
        print("Hello my name is ",self.firstname, self.lastname)



happy_lawyers = Lawyers("Jack", "smiley", "criminal")
happy_lawyers.printinfo()

print(happy_lawyers.casetype)

