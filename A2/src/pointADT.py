## @file pointADT.py

## @title pointADT
# @author Amit Binu
# @date 19/2/2017
from math import *
## @brief Creates a point by taking its xcoordinate and ycoordinate
# @details This class has 4 methods. 2 of them are getters, 1 of them is a modifier and the other one returns the distance between 2 points.
class PointT(object):

    ## @breif PointT's constructor
    # @details The constructor assigns the values of xccordinate and ycoordinate to the varibales.
    # @param xc is the xcoordinate of the point
    # @param yc is the ycordinate of the point
    def __init__(self,x,y):
        self.xc = x
        self.yc = y
            
    ## @brief Returns the xcoordinate of the point
    # @return an integer value of the point's xcoordinate
    def xcrd(self):
        return self.xc 
    
    ## @brief Returns the ycoordinate of the point
    # @return an integer value of the point's ycoordinate    
    def ycrd(self):
        return self.yc
    ## @brief Returns the distance between two points
    # @details This method uses Pythagoream theorem to do the math. 
    # @param p is a point object which has its own xcoordinate nad ycoordinate
    # @return an integer value of the distance between 2 points
    def dist(self,p):
        return sqrt((self.xc  - p.xcrd())**2 + (self.yc - p.ycrd())**2)
    
    ## @brief Changes the xcoordinate and ycoordinate of the point
    # @param theta is the shift value that is used to change point's xcoordinate and ycoordinate
    def rot(self, theta):
        t = (round(cos(theta))*self.xc ) - (round(sin(theta)) * self.yc)
        t1 = (round(sin(theta))*self.xc ) + (round(cos(theta)) * self.yc)
        self.xc = t
        self.yc = t1
