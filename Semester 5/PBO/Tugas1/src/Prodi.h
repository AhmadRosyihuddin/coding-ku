#ifndef PRODI_H
#define PRODI_H
#include "Mahasiswa.h"
#include <iostream>
class Prodi
{
public:
    Mahasiswa *mahasiswa;
    string name, code;
    Prodi(string name, string code, Mahasiswa *mahasiswa)
    {
        this->name = name;
        this->code = code;
        this->mahasiswa = mahasiswa;
    }
    void display()
    {
        cout << "Nama Mahasiswa : " << mahasiswa->name << endl;
        cout << "Alamat : " << mahasiswa->address << endl;
        cout << "Nama Prodi : " << name << endl;
        cout << "Kode Prodi : " << code << endl;
        cout << "Semester : " << mahasiswa->semester << endl;
        cout << "Mata Kuliah : " << mahasiswa->khs->mataKuliah->name << endl;
        cout << "Nilai : " << mahasiswa->khs->nilai << endl;
    }
};
#endif