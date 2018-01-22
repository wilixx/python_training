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


class My_Singleton(object):
    def foo(self):
        print("A")

A_singleton = My_Singleton()
B_singleton = My_Singleton()
A_singleton.foo()
B_singleton.foo()
assert A_singleton is not B_singleton
print(id(A_singleton), id(B_singleton))