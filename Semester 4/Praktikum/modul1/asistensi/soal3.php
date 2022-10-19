<?php
$y = "Variabel Global";
function nomor3(){
    Global $y;
    $x="Variabel Local";
    echo $x."<br>";
    echo $y;
}
nomor3();

?>