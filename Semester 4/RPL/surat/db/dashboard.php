<?php
include "../connect/koneksi.php";
$tb_pengajuan = mysqli_query($koneksi,"SELECT * FROM tb_user INNER JOIN tb_pengajuan  INNER JOIN tb_surat ON tb_pengajuan.kode_surat=tb_surat.kode_surat AND tb_user.nik=tb_pengajuan.nik_user");
while ($row = mysqli_fetch_assoc($tb_pengajuan)):
    if($row["status_pengajuan"]=="Menunggu"){?>
        <tr>
            <td><?= $row["nik_user"] ?></td>
            <td><?= $row["nama"] ?></td>
            <td><?= $row["kode_surat"] ?></td>
            <td><?= $row["jenis_surat"] ?></td>
            <td><?= $row["waktu_pengajuan"] ?></td>
            <td><?= $row["keperluan"] ?></td>
            <?php
            if($row["kode_surat"]=="SKTM"){?>
                <td>
                    <a href="../data_input/data_sktm.php?id_pengajuan=<?= $row['id_pengajuan']?>">View Data</a>
                </td>
            <?php }elseif($row["kode_surat"]=="SKK"){?>
                <td>
                    <a href="../data_input/data_skk.php?id_pengajuan=<?= $row['id_pengajuan']?>">View Data</a>
                </td>
            <?php }elseif($row["kode_surat"]=="SKM"){?>
                <td>
                    <a href="../data_input/data_skm.php?id_pengajuan=<?= $row['id_pengajuan']?>">View Data</a>
                </td>
            <?php }elseif($row["kode_surat"]=="SL"){?>
                <td>
                    <a href="../data_input/data_sl.php?id_pengajuan=<?= $row['id_pengajuan']?>">View Data</a>
                </td>
            <?php }elseif($row["kode_surat"]=="SPA"){?>
                <td>
                    <a href="../data_input/data_spa.php?id_pengajuan=<?= $row['id_pengajuan']?>">View Data</a>
                </td>
            <?php }elseif($row["kode_surat"]=="SPK"){?>
                <td>
                    <a href="../data_input/data_spk.php?id_pengajuan=<?= $row['id_pengajuan']?>">View Data</a>
                </td>
            <?php }?>

            <td>
                <a href="../update_data/terima_pengajuan.php?id_pengajuan=<?= $row["id_pengajuan"]?>&kode_surat=<?= $row["kode_surat"]?>&nik_user=<?= $row["nik_user"]?>"><button type="button" class="btn btn-primary" style="margin-bottom: 10px;">Terima</button></a>
                <a href="../update_data/tolak_pengajuan.php?id_pengajuan=<?= $row["id_pengajuan"]?>&kode_surat=<?= $row["kode_surat"]?>&nik_user=<?= $row["nik_user"]?>"><button type="button" class="btn btn-danger">Tolak</button></a>
            </td>
        </tr>
    <?php
    }
endwhile; 
?>