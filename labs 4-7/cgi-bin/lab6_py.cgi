#!/usr/bin/python

import cgi, cgitb, string
form = cgi.FieldStorage()

fullName = string.capwords(form.getvalue('name').title())
address = string.capwords(form.getvalue('address'))
numbers = form.getvalue('number').split('-')

print "Content-Type: text/html\r\n"

print "<html>"
print "<head>"
print "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\">"
print "<title> Lab 6 - Python </title>"

print "<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css\" integrity=\"sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb\" crossorigin=\"anonymous\">"
print "<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js\" integrity=\"sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ\" crossorigin=\"anonymous\"></script>"
print "<script src=\"https://code.jquery.com/jquery-3.2.1.slim.min.js\" integrity=\"sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN\" crossorigin=\"anonymous\"></script>"
print "<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js\"></script>"
print "<script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js\" integrity=\"sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh\" crossorigin=\"anonymous\"></script>"

print "<link href=\"https://fonts.googleapis.com/css?family=Dosis\" rel=\"stylesheet\">"

print "<style>.jumbotron{background-image: url(\"../download.png\");background-size: cover;color: white;text-align: center;}</style>"

print "<script> $(document).ready(function(){ $(\"button\").click(function(){ $(\"#num1\").animate({fontSize: '2em'}); $(\"#num2\").animate({width: '500px'}); $(\"#num3\").animate({opacity: '0.25'}); }); }); </script>"
print "</head>"

print "<body style=\"text-align:center\">"

print "<div class=\"container-fluid\">"
print "<div class=\"jumbotron\">"
print "<h1 class=\"display-3\" style=\"font-family:\'Dosis\', sans-serif;\"> Python Side </h1>"
print "</div>"

print "<div class=\"card\" style=\"padding: 10px 30px\">"
print "<div> <h1>", fullName, "</h1> </div>"
print "<div> <h1>", address, "</h1> </div>"
print "<div><button class=\"btn btn-primary\"> Animate Numbers </button></div></div>"

print "<div class=\"card\" style=\"font-size: 5em\">"
print "<p>"
print "<span id=\"num1\">(", numbers[0], ")</span>"
print "<span id=\"num2\">", numbers[1], "</span>"
print "-"
print "<span id=\"num3\">", numbers[2], "</span>"
print "</p>"
print "</div>"

print "</div>"

print "</body></html>\r\n"

