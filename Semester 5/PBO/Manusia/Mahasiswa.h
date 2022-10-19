/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   Mahasiswa.h
 * Author: LENOVO
 *
 * Created on September 19, 2022, 10:07 AM
 */

#ifndef MAHASISWA_H
#define MAHASISWA_H
#include<iostream>
#include"Khs.h"
using namespace std;

class Mahasiswa {
public:
    Mahasiswa();
//    explicit Mahasiswa(string no="01",string nama="Mahasiswa");;
    Mahasiswa(const Mahasiswa& orig);
    virtual ~Mahasiswa();
    void setKhs(Khs *khs);
    void printKhs();
    void print();
    Khs *getKhs();
    string getName();
    string getNim();
    void setName(string n);
    void setNim(string n);
    void setCounter();
    int getCounter();
    int counter;
    //friend class Khs;
    
private:
    string nim;
    string name;
    Khs *khs[];
    
    
};

#endif /* MAHASISWA_H */

