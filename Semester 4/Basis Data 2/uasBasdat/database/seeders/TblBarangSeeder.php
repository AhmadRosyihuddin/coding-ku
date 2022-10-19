<?php

namespace Database\Seeders;

use App\Models\tbl_barang;
use App\Models\Tbl_barang as ModelsTbl_barang;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class TblBarangSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        Tbl_barang::create([
            'IDBARANG' => 1,
            'NAMABARANG' => 'Tas',
            'STOCK' => 10,
        ]);
        Tbl_barang::create([
            'IDBARANG' => 2,
            'NAMABARANG' => 'Dompet',
            'STOCK' => 10,
        ]);
        Tbl_barang::create([
            'IDBARANG' => 3,
            'NAMABARANG' => 'Sepatu',
            'STOCK' => 10,
        ]);
        Tbl_barang::create([
            'IDBARANG' => 4,
            'NAMABARANG' => 'Gelang',
            'STOCK' => 10,
        ]);
        Tbl_barang::create([
            'IDBARANG' => 5,
            'NAMABARANG' => 'Jam Tangan',
            'STOCK' => 10,
        ]);
        Tbl_barang::create([
            'IDBARANG' => 6,
            'NAMABARANG' => 'Handphone',
            'STOCK' => 10,
        ]);
    }
}
