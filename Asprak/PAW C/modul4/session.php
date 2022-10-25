<?php
session_start();
// session_unset();
session_destroy();
// $_SESSION['buatSession'] = 'session baru';
echo '<pre>';
print_r($_SESSION);
echo '<pre>';
// echo $_SESSION['buatSession'];
// echo session_save_path();
