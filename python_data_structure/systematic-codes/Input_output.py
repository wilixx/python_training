'''
Created on Jan 22, 2018

@author: Dr.Guo
'''
# Atomic data types
#from _cffi_backend import string
Name=[]
aName = input("Please enter your name ")

Name.append(aName)
print("Your name in all capitals is",Name.upper(),
      "and has length", len(Name))
