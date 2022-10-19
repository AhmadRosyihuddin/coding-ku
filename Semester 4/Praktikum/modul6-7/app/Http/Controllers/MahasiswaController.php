<?php

namespace App\Http\Controllers;

use App\Models\Mahasiswa;
use Illuminate\Routing\Controller;
use App\Http\Requests\StoreMahasiswaRequest;
use App\Http\Requests\UpdateMahasiswaRequest;

class MahasiswaController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $mahasiswa = Mahasiswa::all();
        return View('tampilan.index', compact('mahasiswa'), ['title' => 'Home | Modul6-7 Laravel']);
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        return View('tampilan.create', ['title' => 'Tambah Data | Modul6-7 Laravel']);
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \App\Http\Requests\StoreMahasiswaRequest  $request
     * @return \Illuminate\Http\Response
     */
    public function store(StoreMahasiswaRequest $request)
    {
        $request->validate([
            'nrp' => 'required|max:12|unique:mahasiswas',
            'nama' => 'required',
            'email' => 'required|email|unique:mahasiswas',
            'alamat' => 'required|min:5'
        ]);

        Mahasiswa::create($request->all());
        return redirect()->route('home')->withPesan('Data Berhasil Di Tambahkan');
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Models\Mahasiswa  $mahasiswa
     * @return \Illuminate\Http\Response
     */
    public function show(Mahasiswa $mahasiswa)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Models\Mahasiswa  $mahasiswa
     * @return \Illuminate\Http\Response
     */
    public function edit(Mahasiswa $mahasiswa)
    {
        return View('tampilan.edit', compact('mahasiswa'), [
            'title' => 'Edit Data | Modul5 Laravel',
        ]);
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \App\Http\Requests\UpdateMahasiswaRequest  $request
     * @param  \App\Models\Mahasiswa  $mahasiswa
     * @return \Illuminate\Http\Response
     */
    public function update(UpdateMahasiswaRequest $request, Mahasiswa $mahasiswa)
    {
        $rules = [
            'nama' => 'required',
            'alamat' => 'required|min:5'
        ];
        if ($request->nrp != $mahasiswa->nrp) {
            $rules['nrp'] = 'required|max:12|unique:mahasiswas';
        } elseif ($request->email != $mahasiswa->email) {
            $rules['email'] = 'required|email|unique:mahasiswas';
        }

        $validasi = $request->validate($rules);

        $mahasiswa->update($validasi);
        return redirect()->route('home')->withPesan('Data Berhasil Di Edit');
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Models\Mahasiswa  $mahasiswa
     * @return \Illuminate\Http\Response
     */
    public function destroy(Mahasiswa $mahasiswa)
    {
        Mahasiswa::destroy($mahasiswa->nrp);
        return redirect()->route('home')->withPesan('Data Berhasil Di Hapus');
    }
}
