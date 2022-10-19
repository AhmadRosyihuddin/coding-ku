<?php
session_start();
if ($_SESSION == NULL) {
    header('location: index.php');
}

if (isset($_GET['logout'])) {
    session_destroy();
    header('location:index.php');
}

$database = array(
    ['Ahmad Rosyihuddin', '200411100126', 'Gresik'],
    ['Ahmad Fanani', '200411100143', 'Jombang'],
    ['Ahmad Teguh Setia Budiono', '200411100144', 'Lamongan'],
    ['Yoga Tirta Permana', '200411100142', 'Mojokerto'],
    ['Fiqri Dwi Wicaksono', '200411100190', 'Nganjuk']
);

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>

    <style>
        #tabel {
            font-family: Arial, Helvetica, sans-serif;
            border-collapse: collapse;
            width: 100%;
        }

        #tabel td,
        #tabel th {
            border: 1px solid #ddd;
            padding: 8px;
        }

        #tabel th {
            background-color: greenyellow;
        }

        a button {
            margin-top: 20px;
        }
    </style>
</head>

<body style="padding: 50px;">
    <h1>Daftar Mahasiswa</h1>
    <table border="1px" align="center" id="tabel">
        <th>Nama Mahasiswa</th>
        <th>NIM</th>
        <th>Alamat</th>
        <?php
        for ($i = 0; $i < count($database); $i++) { ?>
            <tr>
                <td><?= $database[$i][0] ?></td>
                <td><?= $database[$i][1] ?></td>
                <td><?= $database[$i][2] ?></td>
            </tr>
        <?php } ?>
    </table>
    <a href="<?= $_SERVER['PHP_SELF'] ?>?logout=logout"><button>Logout</button></a>
</body>

</html>