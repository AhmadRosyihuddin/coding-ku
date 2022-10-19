@extends('layouts.main')
@section('container')
<div class=" col-lg-12">
    <h2>Tambah Data</h2>
    <form method="POST" action="/create">
        @csrf
        <div class="form-group">
            <label for="nrp">NRP</label>
            <input type="text" class="form-control @error('nrp') is-invalid @enderror" name="nrp" id="nrp"
                aria-describedby="emailHelp" placeholder="Masukkan NRP" value="{{ Old('nrp') }}">
        </div>
        <div class="form-group">
            <label for="nama">Nama</label>
            <input type="text" class="form-control @error('nama') is-invalid @enderror" name="nama" id="nama"
                placeholder="Masukkan Nama" value="{{ old('nama') }}">
        </div>
        <div class="form-group">
            <label for="email">Email</label>
            <input type="text" class="form-control @error('email') is-invalid @enderror" name="email" id="email"
                placeholder="Masukkan Email" value="{{ old('email') }}">
        </div>
        <div class="form-group">
            <label for="alamat">Alamat</label>
            <input type="text" class="form-control @error('alamat') is-invalid @enderror" name="alamat" id="alamat"
                placeholder="Masukkan Alamat" value="{{ old('alamat') }}">
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</div>
@endsection
