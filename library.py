class FavoriteMovies(object):
    def __init__(self):
        self.__car_list = []
        #create array to hold movie information
        #create method to add to array
        #generate list of movies
        #calculate time between movies

    def add_movie(self, m):
        self.__car_list.append(m)
        print m.make

    def compile_list(self):
        output = ''
        for car in self.__car_list: #for each movie in array
            output += 'Make: ' + car.make + ' Model: ' + car.model + ' Year: ' + str(car.year) + ' Price: ' + car.price + '<br />'
        return output

    def calc_time_span(self):
        #years
        years = []
        for movie in self.__car_list:
            years.append(movie.year)
        #sort years
        years.sort()

        #subtract lowest year from highest
        num = len(years) - 1
        span = years[num] - years[0]

        return 'The time between the oldest and newest film entered is ' + str(span)

        #return span

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
