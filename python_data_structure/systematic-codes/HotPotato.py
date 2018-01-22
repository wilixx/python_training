'''
Created on Jan 22, 2018

@author: Dr.Guo
'''
from Queue import Queue

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num-1):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato(["Bill","David"],7))
print(hotPotato(["Bill","David","Susan"],7))
print(hotPotato(["Bill","David","Susan"],7))
print(hotPotato(["Bill","David","Susan","Jane",],7))
print(hotPotato(["Bill","David","Susan","Jane","Kent"],7))
print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad","Allen"],7))
print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad","Allen","Dr.S"],7))
print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad","Allen","Dr.S","A"],7))
print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad","Allen","Dr.S","A","B"],7))
print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad","Allen","Dr.S","A","B","C"],7))
print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad","Allen","Dr.S","A","B","C","D"],7))
