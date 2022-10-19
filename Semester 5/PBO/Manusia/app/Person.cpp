/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   Person.cpp
 * Author: LENOVO
 * 
 * Created on September 7, 2022, 10:34 AM
 */

#include <memory>

#include "Person.h"

Person::Person(Person *p) {
    this->name=p->name;
        this->address=p->address;
        cout<<"copy constructor"<<endl;
}

Person::Person(const Person& orig) {
        this->name=orig.name;
        this->address=orig.address;
        cout<<"copy constructor"<<endl;
}

Person::~Person() {
    
    cout<<"virtual function"<<endl;
    
    //delete this;
    
}

void Person::setName(string name){
    this->name=name;
}

void Person::setAddress(string address){
    this->address=address;
}
string Person::getName(){
    return this->name;
}