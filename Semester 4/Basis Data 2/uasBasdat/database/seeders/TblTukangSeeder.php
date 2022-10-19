<?php

namespace Database\Seeders;

use App\Models\tbl_tukang;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class TblTukangSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        Tbl_tukang::create([
            'IDTUKANG' => 1,
            'NAMATUKANG' => 'Yoga'
        ]);
        Tbl_tukang::create([
            'IDTUKANG' => 2,
            'NAMATUKANG' => 'Fanani'
        ]);
        Tbl_tukang::create([
            'IDTUKANG' => 3,
            'NAMATUKANG' => 'Teguh'
        ]);
        Tbl_tukang::create([
            'IDTUKANG' => 4,
            'NAMATUKANG' => 'Nico'
        ]);
        Tbl_tukang::create([
            'IDTUKANG' => 5,
            'NAMATUKANG' => 'Fiqri'
        ]);
        Tbl_tukang::create([
            'IDTUKANG' => 6,
            'NAMATUKANG' => 'Nizam'
        ]);
    }
}
