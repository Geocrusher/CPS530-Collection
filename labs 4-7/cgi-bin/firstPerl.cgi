#!/usr/bin/perl
use CGI':standard';
use strict;

print "Content-type: text\html\n\n";

print 
(qq
	(	
		<head>
		<title>First Perl Program</title>
		<link href="https://fonts.googleapis.com/css?family=Dosis:400,800" rel="stylesheet">
		</head>
		
		<body>
			<h1 style="font-family: 'Dosis', sans-serif; color: #6496ED; text-align: center">
				This is my first Perl program
			</h1>
		</body>
	)
);

