'''
Created on Jan 22, 2018

@author: Dr.Guo
'''
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
     def __str__(self):
        str = ''
        for item in self.items:
            str=str+item+' '
        return str
 
# Stack_A = Stack()
# Stack_A.push()
# print Stack_A
# Stack_A.isEmpty()
# Stack_A.push('Mathbook')
# Stack_A.push('Chinese')
# Stack_A.push('French')
# Stack_A.push('English')
# Stack_A.push('Foo')
# Stack_A.push('Hello')
# Stack_A.push('Hello')
# Stack_A.push('Hello')
# 
# print Stack_A
# Stack_A.pop()
# print Stack_A
# Stack_A.pop()
# print Stack_A
# Stack_A.pop()
# print Stack_A
# Stack_A.pop()
# print Stack_A
# Stack_A.pop()
# print Stack_A
# Stack_A.pop()
# print Stack_A
# print Stack_A.peek()
# print Stack_A.pop()
# print Stack_A.peek()
# print Stack_A.pop()
# print Stack_A.peek()
# print Stack_A.pop()
# print Stack_A.peek()
# print Stack_A.pop()
# print Stack_A.peek()