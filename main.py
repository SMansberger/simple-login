'''
Steven Mansberger
August 16, 2016
Design Patterns for Web Programming
Reusable Library
'''

import webapp2
from library import CarData, FavoriteMovies
from pages import Page


class MainHandler(webapp2.RequestHandler):
    def get(self):
        # page for class
        p = Page()
        lib = FavoriteMovies()

        p.body = """<form name="carForm" method="GET">
                <h2>Car One</h2>
                <label>Make: </label><input type="text" name="carmakeone" required>
                <label>Model: </label><input type="text" name="carmodelone" required>
                <label>Year: </label><input type="text" name="caryearone" required>
                <label>Price: </label><input type="text" name="carpriceone" required>
                <input type="submit" value="Submit" /></br>

                <h2>Car Two</h2>
                <label>Make: </label><input type="text" name="carmaketwo" required>
                <label>Model: </label><input type="text" name="carmodeltwo" required>
                <label>Year: </label><input type="text" name="caryeartwo" required>
                <label>Price: </label><input type="text" name="carpricetwo" required>
                <input type="submit" value="Submit" /></br>

                <h2>Car Three</h2>
                <label>Make: </label><input type="text" name="carmakethree" required>
                <label>Model: </label><input type="text" name="carmodelthree" required>
                <label>Year: </label><input type="text" name="caryearthree" required>
                <label>Price: </label><input type="text" name="carpricethree" required>
                <input type="submit" value="Submit" /></br>

                <h2>Car Four</h2>
                <label>Make: </label><input type="text" name="carmakefour" required>
                <label>Model: </label><input type="text" name="carmodelfour" required>
                <label>Year: </label><input type="text" name="caryearfour" required>
                <label>Price: </label><input type="text" name="carpricefour" required>
                <input type="submit" value="Submit" /></br>
                </form>"""

        if self.request.GET:

            md1 = CarData()
            md1.make = self.request.GET['carmakeone']
            md1.model = self.request.GET['carmodelone']
            md1.year = self.request.GET['caryearone']# actually calling function
            md1.price = self.request.GET['carpriceone']
            lib.add_movie(md1)

            md2 = CarData()
            md2.make = self.request.GET['carmaketwo']
            md2.model = self.request.GET['carmodeltwo']
            md2.year = self.request.GET['caryeartwo']  # actually calling function
            md2.price = self.request.GET['carpricetwo']
            lib.add_movie(md2)

            md3 = CarData()
            md3.make = self.request.GET['carmakethree']
            md3.model = self.request.GET['carmodelthree']
            md3.year = self.request.GET['caryearthree']  # actually calling function
            md3.price = self.request.GET['carpricethree']
            lib.add_movie(md3)

            md4 = CarData()
            md4.make = self.request.GET['carmakefour']
            md4.model = self.request.GET['carmodelfour']
            md4.year = self.request.GET['caryearfour']  # actually calling function
            md4.price = self.request.GET['carpricefour']
            lib.add_movie(md4)

            p.body = lib.compile_list() + lib.calc_time_span()
            self.response.write(p.print_out())
        else:
            self.response.write(p.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
