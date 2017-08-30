## @file CircleADT.py

## @title CircleADT
# @author Amit Binu
# @date 28/1/2017



from math import *
## @brief Creates a circle by taking its center x-coordinate, y-coordinate and radius.
# @details This class also has 2 methods that will modify the cordinates and radius
# and 4 methods that returns something about the circle. 
class CircleT(object):
   
    ## @brief Constructor for CircleT
    # @details The Constructor for this class accepts 3 parameters for the circle's
    # coordinates and its radius.
    # @param x is for the xcoordinate of Circle's center
    # @param y is for the ycoordinate of Circle's center
    # @param r is for the radius of the Circle
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r

    ## @brief Returns the x-coordinate of the Circle's center
    # @return an integer value of the Circle's x-coordinate
    def xcoord(self):
        return self.x

    ## @brief Returns the y-coordinate of the Circle's center
    # @return an integer value of the Circle's y-coordinate
    def ycoord(self):
        return self.y

    ## @brief Returns the radius of the Circle
    # @return an integer value of the Circle's raidus
    def radius(self):
        return self.r
  
    ## @brief Returns the area of the Circle.
    # @return an integer value of the Circle's Circle
    def area(self):
        return pi * (self.r)**2

    ## @brief Returns the circumference of the Circle.
    # @return an integer value of the Circle's circumference.
    def circumference(self):
        return 2 * pi * (self.r)

    ## @brief This function checks whether the Circle is inside a box whose coordinates are taken as pararmeters.
    # @details Assumes that the coordinates of the box are of the top left corner, no matter on what quadrant of the graph the box is.
    # @details It is also assumed that circle is inside the box if all the top, bottom, left and right edges of circle touches the box. 
    # @param x0 The x-coordinate of the top left front facing box.
    # @param y0 The y-coordinate of the top top left fron facing box.
    # @param w The width of the box
    # @param h The height of the box
    # @return a boolean value True if the Circle is inside the box
    # @return a boolean value False if any part of the Circle is outside the box.
    def insidebox(self, x0, y0, w, h):
        if ((self.x-self.r) >= x0 and (self.x+self.r)<= (x0+w) and (self.y+self.r)<= y0 and (self.y-self.r) >= y0-h):
            return True
        else:
            return False

    ## @brief This function checks whether 2 Circle intersected or not
    # @param c This is a Circle object which has its own coordinates and radius
    # @return a boolean value True, if the circles intersected
    # @return a boolean value False, if the circles did not intersect at all. 
    def intersect(self, c):
        if (self.x - c.xcoord())**2 + (self.y - c.ycoord())**2 <= (self.r + c.radius())**2:
            return True
        else:
            return False

    ## @brief This function sets a new radius value for the Circle by multiplying it by a value that is taken as a parameter.
    # @param k This is an integer value that will be multipied by the old radius to set the new radius.
    def scale(self, k):
        self.r = self.r * k
        
    ## @brief This function sets new x-coordinate and y-coordinate by adding the old coordinates with the numbers that are taken as parameters.
    # @param dx This is an integer value that is used to shift the circle's x-coordinate.
    # @param dy This is an integer value that is used to shift tht circle's ycoordinate. 
    def translate(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        
