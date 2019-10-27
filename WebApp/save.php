<html>
<body>
<?php
   $var=$_GET['sup'];
   print("Your Coordinates are <br>");
   print($var);
   //print($_GET[])
$servername = "localhost";
$username = "root";
$password = "password";
$dbname = "gpsdb";
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
$var_arr=preg_split("/\,/",$var);
$ip=$var_arr[0];
//$var_arr=explode(",",$var);
//$ip=$var_arr[0];
//$ip='10.16.160.171';
$sql= "DELETE FROM ambulance WHERE ip = $ip;";
if ($conn->query($sql) === TRUE) {
  echo "Duplicates deleted";
} else {
  echo "This is a new ip ";
}    
$sql = "INSERT INTO ambulance (ip,latitude, longitude, speed, direction) VALUES ($var);";
if ($conn->query($sql) === TRUE) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}
$conn->close();
?>
</body>
</html>
