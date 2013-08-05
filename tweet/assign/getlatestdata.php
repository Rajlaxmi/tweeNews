<?php
header('Access-Control-Allow-Origin: *');

$con=mysqli_connect("localhost","root","","Tweet");
// Check connection
if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }

$result = mysqli_query($con,"SELECT * FROM sentiment");
$r="";
while($row = mysqli_fetch_array($result))
  {
 // echo $row['FirstName'] . " " . $row['LastName'];
  //echo "<br>";
$r=$row;
  }

mysqli_close($con);
    $scores = array(
        'x'    => $r[1],
        'y' => $r[2],
				'z' => $r[3]
    );
 
    header('Content-type: application/json');
 
    echo json_encode($scores);
?>
