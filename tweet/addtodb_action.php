<?php
$con=mysqli_connect("localhost","root","","Tweet");
// Check connection
if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }
$lat = $_GET["x"];
$long =$_GET["y"];
$score = $_GET["z"];
mysqli_query($con,"INSERT INTO sentiment (x,y,z)
VALUES ($lat,$long,$score)");


mysqli_close($con);
?>

