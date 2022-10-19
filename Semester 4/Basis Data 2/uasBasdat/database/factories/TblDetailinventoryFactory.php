<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\tbl_detailinventory>
 */
class TblDetailinventoryFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition()
    {
        return [
            'IDBARANG' => $this->faker->numberBetween(1, 100),
            'NAMABARANG' => $this->faker->word(),
            'STOCK' => 10,
        ];
    }
}
