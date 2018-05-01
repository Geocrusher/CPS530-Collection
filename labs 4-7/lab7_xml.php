<!DOCTYPE html>
<html>

<head>
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<meta http-equiv="refresh" content="240">

<style>
table {
	table-layout: fixed;
	width: 200px;
}
input {
	text-align: center;
}
</style>

<title> Lab 7 - XML </title>

<!-- Bootstrap stuff -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>

<link href="https://fonts.googleapis.com/css?family=Dosis" rel="stylesheet">

<style>
.jumbotron {
	background-image: url("download.png");
	background-size: cover;
	color: white;
	text-align: center;
}
img {
object-fit: contain;
}
</style>
</head>

<body>

<div class="container">
	<div class="jumbotron">
		<h1 class="display-3" style="font-family:'Dosis', sans-serif;">Lab 7 - XML</h1>
	</div>

	<div class="card text-center" style="padding: 10px 30px">
		<?php
		$xml = simplexml_load_file("http://107.170.98.130/yr2/cache_yr2.txt");
		$coverArt = $xml->track->cover;
		$title = $xml->track->title;
		$artist = $xml->track->artists;
		$startTime = $xml->track->starttime;
		$duration = $xml->track->playduration;

		echo "<img class\"card-image-top col-2\" src=\"$coverArt\" alt=\"Cover Art\"";
		echo "<div class=\"card-body\">";
		echo "<h3>$title</h3>";
		echo "<p>$artist</p>";
		echo "<hr>";
		echo "<p><span style=\"font-weight: bold\">Start time (CET): </span><br>";
		echo "$startTime</p>";
		echo "<p><span style=\"font-weight: bold\">Duration: </span><br>";
		echo "$duration</p>";
		echo "</div>";
		?>
	</div>
</div>

</body>

</html>
