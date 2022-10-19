<?php
session_start();
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if (isset($_POST['ingat'])) {
        $_SESSION['login'] = True;
        header('Location: home.php');
    }
}

if (isset($_SESSION['login'])) {
    header('location: home.php');
}
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <style>
        .input {
            width: 220px;
            height: 35px;
            padding-left: 15px;
            margin-top: 5px;
            margin-bottom: 5px;
        }

        .submit {
            width: 100%;
            height: 35px;
            background-color: #37b837;
            border: none;
            color: white;
        }

        .lebel {
            font-family: sans-serif;
            font-weight: bold;
            font-size: 20px;
        }
    </style>
</head>

<body style="padding: 150px;">
    <table align="center">
        <form action="<?= $_SERVER['PHP_SELF'] ?>" method="POST">
            <tr>
                <td><label for="username" class="lebel">Username :</label></td>
            </tr>
            <tr>
                <td><input type="text" class="input" name="username" placeholder="Enter Username"></td>

            </tr>
            <tr>
                <td><label for="password" class="lebel">Password :</label></td>
            </tr>
            <tr>
                <td><input type="password" class="input" name="password" placeholder="Enter Password"></td>
            </tr>
            <tr>
                <td><input type="submit" class="submit" value="Login"></td>
            </tr>
            <tr>
                <td><input type="checkbox" name="ingat">Remember Me</td>
            </tr>
        </form>
    </table>
</body>

</html>