import lineADT
import pointADT

from math import *


## @file circleADT.py
#  @author Amit Binu
#  @brief Has a class that creates 2d circles
#  @date 19/02/2017

## @brief Creates a point by taking its xcoordinate and ycoordinate
# @details This class has 6 methods. 2 of them are getters and the others represent some properties of the circle.
class CircleT(object):
    
    ## @brief Constructor for the circleADT
    # @param cin is a point object that represents the midpoint of the circle
    # @param rin is an integer value that represents the radius of the circle
    def __init__ (self, cin, rin):
        self.c = cin
        self.r = rin

    ## @brief This is a getter method
    # @return a point object that represents the middle point of the circle.
    def cen(self):
        return self.c

    ## @breif This is a getter method
    # @return an integer value that represents the radius of the circle. 
    def rad(self):
        return self.r

    ## @brief This method calculates the area of the circle using the Pi from math libraray.
    # @return an integer value that represents the area of the cirlce
    def area(self):
        return pi * ((self.r)**2.0)

    ## @brief Checks whether two circles interesect or not.
    # @details p is a point object whose coordinates are average of the coordinates of 2 Circles' centeres.
    # @details It is assumed that the if one circle is inside the other, then it intersects.
    # @param ci is a CircleT object, so it is like another circle.
    # @return True if the 2 circle objects intersect and Fasle is it doesn't.
    def intersect(self, ci):
        p = pointADT.PointT(( (self.c).xcrd() + (ci.cen()).xcrd()) /2.0,( (self.c).ycrd() + (ci.cen()).ycrd()) /2.0 )
        
        return insideCircle(p, self) and insideCircle(p, ci)

    ## @breif makes a new connection with a new circle object
    # @return a line object that represents the line between the nid points of the 2 circle object. This line represents the connection between these 2 circle objects.
    def connection(self, ci):
        return lineADT.LineT(self.c, ci.cen())
    
    ## @breif Calculates the force that one circle expereinces from the other circle
    # @details This method uses the formula for the gravitational force. However, instead of the mass area() is used to calculate this.
    # @details Gravitational force is the force between 2 planets/2electrons. In this module, it is the force between 2 circles. 
    # @param f is a function that has the equation for gravitational force.
    # @return The value of the force between two circles. 
    def force(self, f):
        return (lambda x: (self.area()) * (x.area()) * f((self.connection(x)).len()))
    
# @brief A local function that checks whether the distance between a point and a circle's center is less than or equal to the circle's radius.
# @details This function uses cen() and rad() methods to get the circle's center point and circle's radius.
# @param p is a point object
# @param c is a circle object
# @ return a boolean value. True if the distance between a point and a circle's center is less than ot equal to the circle's radius and False otherwise.
def insideCircle(p,c):
    return p.dist(c.cen()) <= c.rad()

