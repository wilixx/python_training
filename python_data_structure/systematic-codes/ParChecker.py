'''
Created on Jan 22, 2018

@author: Dr.Guo
'''
from Stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        elif symbol == ")":
            s.pop()
        elif symbol == ")":
            pass
#         else:s.isEmpty():
#             balanced = False
#           
               

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('(((A)B))'))
print(parChecker('(()'))
