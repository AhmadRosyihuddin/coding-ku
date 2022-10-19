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
        Schema::create('tbl_detailinventories', function (Blueprint $table) {
            $table->string('IDBARANG', 5);
            $table->string('IDINVENTORY', 5);
            $table->integer('QUANTITTY');
            $table->timestamps();
            $table->foreign('IDINVENTORY')->references('IDINVENTORY')->on('tbl_inventories')->onDelete('cascade')->onUpdate('cascade');
            $table->foreign('IDBARANG')->references('IDBARANG')->on('tbl_barangs')->onDelete('cascade')->onUpdate('cascade');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('tbl_detailinventories');
    }
};
