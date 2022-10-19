#ifndef MATAKULIAH_H
#define MATAKULIAH_H
#include <iostream>

using namespace std;
class MataKuliah
{
public:
    string name, code;
    int semester;
    MataKuliah(string name, string code, int semester)
    {
        this->name = name;
        this->code = code;
        this->semester = semester;
    }
};
#endif