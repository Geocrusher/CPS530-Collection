<!DOCTYPE html>
<html>

<head>
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

<style>
table {
	table-layout: fixed;
	width: 200px;
}
input {
	text-align: center;
}
</style>

<title> Lab 5 - PHP </title>

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
</style>
</head>

<body>

<div class="container">
	<div class="jumbotron">
		<h1 class="display-3" style="font-family:'Dosis', sans-serif;">Lab 5 - PHP</h1>
	</div>

	<div class="text-center">
	<?php
		$col = $_POST['col'];
		$row = $_POST['row'];

		if ( $col > 12 || $row > 12 || $col < 3 || $row < 3 )
		{
			echo "<h5>Please input the dimensions of the table (3x3 to 12x12)</h5>";
		}
		else
		{
			echo "<table class=\"table\">";
			echo "<thead>";
				echo "<tr>";
				echo "<th> X </th>";

			for ( $colCount = 1; $colCount <= $col; $colCount++ )
			{
				echo "<th>$colCount</th>";
			}
				echo "</tr>";
			echo "</thead>";
			echo "<tbody>";

			for ( $rowCount = 1; $rowCount <= $row; $rowCount++ )
			{
				echo "<tr><th scope=\"row\">$rowCount</th>";

				for ( $multCount = 1; $multCount <= $col; $multCount++ )
				{
					$prod = $rowCount * $multCount;
					echo "<td>$prod</td>";
				}
				echo "</tr>";
			}
			echo "</tbody>";
			echo "</table>";
		}
	?>
	</div>

	<div class="card text-center" style="padding: 10px 30px">
	<form action="" method="post">
		<div class="form-group" style="padding: 5px">
		<div class="input-group">
			<input type="text" class="form-control" name="col">
			<span class="input-group-addon">X</span>
			<input type="text" class="form-control" name="row">
		</div>
		</div>

		<button type="submit" class="btn btn-primary"> Submit </button>
	</form>
	</div>
</div>

</body>

<footer class="container-fluid text-center" style="padding:10px">
<p>
<?php
session_start();

if(isset($_SESSION['views']))
  $_SESSION['views'] = $_SESSION['views']+1;
else
  $_SESSION['views'] = 1;

echo "View Count: ". $_SESSION['views'];

?>
</p>
</footer>

</html>
