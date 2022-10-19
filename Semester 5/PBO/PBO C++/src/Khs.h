#ifndef KHS_H
#define KHS_H
#include <iostream>
#include <vector>
#include "MataKuliah.h"
class Khs
{
public:
    vector<MataKuliah> mataKuliah;
    string student;
    Khs();
    Khs(string student, MataKuliah mk)
    {
        this->student = student;
        this->mataKuliah.push_back(mk);
    }

    void addMk(MataKuliah mk)
    {
        this->mataKuliah.push_back(mk);
    }
    // int display()
    // {
    //     for (MataKuliah mk : mataKuliah)
    //     {
    //         cout << "\t\t\t " << mk.name;
    //     };
    //     return 0;
    // }
};
#endif