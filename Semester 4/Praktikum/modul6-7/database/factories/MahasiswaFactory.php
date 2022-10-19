<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\Mahasiswa>
 */
class MahasiswaFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition()
    {
        return [
            'nrp' => $this->faker->randomNumber(8),
            'nama' => $this->faker->name(),
            'email' => $this->faker->safeEmail(),
            'alamat' => $this->faker->streetAddress()
        ];
    }
}
