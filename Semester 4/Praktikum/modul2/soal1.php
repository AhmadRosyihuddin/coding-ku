<?php
function jumlah($x, $y)
{
    return "Jumlah x + y : " . $x + $y;
}
function kali($x, $y)
{
    return "Jumlah x * y : " . $x * $y;
}
function bagi($x, $y)
{
    return "Jumlah x / y : " . $x / $y;
}
echo "<br>Pemanggilan Fungsi Jumlah()<br>" . jumlah(6, 6);
echo "<br>Pemanggilan Fungsi Jumlah()<br>" . jumlah(8, 8);
echo "<br>Pemanggilan Fungsi Jumlah()<br>" . jumlah(4, 3);

echo "<br>";
echo "<br>Pemanggilan Fungsi kali()<br>" . kali(17, 5);
echo "<br>Pemanggilan Fungsi kali()<br>" . kali(405, 1);
echo "<br>Pemanggilan Fungsi kali()<br>" . kali(675, 1);

echo "<br>";
echo "<br>Pemanggilan Fungsi bagi()<br>" . bagi(2, 3);
echo "<br>Pemanggilan Fungsi bagi()<br>" . bagi(22, 9);
echo "<br>Pemanggilan Fungsi bagi()<br>" . bagi(17, 9);
?>