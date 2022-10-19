<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tugas Praktikum Modul 3</title>
    <style>
        .requerment {
            color: red;
        }
    </style>
    <?php
    // print_r('Value Dari $_SERVER["PHP_SELF"] = ' . $_SERVER['PHP_SELF']);
    $nama = $email = $website = $comment = $gender = "";
    $namaErr = $emailErr = $websiteErr = $fieldErr = $genderErr = "";
    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        if (!empty($_POST['nama'])) {
            $nama = $_POST['nama'];
            if (!preg_match("/^[a-zA-Z ]*$/", $nama)) {
                $namaErr = "Hanya Huruf Dan Spasi yang di izinkan";
            }
        } else {
            $namaErr = "Name is required";
        }

        if (!empty($_POST['email'])) {
            $email = $_POST['email'];
            if (!filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) {
                $emailErr = 'Email Tidak Valid';
            }
        } else {
            $emailErr = "Email is required";
        }

        if (!empty($_POST['website'])) {
            $website = $_POST['website'];
            if (!preg_match("/\b(?:(?:https?|ftp):\/\/|www\.)[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%=~_|]/i", $website)) {
                $websiteErr = "URL Tidak Valid";
            }
        }

        if (!empty($_POST['gender'])) {
            $gender = $_POST['gender'];
        } else {
            $genderErr = "Gender is required";
        }

        if (!empty($_POST['comment'])) {
            $comment =  $_POST['comment'];
        }
    }
    ?>
</head>

<body>
    <h1>PHP Form Validation Example</h1>
    <div class="requerment">* required field</div><br>
    <form action="<?php $_SERVER['PHP_SELF'] ?>" method="POST">
        <label for="nama">Nama :</label>
        <input type="text" name="nama" value="<?= $nama ?>" placeholder="Masukkan Nama">
        <span class="requerment"> * <?= $namaErr ?></span>

        <br><br>

        <label for="email">Email :</label>
        <input type="text" name="email" value="<?= $email ?>" placeholder="Masukkan Email">
        <span class="requerment"> * <?= $emailErr ?></span>

        <br><br>

        <label for="website">Website :</label>
        <input type="text" name="website" placeholder="Masukkan Website" value="<?= $website ?>">
        <span class="requerment"><?= $websiteErr ?></span>

        <br><br>

        <label for="coment">Comment :</label>
        <textarea id="comment" name="comment"><?= $comment ?></textarea>

        <br><br>

        <label for="gender">Gender :</label>
        <input type="radio" name="gender" value="Famale" <?php if (isset($gender) && $gender == 'Famale') echo 'checked'; ?>>Female
        <input type="radio" name="gender" value="Male" <?php if (isset($gender) && $gender == 'Male') echo 'checked'; ?>>Male
        <input type="radio" name="gender" value="Other" <?php if (isset($gender) && $gender == 'Other') echo 'checked'; ?>>Other
        <span class="requerment"> * <?= $genderErr ?></span>

        <br><br>

        <button type="submit" name="kirim">Kirim</button>
    </form>
    <h2>Your Input</h2>
    <?= $nama ?><br>
    <?= $email ?><br>
    <?= $website ?><br>
    <?= $comment ?><br>
    <?= $gender ?><br>
</body>

</html>