<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\tbl_tukang>
 */
class TblTukangFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition()
    {
        return [
            'IDTUKANG' => $this->faker->uuid(),
            'NAMATUKAG' => $this->faker->name()
        ];
    }
}
