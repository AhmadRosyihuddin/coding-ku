<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('tbl_inventories', function (Blueprint $table) {
            $table->string('IDINVENTORY', 5)->primary();
            $table->string('IDTUKANG', 5);
            $table->date('TANGGAL');
            $table->string('STATUS', 3);
            $table->timestamps();
            $table->foreign('IDTUKANG')->references('IDTUKANG')->on('tbl_tukangs')->onDelete('cascade')->onUpdate('cascade');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('tbl_inventories');
    }
};
