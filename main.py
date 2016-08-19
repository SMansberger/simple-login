'''
Steven Mansberger
August 16, 2016
Design Patterns for Web Programming
Reusable Library
'''

import webapp2
from library import MovieData, FavoriteMovies
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):

        #page for class
        p = Page()
        lib = FavoriteMovies()


        # movie title
        # year movie was made
        # director of the film
        md1 = MovieData()
        md1.title = "The Princess Bride"
        md1.year = 1987 #actually calling function
        md1.director = "Rob Reiner"
        lib.add_movie(md1)

        md2 = MovieData()
        md2.title = "The Dark Knight"
        md2.year = 2008  # actually calling function
        md2.director = "Christopher Nolan"
        lib.add_movie(md2)

        md3 = MovieData()
        md3.title = "Star Wars"
        md3.year = 1977  # actually calling function
        md3.director = "George Lucas"
        lib.add_movie(md3)


        p.body = lib.compile_list() + lib.calc_time_span()
        self.response.write(p.print_out())


        # page_head = '''
        # <!DOCTYPE HTML>
        # <html>
        #     <head>
        #         <title>Enter your information:</title>
        #         <link href="css/styles.css" rel="stylesheet" type="text/css" />
        #     </head>
        #     <body>'''
        #
        # # page_body = '''<form method="GET">
        # #             <label>Name: </label><input type="text" name="user" />
        # #             <label>Email:</label><input type="text" name="email" />
        # #             <input type="submit" value="Submit" />'''
        # page_body = '''
        # <a href="?email=mickey@disney.com&user="Mickey">Mickey</a><br/>
        # <a href="?email=donald@disney.com&user=Donald">Donald</a><br/>
        # <a href="?email=minnie@disney.com&user=Minnie">Minnie</a><br/>
        # <a href="?email=pluto@disney.com&user=Pluto">Pluto</a><br/>
        # '''
        # page_close = '''
        #         </form>
        #     </body>
        # </html>'''
        # if self.request.GET:
        #     user = self.request.GET['user']
        #     email = self.request.GET['email']
        #     self.response.write(page_head + user + ' ' + email + page_close)
        # else:
        #     self.response.write(page_head + page_body + page_close)
        #
        # #self.response.write(page) #printing information

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
