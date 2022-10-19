<?php
// mengkoneksikan ke database
$koneksi = mysqli_connect('localhost', 'root', '', 'modul5PAW');
// if ($koneksi) {
//     echo "Koneksi Berhasil";
// } else {
//     echo "Koneksi Gagal";
// }

//fungsion select
function select($query)
{
    global $koneksi; // membuat variabel koneksi mennjadi global
    $data = mysqli_query($koneksi, $query);
    $rows = []; // menyimpan semua data ke dalam array
    while ($row = mysqli_fetch_assoc($data)) {
        $rows[] = $row;
    }
    return $rows;
}

// function delete data
function delete($nrp)
{
    global $koneksi; // membuat variabel koneksi mennjadi global
    $data = mysqli_query($koneksi, "DElETE FROM tbl_mahasiswa WHERE nrp=$nrp");

    return mysqli_affected_rows($koneksi);
}

// function untuk menambahkan data ke tabel
function tambahData($value)
{
    global $koneksi; // membuat variabel koneksi mennjadi global
    $nrp = $value['nrp'];
    $nama = $value['nama'];
    $email = $value['email'];
    $alamat = $value['alamat'];
    if (mysqli_num_rows(mysqli_query($koneksi, "SELECT nrp FROM tbl_mahasiswa WHERE nrp = '$nrp'"))) {
        return false;
    } else {
        $tambah = mysqli_query($koneksi, "INSERT INTO tbl_mahasiswa(nrp, nama, email, alamat) VALUES('$nrp', '$nama', '$email', '$alamat')");
        return $tambah;
    }
}

// function untuk merubah/edit data
function edit($OldNrp, $value)
{
    global $koneksi; // membuat variabel koneksi mennjadi globa
    $newNrp = $value['nrp'];
    $nama = $value['nama'];
    $email = $value['email'];
    $alamat = $value['alamat'];
    if (!mysqli_num_rows(mysqli_query($koneksi, "SELECT nrp FROM tbl_mahasiswa WHERE nrp = '$newNrp'")) || $newNrp == $OldNrp) {
        $update = mysqli_query($koneksi, "UPDATE tbl_mahasiswa SET nrp=$newNrp, nama='$nama', email='$email', alamat='$alamat' WHERE nrp = '$OldNrp'");
        return $update;
    } else {
        return False;
    }
}
