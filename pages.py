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
    <script>
    function carValidate() {
        var x, text;

        // Get the value of the input field with id="numb"
        x = document.getElementById("caryearone").value;

        if (isNaN(x) || x < 1 || x > 2018) {
            text = "Input not valid";
        } else {
            text = "Input OK";
        }
        document.getElementById("demo").innerHTML = text;
    }
    </script>

            </body>
        </html>"""

    def print_out(self):
        everything = self.__head + self.body + self.__close
        return everything
