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
        
        self.body = ""
        self.__close = """
                </form>
            </body>
        </html>"""

    def print_out(self):
        everything = self.__head + self.body + self.__close
        return everything
