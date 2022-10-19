/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   Mahasiswa.cpp
 * Author: LENOVO
 * 
 * Created on September 19, 2022, 10:07 AM
 */

#include "Mahasiswa.h"

Mahasiswa::Mahasiswa(){
    this->counter=0;
}
Mahasiswa::Mahasiswa(const Mahasiswa& orig) {
    this->nim=orig.nim;
    this->name=orig.name;
}

Mahasiswa::~Mahasiswa() {
    cout<<"virtual";
    //delete this;
}


string Mahasiswa::getName(){
    return this->name;
}

string Mahasiswa::getNim(){
    return this->nim;
}

void Mahasiswa::setKhs(Khs *vkhs){
    this->khs[getCounter()]=vkhs;
    this->setCounter();
}

void Mahasiswa::setCounter(){
    this->counter+=1;
}
void Mahasiswa::setName( string n){
    this->name=n;
    
}
void Mahasiswa::setNim( string n){
    this->nim=n;
    
}
int Mahasiswa::getCounter(){
    return this->counter;
}

void Mahasiswa::print(){
    cout<<"========================================"<<endl;
    cout<<"NIM:"<<this->getNim()<<endl;
    cout<<"NAMA:"<<this->getName()<<endl;
}

void Mahasiswa::printKhs(){
    cout<<"========================================"<<endl;
    cout<<"KHS:"<<this->getCounter()<<" Mata Kuliah"<<endl;
    cout<<"----------------------------------------"<<endl;
    for (int i=0;i<this->getCounter();i++) {
            cout<<i+1<<". Mata Kuliah: "<<this->khs[i]->course<<endl;           
            cout<<"Nilai: "<<this->khs[i]->grade<<endl;
        }  
    cout<<"----------------------------------------\n"<<endl;
}




