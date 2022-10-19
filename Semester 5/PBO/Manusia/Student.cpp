/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   Student.cpp
 * Author: LENOVO
 * 
 * Created on September 7, 2022, 12:58 AM
 */

#include "Student.h"



Student::Student(Student *s){
    this->name=s->name;
    this->address=s->address;
    this->age=s->age;
}

string Student::getName(){
    return this->name;
}

string Student::getAddress(){
    return this->address;
}
int Student::getAge(){
    return this->age;
}

void Student::print(){
    cout<<"++++++++++++++++++++++++++++++++"<<endl;
    cout<<"Student Name: "<<this->getName()<<endl;
    cout<<"Student Address: "<<this->getAddress()<<endl;
    cout<<"Student Age: "<<this->getAge()<<endl;    
}

