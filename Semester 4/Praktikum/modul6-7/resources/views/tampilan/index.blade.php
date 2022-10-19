@extends('layouts.main')
@section('container')
<div class="container-home" style="margin: 50px">
    @if (session()->has('pesan'))
    <div class="alert alert-success alert-dismissible fade show" role="alert">
        <strong>Berhasil</strong> {{ Session::get('pesan') }}
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
        </button>
    </div>
    @endif
    <h1>Data Mahasiswa</h1>
    <table class="table table-striped">
        <thead>
            <tr>
                <th scope="col">NO</th>
                <th scope="col">nrp</th>
                <th scope="col">Nama</th>
                <th scope="col">Email</th>
                <th scope="col">Alamat</th>
                <th scope="col">Opsi</th>
            </tr>
        </thead>
        <tbody>
            @php $no = 1 @endphp
            @foreach ($mahasiswa as $row )
            <tr>    
                <th scope="row">{{ $no++ }}</th>
                <td>{{ $row->nrp }}</td>
                <td>{{ $row->nama }}</td>
                <td>{{ $row->email }}</td>
                <td>{{ $row->alamat }}</td>
                <td>
                    <a class="btn btn-primary" href="/{{ $row->nrp }}/edit" role="button">Edit</a>
                    {{-- <a class="btn btn-danger" href="/{{ $row->id }}" role="button">Hapus</a> --}}
                    <form action="/{{ $row->nrp }}" method="POST" class="d-inline">
                        @csrf
                        @method('delete')
                        <button class="btn btn-danger">Hapus</button>
                    </form>

                </td>
            </tr>
            @endforeach
        </tbody>
    </table>
</div>
@endsection
