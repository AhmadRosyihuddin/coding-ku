/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   Person.h
 * Author: LENOVO
 *
 * Created on September 7, 2022, 10:34 AM
 */

#ifndef PERSON_H
#define PERSON_H

#include <iostream>

using namespace std;

class Person {
public:
    Person(Person *p);
    Person(const Person& orig);
    explicit Person(string name="Mahasiswa", string alamat="Trunojoyo", int nilai=90):name(name),address(alamat),grade(nilai){};
    virtual ~Person();
    void setName(string name);
    void setAddress(string address);
    string getName();
    string getAddress();
private:
    string name;
    string address;
    int grade;

};

#endif /* PERSON_H */

