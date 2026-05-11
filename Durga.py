# print("This is my first programming language")
# #print("This is my first programming language")
# #single line or in line comment
# '''triple comment or multi line comment
# '''
# '''print("This is my first programming language")
# '''
# hemanth=30
# print(hemanth)
# nagaDurga=78
# NagaDurga=79
# naga_durga=90
# print(nagaDurga)
# print(NagaDurga)
# print(naga_durga)
# a=67
# print(a)
# print(id(a))#adress of a variable
# print(type(a))
# #simple interest
# p=70989
# t=8
# r=3
# d=p*t*r/100
# print(d)
# a=78
# b=89
# c=(a+b)**2
# print(c)
# if 2<1:
#     print("this is java")
# elif 2<1:
#     print("this is c++")
# else:
#     print("this is python")
# print("this is if") if 2>1 else print("this is else")
# #loop statements
# #while False:
#         #print("this is loops")
# thirumala=20
# while thirumala<40:
#     print("this is while",thirumala)
#     thirumala+=1
# for i in range(1,100,3):
#     print(i)
# # user="durga"
# # password="naga123"
# # user_name=input("enter the user")
# # pass_word=input("enter the password")
# # if user==user_name and password==pass_word:
# #     print("success")
# # else:
# #     print("try again")
# #list methods
# krishna=[1,2,3,4,4] #or krishna1=list([1,23,34,56])
# print(krishna)
# a=79
# if a%2!=0:
#     print("odd")
# else:
#     print("even")
#Dictionaries
# sunny={1:"names","sno":2.2,11:True}
# print(type(sunny))
# sunny={1:"names","sno":2.2,11:True}
# print(sunny[1])
# sunny={"kiran":"names","sno":2.2,11:True}
# sunny["kiran"]="python"
# print(sunny)
#get method
#aswini={"sno":1,"name":"sunny","phone":[12,32]}
# print(aswini.get("sno"))
# print(aswini.keys())
# print(aswini.values())
# print(aswini.items())
# aswini={"sno":1,"name":"sunny","phone":[12,32]}
# aswini.update({"food":"biryani"})
# print(aswini)
# aswini={"sno":1,"name":"sunny","phone":[12,32]}
# aswini.pop("name")
# print(aswini)
#nested dictionary(dictionary within dictionary)
# phani={
#     1:"a",
#     2:"b",
#     3:{1:"aa"},
# }
# print(phani[3][1])
#tuples
# mohan=(1,2,3,4,543)
# print(type(mohan))
#tuple operations (builtin methods) not only for tuple for everything common
# mohan=(1,22,2,232.33)
# print(max(mohan))
# print(min(mohan))
# print(sum(mohan))
# print(len(mohan))
#print(list(mohan))
#a small progarm
#Atm
# s='''
#     1.credit
#     2.debit
#     3.mini statement
#     4.exit
# '''
# Amount=1000
# name="kiran"
# password="123"
# user_name=input("enter the user name:")
# pass_word=input("enter the password:")
# if user_name==name and pass_word==password:
#     print(s)
#     option=int(input("enter the option:"))
#     if option==1:
#         credit_amount=float(input("enter the Amount:"))
#         print("Amount after credit:",Amount+credit_amount)
# else:
#     print("incorrect")
#sets and functions
#sunny={2,2,3,212,232,1232}
# print(sunny)   #unodered and unindexed o/p will be not in same order as i/p
#sunny.add(123)
#print(sunny) # value added still unordered and revomed duplicate 2
#sunny.update({1,2,3})
#print(sunny) # if you want to add one value then use "add" or you want to add more values then use "update"
#sunny.remove(3)# if you want to remove a particular element then use remove
#sunny.pop() #if you want to remove a random element then use pop
#sunny.clear()
#sandeep=sunny.copy()
#print(sandeep)
# Set operations
#union(all elements)i.e,(+)
# set1={1,2,3,4,5}
# set2={5,6,7,8,4}
# print(set1.union(set2))  #if set 1 and 2 have same numbers then this union function will remove those duplicate keys and give unordered set in output
#Intersection(only common elemets) i.e, (-)
# set1={1,2,3,4,5}
# set2={56,7,8,4,4}
#print(set1.intersection(set2))   # print only common elements in set 1 amd set 2
#print(set1.difference(set2))
# Symmetric difference -- is opposite of intersection
#print(set1.symmetric_difference(set2))
#Disjoint set --- different sets --- no common elements
# set1={1,2,3,4}
# set2={5,6,7,8}
# print(set1.isdisjoint(set2))
#Subset
# set1={1,2,3}
# set2={1,2,3}
# print(set1.issubset(set2))
# print(set2.issuperset(set1)) opp to issubset
#frozen set --- not able to make changes in that set
                                                     #*****notes completed****#



#Functions and advanced functions
#Function-- a block of code , it executes by call#syntax
# def Suresh(a,v,b):
#     print("this is function",a,v,b)
# Suresh(100,34,56)# function call
#single parameter function and multiple parameter
#we can reuse the code by function instesd of writing the code again
# def Suresh(a,b):
#     print(a+b)
# while True:
#     Suresh(10,33)
# def lakshmi(name):
#     print("hii",name)
# n=input("enter the name")
# lakshmi(n)
#orbitary parameters
# def lakshmi(*name):
#     print("hii",name)
# lakshmi(1,2,3,44,5,5,6)# if you give * then it will take in the form of tuple
#key word arguments 
# def lakshmi(**name):
#     print("hii",name)
# lakshmi(name="ram",age=25)#data stored in dictonary form
#nested function
# def outer_function():
#     print("this is outer function")
#     def inner_function():
#         print("this is inner function")
#     inner_function()
# outer_function()
#Module-- Collection of functions is called module
# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)
# #import key word only in python no export
# from Durga import* # importing one function fro one file
# add (1,5)
#Lambda Function
# x=lambda a,b,c : a+b+c # lambda is a key word consists of n no of arguments and only one expression
# print(x(5,2,1))
#filtered 
#Map
#reduce
#why we use return insted of print
#break point in de bug file
#file handling
# file=open("dema.txt",mode="r")
# c=file.readlines()
# print(c)
# file.close()
# file=open("dema.txt",mode="w")
# c=file.write("this is my write function")
# file.close()
# file=open("dema.txt",mode="a")
# c=file.write("this is my append function")
# file.close()
# #Reading file in 'r+ mode:
# with open ('demo.txt','r+') as fd:
#     print(fd.tell())
#     print(fd.read())
#     print(fd.tell())
#     c=fd.write("this is w+")
#file methods
#read , readline, read lines, write, writelines, close, seek, tell
#opening file 
# fp= open ('demo.txt', "r")
# print(fp.tell())
# fp.read(2)
# print the position of handle
# print(fp.tell())
# fp.seek(0)
# print(fp.tell())
#closing file
#fp.close()
#error types:
#Python Errors (Correct & Simple Explanation)
# 1️ AttributeError
# Object lo leni attribute access chesthe
# x = 10
# x.append(5)   # error
# 2️ EOFError
#  Input adigina appudu data lekapothe
# Example:
# File end ayipothe
# input miss ayithe
# 3️ IOError (now mostly OSError)
#  File open/read/write fail ayithe
# open("wrongfile.txt")
# 4️ IndexError
#  List lo wrong index access chesthe
# a = [1,2,3]
# print(a[5])
# 5️ KeyError
#  Dictionary lo key lekunte
# d = {"a":1}
# print(d["b"])
# 6️ KeyboardInterrupt
#  User Ctrl + C press chesthe
# 7️ NameError
#  Variable define cheyyakunda use chesthe
# print(x)
# 8️ StopIteration
#  Loop / iterator aipothe
# 9️ TypeError
#  Wrong type use chesthe
# "5" + 5
#  ZeroDivisionError ⚠️ (IMPORTANT correction)
#  Your notes lo wrong meaning undi
# Correct meaning:
#  0 tho divide chesthe error
# 5 / 0
# ValueError (simple ga)
#ValueError = correct type untundi, kani value wrong untundi
#Easy example:
# int("abc")
#Error: ValueError
#Why?
#"abc" → string ✔️
#kani number ga convert avvadu ❌
#One line meaning:
# ValueError = wrong value for correct operation
#try , except, else
#OOps concepts
# class Karthik(): #class definition
#     def Output(self):
#         print("thius is class")
# #object name= class name() object creation
# vivo=Karthik()
# vivo.Output() #methods access object name.method
# class Shiva():
#     a=10
#     def show(self):
#         print("this is class")
# #obj name=class name()
# Kiran=Shiva()
# print(Kiran.a)
# Kiran.show()
# PYTHON OOP BASICS NOTES
# 1. Class and Object Example
# Python
# class Kiran:
#     a = 10   # data member (class variable)

#     def Output(self):   # method
#         print(self.a)

# obj = Kiran()   # object creation
# obj.Output()    # method call
# Output:

# 10
# 2. Another Class Example
# Python
# class James:
#     def display(self):
#         print("this is class")

# obj = James()
# obj.display()
# Output:

# this is class
# 3. Multiple Objects Example
# Python
# class Naveen:
#     a = 10

#     def display(self):
#         print(self.a)

# ram = Naveen()
# syam = Naveen()

# ram.display()
# syam.display()
# Output:

# 10
# 10
# KEY CONCEPTS
# Class
# Blueprint or template
# Example: class Student
# Object
# Instance of class
# Example: obj = Student()
# self
# Refers to current object
# Must be used inside methods
# CONSTRUCTOR (init)
# Special method in Python
# Automatically called when object is created
# Used to initialize values
# Python
# class Student:
#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         print(self.name)

# obj = Student("Durga")
# obj.display()
# Output:

# Durga
# IMPORTANT POINT
# Python does NOT support multiple constructors directly
# Can use default arguments instead
# PRACTICE PROGRAM
# Python
# class Car:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def show(self):
#         print(self.name, self.price)

# c1 = Car("BMW", 5000000)
# c1.show()
# Output:
# BMW 5000000
# oops terminology
# What is class, object
# Inheritence
# polymorphism
# What is encpsulation
# Acess modifiers 
# data abstraction
#self.__init__
#inheritence
# Single(parent child)
# multiple _(two or more base classes)
# multilevel(tree)
# hierarchical(one base with sibling childs)
# class parent:
#     def output(self):
#         print('this is parent class')
# class Child(parent):
#     def outputChild(self): #output
#         print('this is child class')
# i=Child()
# i.output()
# i.outputChild()
# Decorator function behavior ni modify chesthundi.
# @ symbol use chestharu.
# Original function ni change cheyakunda extra functionality add chesthundi.
# Syntax
# @decorator_name
# def function():
#     pass
# Example
# def deco(func):

#     def wrapper():
#         print("Before")
#         func()
#         print("After")

#     return wrapper
# @deco
# def hello():
#     print("Hello")
# hello()
# Output
# Before
# Hello
# After
# Internal Working
# hello = deco(hello)
# Common Decorators
# @staticmethod
# @classmethod
# @property











     










