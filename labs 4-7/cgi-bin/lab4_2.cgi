#!/usr/bin/perl

use CGI ':standard';

$name = param('name');
$uni = param('uni');
$type = param('type');
$extra = param('extra');

unless ($name) {
	$name = "anonymous";
}

print "Content-type: text/html\n\n";
print(qq( <head> <link href="https://fonts.googleapis.com/css?family=Dosis:700" rel="stylesheet">  </head> ));
print(qq( <body> <h1 style="font-family: 'Dosis', sans-serif; text-align: center; color: #6495ed;"> Hello $name! ));

if ($uni eq "none") {
	print(qq( You are not in/from a university? That is OK! ));
}
elsif ($type eq "" || $type eq "none" ) {
	print(qq( So you do something else at $uni? Interesting! ));
}
else {
	print(qq( You are a $type at $uni? Cool! ));
}

print "</h1>";

if ($name eq "Dave Mason" && $type eq "professor" && $uni eq "Ryerson") {
	print(qq( <h1 style="font-family: 'Dosis', sans-serif; text-align: center; color: red"> Welcome, you four-holed being </h1> ));
}

if ($extra) {
print(qq( <h2 style="font-family: 'Dosis', sans-serif; text-align: center;"> You also said: $extra </h2> ));
}

print "</body>";
