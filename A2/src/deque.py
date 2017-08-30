## @file deque.py

## @title deque
# @author Amit Binu
# @date 19/2/2017
from circleADT import *
from math import *


## @brief This is an abstract object that represents a queue that has a sequence of circles.
class Deq:
    
    MAX_SIZE = 20
    s = []
    
    def init():
        Deq.s = []

    @staticmethod
    def pushBack(c):
        if (len(Deq.s) <= Deq.MAX_SIZE):
            
            (Deq.s).append(c)
            

        else:
            raise FULL("The maximum size of the queue is 20 !")

    @staticmethod
    def pushFront(c):
        if (len(Deq.s) <= Deq.MAX_SIZE):
                (Deq.s).insert(0,c)

        else:
            raise FULL("The maximum size of the queue is 20 !")

    @staticmethod
    def popBack():
        if (len(Deq.s) != 0):
            return (Deq.s).pop(len(Deq.s) - 1)
        else:
            raise EMPTY("The queue is empty!")

    @staticmethod
    def popFront():
        if (len(Deq.s) != 0):
            return (Deq.s).pop(0)
        
        else:
            raise EMPTY("The queue is empty!")

    @staticmethod
    def back():
        if (len(Deq.s) != 0):
            return (Deq.s)[len(Deq.s) - 1]
        else:
            raise EMPTY("The queue is empty!")

    @staticmethod
    def front():
        if (len(Deq.s) != 0):
            return (Deq.s)[0]
        else:
            raise EMPTY("The queue is empty!")

    @staticmethod
    def size():
        return (len(Deq.s))

    @staticmethod
    def disjoint():
        if (len(Deq.s) == 0):
            raise EMPTY("The queue is empty")
        else:
            for i in range (len(Deq.s)):
                for j in range (len(Deq.s)):
                    if i != j:
                        if ((Deq.s)[i].intersect((Deq.s)[j])):
                            return False

            return True

    @staticmethod
    def sumFx(f):
        if (len(Deq.s) == 0):
            raise EMPTY("The queue is empty")
        else:
            sum = 0
            for i in range (len(Deq.s)):
                sum = sum  +  Fx(f, Deq.s[i], Deq.s[0])

            return sum

    @staticmethod
    def totalArea():
        size = len(Deq.s)
        if size == 0:
            raise EMPTY("The queue is empty")

        else:
            sum_of_area = 0
            for i in range(len(Deq.s)):
                sum_of_area = sum_of_area + ((Deq.s)[i]).area()

            return sum_of_area
        

    @staticmethod
    def averageRadius():
        size = len(Deq.s)
        if size == 0:
            raise EMPTY("The queue is empty")
        else:
            average_radius =0

            for i in range(len(Deq.s)):
                average_radius = average_radius + ((Deq.s)[i].rad())

            return average_radius / (1.0* (len(Deq.s)))
    
        
class FULL(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

class EMPTY(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

def Fx(f, ci, cj):
    return xcomp(ci.force(f)(cj), ci, cj)

def xcomp(F, ci, cj):
    return F*((((ci.cen()).xcrd()) - ((cj.cen()).xcrd()))/((ci.connection(cj)).len()))
    
