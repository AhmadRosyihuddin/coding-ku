<?php

use App\Http\Controllers\HomeController;
use App\Http\Controllers\MahasiswaController;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', [MahasiswaController::class, 'index'])->name('home');
Route::get('/create', [MahasiswaController::class, 'create'])->name('create.form');
Route::post('/create', [MahasiswaController::class, 'store'])->name('create.proses');
Route::delete('/{mahasiswa:nrp}', [MahasiswaController::class, 'destroy'])->name('hapus.data');
Route::get('/{mahasiswa:nrp}/edit', [MahasiswaController::class, 'edit'])->name('edit.form');
Route::put('/{mahasiswa:nrp}/edit', [MahasiswaController::class, 'update'])->name('edit.proses');
