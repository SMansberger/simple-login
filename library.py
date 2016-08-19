class InputCars(object):
    def __init__(self):
        #array to hold list of cars
        self.__car_list = []

    #adds cars to array
    def add_car(self, m):
        self.__car_list.append(m)
        print m.make

    #lists out cars from gathered inputs
    def compile_list(self):
        output = ''
        for car in self.__car_list:
            output += 'Make: ' + car.make + ' Model: ' + car.model + ' Year: ' + str(car.year) + ' Price: ' + car.price + '<br />'
        return output

    def calc_price(self):
        #years
        price = []
        for car in self.__car_list:
            price.append(car.price)

        #determines highest priced car from car prices passed to array
        highestprice = max(price)

        return 'The most expensive car you own costs $' + str(highestprice) + "!"

class CarData(object): #Data Object
    def __init__(self):
        self.make = ''
        self.model = ''
        self.__year = 0
        self.price = ''

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y):
        if y > 2017: #if date is not valid
            print "Error: Enter a valid year!"
        else:
            self.__year = y
