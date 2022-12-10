<?php

namespace App\Http\Controllers;

use App\Models\Tbl_Mahasiswa;
use App\Http\Requests\StoreTbl_MahasiswaRequest;
use App\Http\Requests\UpdateTbl_MahasiswaRequest;

class TblMahasiswaController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        //
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \App\Http\Requests\StoreTbl_MahasiswaRequest  $request
     * @return \Illuminate\Http\Response
     */
    public function store(StoreTbl_MahasiswaRequest $request)
    {
        //
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Models\Tbl_Mahasiswa  $tbl_Mahasiswa
     * @return \Illuminate\Http\Response
     */
    public function show(Tbl_Mahasiswa $tbl_Mahasiswa)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Models\Tbl_Mahasiswa  $tbl_Mahasiswa
     * @return \Illuminate\Http\Response
     */
    public function edit(Tbl_Mahasiswa $tbl_Mahasiswa)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \App\Http\Requests\UpdateTbl_MahasiswaRequest  $request
     * @param  \App\Models\Tbl_Mahasiswa  $tbl_Mahasiswa
     * @return \Illuminate\Http\Response
     */
    public function update(UpdateTbl_MahasiswaRequest $request, Tbl_Mahasiswa $tbl_Mahasiswa)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Models\Tbl_Mahasiswa  $tbl_Mahasiswa
     * @return \Illuminate\Http\Response
     */
    public function destroy(Tbl_Mahasiswa $tbl_Mahasiswa)
    {
        //
    }
}
