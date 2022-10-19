/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: LENOVO
 *
 * Created on September 6, 2022, 10:48 PM
 */

#include <cstdlib>
#include <sstream>
#include <stdio.h>

#include "Manusia.h"
#include "Student.h"
#include "../Manusia/app/Person.h"
#include "Khs.h"
#include "Mahasiswa.h"

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
/**
    Manusia *adi= new Manusia("Adi Wibisono","Surabaya", 20);
    
    cout<<"Name:"<<adi->getName()<<adi->getAge()<<endl;
    cout<<"Address: "<<adi->getAddress()<<endl;
    cout<<"age: "<<adi->getAge()<<endl;
    
    Student *budi = new Student();
    cout<<"Student Name: "<<budi->getName()<<endl;
    cout<<"Student Address: "<<budi->getAddress()<<endl;
    
    budi = new Student("Budi darmawan", "SUrabaya", 20);
    cout<<"Student Name: "<<budi->getName()<<endl;
    cout<<"Student Address: "<<budi->getAddress()<<endl;
    
    Student *hani = new Student("Hani Ardila", "Pamekasan", 20);
    cout<<"Student Name: "<<hani->getName()<<endl;
    cout<<"Student Address: "<<hani->getAddress()<<endl;
    
    
    Students *listStudent = new Students();
    listStudent->setStudent(budi);
    cout<<"Student Name: "<<listStudent->getStudent(0)->getName()<<endl;
    cout<<"Student Address: "<<listStudent->getStudent(0)->getAddress()<<endl;
    
    Student *eko = new Student(budi);
    eko->print();
    
    listStudent->setStudent(eko);
    listStudent->setStudent(budi);
    listStudent->setStudent(hani);
    listStudent->setStudent(eko);
    listStudent->setStudent(budi);
    listStudent->setStudent(hani);
    listStudent->setStudent(eko);
    listStudent->setStudent(budi);
    listStudent->setStudent(hani);
    listStudent->setStudent(eko);
    listStudent->setStudent(budi);
    listStudent->setStudent(hani);
    
    listStudent->print();
        
    
    Person p;
    Person *s;    
    s=&p; //reference
    Person *r;
    r=&p;
    cout<<"first"<<r->getName()<<endl; ////dereference
    cout<<"first"<<p.getName()<<endl; 
    cout<<"first"<<s->getName()<<endl; 
    
    p.setName("jono");
    p.setAddress("sidoarjo");
    cout<<"second"<<r->getName()<<endl;
    cout<<"second"<<p.getName()<<endl; 
    cout<<"second"<<s->getName()<<endl;

    r=new Person(p);
    r->setName("satu");
    cout<<r->getName()<<endl;
    p.setName("jono");
    p.setAddress("sidoarjo");
    cout<<r->getName()<<endl;
    
    
**/    
//    if(r!=NULL) delete r;
//    if(s!=NULL) delete s;
   
    Khs *khs=new Khs();
    Mahasiswa *mhs=new Mahasiswa();
    mhs->setName("ADI");
    mhs->setNim("012001");
    mhs->print();
    
    mhs->setKhs(khs);
    khs=new Khs("SD","B");
    mhs->setKhs(khs);
    khs=new Khs("ALPRO","C");
    mhs->setKhs(khs);
    mhs->printKhs();
    
    
    mhs=new Mahasiswa();
    mhs->setName("BADU");
    mhs->setNim("022002");
    mhs->print();
    mhs->setKhs(khs);
    khs=new Khs("SD","A");
    mhs->setKhs(khs);
    khs=new Khs("ALPRO","B");
    mhs->setKhs(khs);
    mhs->printKhs();
        
    mhs=new Mahasiswa();
    mhs->setName("CACA");
    mhs->setNim("022020");
    mhs->print();
    mhs->setKhs(khs);
    khs=new Khs("SD","A");
    mhs->setKhs(khs);
    khs=new Khs("ALPRO","B");
    mhs->setKhs(khs);
    mhs->printKhs();
    return 0;
}

