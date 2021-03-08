#! /user/local/bin/python3.7
#######################################################
#   Author:     Tsung Lin Hsia
#   email:      thsia@purdue.edu
#   ID:         ee364g21
#   Date:       02/20/2019
#######################################################
import os
class Rectangle:
    def __init__(self,llPoint,urPoint):
        for ll in llPoint:
            if type(ll) is not float:
                raise TypeError("wrong type in tuple, should be float")
        for ur in urPoint:
            if type(ur) is not float:
                raise TypeError("wrong type in tuple, should be float")
        if llPoint[0]< urPoint[0] and llPoint[1]< urPoint[1]:
            self.lowerLeft = llPoint
            self.upperRight = urPoint
        else:
            raise ValueError('xll should < xur and yll should < yur')
    def isSquare(self):
        if (self.upperRight[1] -self.lowerLeft[1]) == (self.upperRight[0] -self.lowerLeft[0]):
            return True
        else:
            return False

    def intersectsWith(self,rect):
        if self.lowerLeft[0] < rect.lowerLeft[0] < self.upperRight[0] and self.lowerLeft[1] < rect.lowerLeft[1] < self.upperRight[1] :
            return True
        elif self.lowerLeft[0] < rect.lowerLeft[0] < self.upperRight[0] and self.lowerLeft[1] < rect.upperRight[1] < self.upperRight[1] :
            return True
        elif self.lowerLeft[0] < rect.upperRight[0] < self.upperRight[0] and self.lowerLeft[1] < rect.upperRight[1] < self.upperRight[1]:
            return True
        elif self.lowerLeft[0] < rect.upperRight[0] < self.upperRight[0] and self.lowerLeft[1] < rect.lowerLeft[1] < self.upperRight[1]:
            return True
        else:
            return False

    def __eq__(self, other):
        if not isinstance(other,Rectangle):
            raise TypeError('The component in the question is not an instance of Rectangle Class')
        if self.lowerLeft == other.lowerLeft and self.upperRight == other.upperRight:
            return True
        else:
            return False

class Circle:
    def __init__(self, center, radius):
        if radius > 0:
            self.radius = radius
        else:
            raise ValueError('radius should be greater than 0')
        self.center = center
    def intersectsWith(self,other):
        x1 = self.center - self.radius
        x3 = self.center - self.radius
        x2 = self.center + self.radius
        x4 = self.center + self.radius
        y1 = self.center + self.radius
        y3 = self.center - self.radius
        y2 = self.center + self.radius
        y4 = self.center - self.radius
        if isinstance(other,Rectangle):
            if x3 < other.lowerLeft[0] < x2 and y3 < other.lowerLeft[1] < y2 :
                return True
            elif x3 < other.lowerLeft[0] < x2 and y3 < other.upperRight[1] < y2 :
                return True
            elif x3 < other.upperRight[0] < x2 and y3 < other.upperRight[1] < y2:
                return True
            elif x3 < other.upperRight[0] < x2 and y3 < other.lowerLeft[1] < y2:
                return True
            else:
                return False
        else:
            x_1 = other.center - other.radius
            x_3 = other.center - other.radius
            x_2 = other.center + other.radius
            x_4 = other.center + other.radius
            y_1 = other.center + other.radius
            y_3 = other.center - other.radius
            y_2 = other.center + other.radius
            y_4 = other.center - other.radius
            if (x1 < x_1 < x3 and y1 < y_1 < y3) or (x1 < x_2 < x3 and y1 < y_2 < y3):
                return True
            else:
                return False


if __name__ == "__main__":
    rect1 = Rectangle((-1.0,-1.0),(4.0,4.0))
    rect2 = Rectangle((-2.0, -3.0), (2.0,3.0))
    #print(rect1 == rect2)
    #print(Rectangle.isSquare(rect1))
    print(rect2.intersectsWith(rect1))
    cir1 = Circle((0.1,0.2), (1.1))
    print(cir1)

