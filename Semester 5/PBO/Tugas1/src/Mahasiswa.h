#ifndef MAHASISWA_H
#define MAHASISWA_H
#include <iostream>
#include "Khs.h"
using namespace std;
class Mahasiswa
{
public:
    Khs *khs;
    string name, address;
    int semester;
    Mahasiswa(string name, string address, int semester, Khs *khs)
    {
        this->name = name;
        this->address = address;
        this->semester = semester;
        this->khs = khs;
    }
    void display()
    {
        cout << "Nama : " << name << endl;
        cout << "Alamat : " << address << endl;
        cout << "Semester : " << semester << endl;
        cout << "Mata Kuliah : " << khs->mataKuliah->name << endl;
        cout << "Nilai : " << khs->nilai << endl;
    }
};
#endif