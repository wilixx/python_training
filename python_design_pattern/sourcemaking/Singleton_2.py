'''
Created on Jan 22, 2018
Introduction:
Ensure a class only has one instance, and provide a global point of
access to it.
@author: Dr.Guo
'''
"""
Ensure a class only has one instance, and provide a global point of
access to it.
"""
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)  
        return cls._instance  

class MyClass(Singleton):  
    a = 1

one = MyClass()
two = MyClass()

assert one == two

assert one is two

print(id(one), id(two))