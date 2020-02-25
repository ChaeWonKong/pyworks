class Vehicle:
    def __init__(self, passingers=[]):
        self.passingers = passingers
    
    def give_ride(self, list):
        self.passingers.extend(list)


class Car(Vehicle):
    def __init__(self, passingers, driver, gear):
        super().__init__(passingers)
        self.driver = driver
        self.gear = gear

    def change_gear(self, newGear):
        self.gear = newGear
        print("Gear Changed: {}".format(self.gear))

    def __str__(self):
         return "driver: {} passingers: {} gear: {}"\
             .format(self.driver, self.passingers, self.gear)
    

class Airplane(Vehicle):
    def __init__(self, passingers, pilots, crews):
        self.passingers = passingers
        self.pilots = pilots
        self.crews = crews
    
    def take_off(self):
        message = ("Ladies and Gentlemen, " + 
                    "our plane is about to take off. " + 
                    "Please fasten your seat belt.")
        print(message)

    def __str__(self):
        return "pilots: {}, passengers: {}, crews: {}"\
            .format(self.pilots, self.passingers, self.crews)


if __name__ == "__main__":
    car = Car(["Steve"], "Leon", "P")
    print(car)
    car.give_ride(["Kay"])
    print(car)
    car.change_gear("D")

    airplane = Airplane(\
    ["Homer", "Marge", "Bart", "Lisa", "Maggie"],\
     ["Luke", "Han"], ["Anakin", "Yoda"])
    print(airplane)
    airplane.take_off()
