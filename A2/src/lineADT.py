## @file lineADT.py

## @title lineADT
# @author Amit Binu
# @date 19/2/2017
import pointADT


b = pointADT.PointT(5,4)
e = pointADT.PointT(2,3)

## @brief Creates a line by taking two point objects
# @details This class has 5 methods. 2 of them are getters, 1 of them is a modifier and the others represent some properties of the line.
class LineT(object):

    ## @breif The constructor assigns the 2 pint objects to the self varibales.
    # @param b is the first point object.
    # @param e is the second point object. 
    def __init__(self,p1,p2):
        self.b = p1
        self.e = p2
        
    ## @brief This is a getter method.
    # @return the first point that is created to make a line. 
    def beg(self):
        return self.b
    
    ## @brief This is a getter method.
    # @return the second point that is created to make a line. 
    def end(self):
        return self.e

    ## @brief This method returns the distance between these poitns.
    # @return an integer value that represents the distance between points b and e that are taken as parameters for the class LinetT. 
    def len(self):
        return (self.b).dist(self.e)

    ## @brief This method calcuates and returns the mid point of the line created between points b and e. 
    # @return a point object that will have the xcoordinate and ycoordinate of the mid point of the line between points b and e.
    def mdpt(self):
        if (self.len() == 0):
            return pointADT.PointT(0,0)
        
        return pointADT.PointT(  avg((self.b).xcrd(),(self.e).xcrd()), avg((self.b).ycrd(),(self.e).ycrd())  )
    
    ## @brief This method changes the values of xcoordinate and ycoordinate of the points b and e. 
    # @param theta is the value that is used to change the xcoordinate and ycoordinate values of b and e.
    def rot(theta):
        (self.b).rot(theta)
        (self.e).rot(theta)

## @brief A local function
# @details This function does the average of two numbers
# @param x1 is a number
# @param x2 is another number
# @return a value that represents the average of the two numbers that were taken as parameters. 
def avg(x1,x2):
    return (x1+x2)/2.0

        
j = LineT(b,e)
