class Page(object):
    def __init__(self):
        self.__title = "Welcome!"
        self.css = "css/styles.css"
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Enter your information:</title>
        <link href="css/styles.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """
        
        self.body = '''
        <form method="GET">
        <label>Name: </label><input type="text" name="user" />
        <label>Email:</label><input type="text" name="email" />
        <input type="submit" value="Submit" />'''
        self.__close = '''
                </form>
            </body>
        </html>'''

    def print_out(self):
        everything = self.__head + self.body + self.__close
        return everything
