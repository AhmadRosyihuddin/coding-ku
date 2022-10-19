/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   Manusia.h
 * Author: LENOVO
 *
 * Created on September 6, 2022, 10:48 PM
 */

#ifndef MANUSIA_H
#define MANUSIA_H
#include <iostream>
using namespace std;

class Manusia {
 
  private:
   string name;
   string address;
   int age;
 
  public:  
      
    Manusia(string name, string address, int age){
        this->name=name;
        this->address=address;
        this->age=age;
      }
    void setName(string var){
        name=var;
    }
    void setAddress(string var){
        address=var;
    }
    void setAge(int var){
        age=var;
    }

    string getName(){
        return this->name;
    }
    string getAddress(){
        return this->address;
    }
    int getAge(){
        return this->age;
    }
};

#endif /* MANUSIA_H */

