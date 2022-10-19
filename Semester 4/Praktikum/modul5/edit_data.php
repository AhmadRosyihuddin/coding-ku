<?php
include 'function.php';
$nrp = $_GET['nrp'];
if (isset($_POST['edit'])) {
    $edit = edit($nrp, $_POST);
    if ($edit) {
        header("location: index.php?edit=true");
    } else {
        header("location: index.php?edit=false");
    }
}
$data = mysqli_fetch_assoc(mysqli_query($koneksi, "SELECT * FROM tbl_mahasiswa WHERE nrp =$nrp"));
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Inputan</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
</head>

<body>
    <div class="container" style="margin-top:20px">
        <form method="POST">
            <h1 align="center">Form Edit Data</h1>
            <div class="form-group">
                <label for="nama">NRP</label>
                <input type="text" class="form-control" id="nrp" aria-describedby="id" placeholder="Masukkan ID" name="nrp" value="<?= $data['nrp'] ?>">
            </div>  
            <div class="form-group">
                <label for="nama">Nama</label>
                <input type="text" class="form-control" id="nama" aria-describedby="nama" placeholder="Masukkan Nama" name="nama" value="<?= $data['nama'] ?>">
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" class="form-control" id="email" placeholder="Masukkan Email" name="email" value="<?= $data['email'] ?>">
            </div>
            <div class="form-group">
                <label for="alamat">Alamat</label>
                <input type="text" class="form-control" id="alamat" placeholder="Masukkan alamat" name="alamat" value="<?= $data['alamat'] ?>">
            </div>
            <button type=" submit" class="btn btn-primary" name="edit">Submit</button>
            <a href="index.php" class="btn btn-danger">Batal</a>
        </form>
    </div>
</body>

</html>