/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   Student.h
 * Author: LENOVO
 *
 * Created on September 7, 2022, 12:58 AM
 */

#ifndef STUDENT_H
#define STUDENT_H

#include<iostream>

using namespace std;

class Student {
public:
    Student(Student *s);
    explicit Student(string name="Mahasiswa", string alamat="Trunojoyo", int age=18):name(name),address(alamat),age(age){};
    string getName();
    string getAddress();
    int getAge();
    void setName(string name);
    void setAddress(string address);
    void setAge(int age);
    void print();
    
private:
    string name;
    string address;
    int age;
};

class Students{
private:
    int counter;
    Student *students[];
    Student Arrstudents[];
public:
    
    Student *getStudent(int i){
        return students[i];       
    }
    Student getArrStudent(int i){
        return Arrstudents[i];       
    }
    void setStudent(Student *s){
        students[counter]=s;
        counter++;
    }
    void setArrStudent(Student s){
        Arrstudents[counter]=s;
        counter++;
    }
    void print(){
        int i=0;
        for (int i=0;i<counter;i++) {
            cout<<"NO."<<i<<endl;
            cout<<"p Address:"<<&this->students[i]<<endl;
            this->getStudent(i)->print();            
        }        
    }
};

#endif /* STUDENT_H */

