# Python -
# Guido Van Rossam - 1989
# DOB - Feb 20th 1991

# Functional Prog features - no need to declare a variable
# --

# Desktop app
# web app
# Database
# Network app
# Games
# Data analyse
# Machine Learning
# AI
# ------
# Features
# simple and easy
# 33 keywords
# --
# Free - u can customize also
# -
# High Level Prog lang - humans can understand
# -
# Dynamically Typed - not require to declare a variable
# ---------

# Flavors of python
# CPython
# Jython
# pypy - performance good
# Anaconda - handle big data
# -------

# Rules
# 0-9
# a-z
# A-Z
# _
# -------------
# 1Prashant = 10

# if = abc - false
# ---

# _======>private
# __=====>Strongly Private
# -------
# 33 reserved words

# True, False, None	 - 3
# and,or,not,is		-4
# if,else,elif		-3
# while,for,break,continue,return,in,yield - 7
# try,except,finally,raise,assert 	- 5
# import,from,as,class,def,pass,global,nonlocal,lamda,del,with -11
# -----------

# Python inbuilt fn
# print()
# type()
# id()
# ----
# 14 Data types-
# int
# float
# complex
# bool
# str
# bytes
# bytesarray
# range
# list
# tuple
# set
# frozenset
# dict
# None
# ----------

# 1. int
# 10, 20, 30
# 1000000000000000000000000000000
# --
# Decimal(10) - 0 to 9
# Binary(2) - 0 to 1
# Octal(8) - 0 to 7
# Hexa(16) - 0 to 9 - a to f
# -----
# a = 0b1111
# a = 0B1111
# a = 0o1111
# a = 0x1111
# -------------

# Base Conversion
# bin()
# oct()
# hex()
# -------

# 2. float
# x = 1.23
# ---

# 3. complex
# a+bj
# x=10+20j
# a - > real part
# b - > imaginary
# ------

# 4. bool
# True and False

# True+True = 2
# 1+0 = 1
# 1-2 = -1
# ----

# 5. str 
# index
# slice
# len(str)
# *
# -----
# s = 'Rishab'
# s1 = "Prashant"
# -
# s='Rishab'
# s1="Prashant"

# s2= '''Prathmesh
#         Jadhav'''
# s3='''Hi, "Hello" good'''
# print(s3)
# ----
#    5432-1
# s='Bilal'
#    01234
# ------
# slice
# [begin:end:step]
# s='Rishab Rajput'
# --
# s='Rishab Rajput'
# # s[1:4]
# # s[:4]
# # s[:]
# # s[-1:-4]
# # s[-4:-1]
# # s[::2]
# s[::-1]
# ------------------------------------------------

# name1 = 'Ravi'
# name1*5
# ---
# name1 = 'Ravi '
# # name1*5
# len(name1)
# ---------------------

# Type Casting 
# int()
# float()
# complex()
# bool()
# str()
# -------
# # float(19)
# # float(10+5j)
# # complex(2)
# # int(2+3j)
# # bool(1)
# # str(10)
# ---------------

# d/f b/w Immutable and mutable
# Immutable - Non Changable
# Mutable - changable
# a = [1,2,3,4,5]
# a[1] = 6 - error
# a[1] = 6 - change
# ------------

# is operator

# x=10
# y=10
# x is y
# y is x
# ----
# x=257
# id(x)
# y=257
# # x is y
# y is x
# - ---
# x=8
# y=9
# # x is y
# y is x
# ---------

# bytes data type 
# immutable array

# x=[10,20,30]
# b=bytes(x)
# type(b)
# ----
# x=[10,20,30]
# b=bytes(x)
# # type(b)
# # type(x)
# # b[1] = 40
# for x in b:print(x)
# ----------

# bytearray data type - same as bytes 
# mutable 

# x=[10,20,30]
# b=bytearray(x)
# # type(b)
# # type(x)
# b[1] = 40
# for x in b:print(x)
# -----------

# list data type - represent []
# mutable

# l=[]
# pop
# remove
# append
# ------
# l=[]
# # type(l)

# l.append(10)
# l.append(20)
# l.append(30)
# l.append('Rishab')
# l.append('Prasang')
# # print(l)
# l.remove(10)
# # print(l)
# l.pop()
# ---
# one = ['b','d','a','x','t']
# one.sort()
# print(one)
# ------- 

# tuple - same as list 
# immutable 
# represent - ()

# t=(10,'Sourav',True,30)
# --- 
# t=(10,'Sourav',True,30)
# # t[1] = 'Abhinav'
# t[1:]
# # print(t)
# ---------------------

# range
# immutable 
# slicing allowed 

# range(end)
# # r = range(11)
# # r = range(11,16)
# r = range(5,51,5)
# # print(r)
# for i in r:print(i)
# -----

# -----------------------------------------------------------------------
# Class - 3 17/5/2021
# -----------------------------------------------------------------------

# Set data type - {}
# not support indexing
# not support slicing 
# no dublicates 
# mutable 
# growable

# s={1,2,1,3,2,4,4,5,5,5}
# s.add('Rishab')
# s.remove(4)
# print(s)
# --------------------------------------------- 

# forzenset
# immutable

# s={1,2,1,3,2,4,4,5,5,5}
# fs=frozenset(s)
# # type(fs)
# # fs
# print(fs)

# can not add or remove 
# -------------------------------------------------------------------- 

# dict data type  - {}
# mutable
# key value 
# no dulicates allowed 

# d={100:'Rishab', 95:'Sourav', 90:'Prasang'}
#  key  object
# type(d)
# d

# x={}
# s=set()
# type(s)

# x={}
# x[100] = 'Rishab'
# x
# -------------------------------- 

# None data type 
# t = None
# print(t)
# ----- 

# \n - next line 
# \'
# \"

# s = 'Rish\'ab \nRajp\"ut'
# print(s)
# ---------------------------------------------------------

# Operators 

# 1. Arithematic
# 2. Relational/comparision
# 3. Logical 
# 4. Bitwise
# 5. Assignment 
# 6. Special


# 1. Arithematic
# +
# -
# *
# /
# %
# **
# //


# 2. Relational/comparision
# >,>=,<,<=

# a=10
# b=3
# print(a>b)

# Equality operator 
# ==, !=
# a=10
# b=3
# print(a==b)


# 3. Logical 
# and || or || not 
# --------------------------------------------- 


# -----------------------------------------------------------------------
# Class - 4     18/5/2021
# -----------------------------------------------------------------------

# 4. Bitwise Operators
# applicable for int and boolean 

# &   and
# |   or
# ^   ex-or
# ~   bitwise complement 
# >>  bitwise left shift
# <<  bitwise right shift

# 4&5 

#     1 0 0
#     1 0 1
#     - - -
#     1 0 1

# 4|5 
# 4^5 
# # ~4
# 10<<2    101000
# 10>>2
# ----------------------------------------- 

# 5. Assignment Operator 
# x=100
# x+=100

# ++x
# x++

# /=
# *=
# %=
# ----

# Ternary operator 
# ? :

# a,b=10,20
# x=30 if a>b else 40
# print(x)
# ---------------------------- 

# 6. Special Opertator
# For address purpose (id)

# identity operator 
# is , is not 
# a=1000
# b=1000
# # print(a is b)
# # 139731645122064
# # 139731645123952
# # id(b)
# print(a is not b)

# Membership operator 
# in 
# in not 

# list1 = [10,20,30]
# print(100 in list1)

# s='Rishab'
# print('t' in s)

# -----
# Math 
# sqrt
# pow
# pi 
# floor
# ceil

# input and output statements 
# eno=int(input("Enter Sno "))
# ename=input("Enter name ")
# print(eno)
# print(ename)

# print("xts")
# ------------------------------------------------ 

# Flow Control 

# 1
# if 
# elif - else if
# else

# 2. Iterative
# for loop
# s='Rishab'
# for y in s:
#   print(y)

# s='Prashant'
# count=0
# for x in s:
#   count+=1
#   print(x)
# print(count)


# while
# x=1
# while x<=10:
#   print(x)
#   x+=1

# nested loops 
# for i in range(3):
#   for j in range(4):
#     print("i={} and j={}".format(i,j))


# 3. Tranasfer 
# break
# continue
# pass

# for i in range (10):
#   if i == 5:
#     # break 
#     continue
#   print(i)
# --------------------------------- 

# String Data Type 
# index 
# slice 
# ''
# ""
# '''
# """
# len(s)
# in ,not in

# s='Sourav'+2
# print(s)

# Remove spaces 
# 1. lstrip()
# 2. rstrip()
# 3. strip()

# s='         Prashant       '
# s.strip()


# -----------------------------------------------------------------------
# Class - 5     21/5/2021
# -----------------------------------------------------------------------
# Record meeting 

# substring 

# find()
# index()
# rfind()
# rindex
# s='Rishab'
# s1='Souravo'
# print(s1.rfind('o'))

# print(s.index('a',2,5))

# print(s.rindex('a',2))
# --------- 

# s='Prasang'
# s1='Prathamesh'
# s2='Ravi'
# s3='prashant'
# s4='Rishab'
# print(s.lower())
# print(s1.upper())
# print(s2.swapcase())
# print(s3.title())
# print(s4.capitalize())


# How to check character 
# gives boolean 
# s='123abv'
# s.isalnum()
# s.isalpha()
# s.isdigit()
# s.islower()
# s.isupper()
# s.istitle()
# s.isspace()

# WAP to reverse the string 
# s='Prasang'
# 1st method
# s[::-1]

# 2nd method
# for x in reversed(s):
#   print(x)

# 3rd method
# i=len(s)-1
# output=''
# while i>=0:
#   output += s[i]
#   i-=1
# print(output)

# WAP to remove dublicates in the string 
# s=input('Enter string : ')
# l=[]
# for x in s:
#   if x not in l:
#     l.append(x)
# # print(l)
# output=''.join(l)
# print(output)

# ------------ 

# WAP to find no. of occurrence 
# s=input('Enter string : ')
# d={}

# # value put in dict 
# for x in s:
#   if x not in d.keys():
#     d[x]=1
#   else:
#     d[x]+=1

# # printing dict
# for key,value in d.items():
#   print('{} occurs {} times'.format(key,value))







