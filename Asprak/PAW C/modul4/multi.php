<?php
$data = [
    'Array Pertama',
    [
        'Array Kedua',
        ['Array Ketiga']
    ]
];
$data[2] = 'data baru';
$data[1][2] = 'data baru';
$data[1][1][1] = 'data baru';
echo '<pre>';
print_r($data);
echo '<pre>';
