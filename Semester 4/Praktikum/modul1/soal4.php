<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modul 1 Soal 4</title>
</head>

<body>
    <table style="margin: auto;">
        <th colspan="2">
            <h1>Modul 1 PHP Looping</h1>
        </th>
        <tr>
            <td>Nama :</td>
            <td>Ahmad Rosyihuddin</td>
        </tr>
        <tr>
            <td>NIM :</td>
            <td>200411100126</td>
        </tr>
        <tr>
            <td>Kelas :</td>
            <td>PAW A</td>
        </tr>
    </table>
</body>

</html>
<?php
echo "Looping menggunakan For";
for($x=1; $x<=10; $x++){
    echo "<br>Data Ke - $x = ", $x;
}

echo "<br><br>Looping menggunakan While";
$y = 10;
while($y > 0){
    echo "<br>Data Ke - $y = ", $y;
    $y--;
}
?>