<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modul 1 Soal 3</title>
</head>

<body>
    <table style="margin: auto;">
        <th colspan="2">
            <h1>Modul 1 PHP Variabel Dan Tipe Data</h1>
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
$y = "y : Adalah Variabel Global";

function soal3()
{
    global $y;
    $x = "x : Adalah Variabel Local";
    echo $x . "<br>";
    echo $y;
}
soal3();
?>