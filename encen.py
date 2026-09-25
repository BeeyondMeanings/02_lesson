class cars:
    def __init__(self,speed,color):
        self.__speed = speed
        self.__color = color

    def set_speed(self,value):
        self.__speed = value

    def get_speed(self):
        return self.__speed

ford = cars(250, "green")
nissan = cars(300, "red")
toyota = cars(350, "blue")

ford.set_speed(750)

ford.speed = 500

print(ford.get_speed())

#print(ford.__color)