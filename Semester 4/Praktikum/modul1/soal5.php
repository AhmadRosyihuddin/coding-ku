<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modul 1 Soal 5</title>
</head>

<body>
    <table style="margin: auto;">
        <th colspan="2">
            <h1>Modul 1 PHP Hari</h1>
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
setlocale(LC_ALL, 'id-ID', 'id_ID');
echo "Sekarang " . strftime('Hari %A: Tanggal %d %B %Y');
?>