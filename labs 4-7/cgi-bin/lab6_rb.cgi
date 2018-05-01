#!/usr/bin/ruby

print "Content-type: text/html\n\n"
require 'cgi'
cgi = CGI.new

print <<BEGINNING

  <html>

  <head>
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <title> Lab 6 - Ruby </title>

  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>
  <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>

  <link href="https://fonts.googleapis.com/css?family=Dosis" rel="stylesheet">

  <style>
    .jumbotron
    {
      background-image: url("../download.png");
	    background-size: cover;
	    color: white;
	    text-align: center;
    }
  </style>

  <script>
  $(document).ready(function(){
    $("button").click(function(){
        $("#num1").fadeIn();
        $("#num2").fadeIn("slow");
        $("#num3").fadeIn(3000);
    });
  });
  </script>

  </head>

  <body style="text-align:center">

    <div class="container">
	    <div class="jumbotron">
		    <h1 class="display-3" style="font-family:'Dosis', sans-serif;"> Ruby Side </h1>
	    </div>

	    <div class="card" style="padding: 10px 30px">

BEGINNING

name = cgi['name'].split.map(&:capitalize)*' '
address = cgi['address'].split.map(&:capitalize)*' '
number = cgi['number'].split(/\-/)

print "<div> <h1> " + name + " </h1> </div>"
print "<div> <h1> " + address + " </h1> </div>"

print "
<div>
  <h1>
    <span id=\"num1\" class=\"display-1\" style=\"color:red;display:none\"> (" + number[0] + ") </span>
    <span id=\"num2\" class=\"display-1\" style=\"color:green;display:none\"> " + number[1] + "</span>
    <span class=\"display-3\"> - </span>
    <span id=\"num3\" class=\"display-1\" style=\"color:blue;display:none\">" + number[2] + "</span>
  </h1>
</div>
"
print <<ENDING
      <div>
      <button class="btn btn-primary"> Fade In Numbers </button>
      </div>
      </div>

    </div>

  </body>

  </html>
ENDING
