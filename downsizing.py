from math import sqrt
import math
import numpy as np

x0,y0,z0 = [int(x) for x in input().split()]
#x0 is 0 x-point center
#y0 is 0 y-point center
#z0 is 0 circle radius

points = input().split()
#print(points)

points = [eval(i) for i in points]
#print(points)

lineCount = points[0]
points.remove(points[0])
#print(lineCount)
#print(points)

other = [(points[j], points[j+1]) for j in range(0,len(points),2)]
pointsTuple = other

other = [[points[j], points[j+1]] for j in range(0,len(points),2)]
pointsArray = other

#print(pointsTuple)
#print(pointsArray)

posNegativeList = []

def signedArea(A,B,C):
    """Assumes A, B and C are each (x,y) tuples."""
    return ((B[0]-A[0])*(C[1]-A[1]) - (C[0]-A[0])*(B[1]-A[1])) / 2

def signedAreaPolygon(P):
    """Return signed area of polygon P, which is presumed as list
     of three or more vertices in order, given as (x,y) pairs.
    """
    total = 0
    for k in range(len(P)):  
       # note: we rely on python wraparound when k-1 is negative
       ababa = signedArea( (0,0), P[k-1], P[k] )
       total += ababa
       if ababa>0:
        posNegativeList.append(1)
       else:
        posNegativeList.append(0)
        
    return total

def findCircle(x1, y1, x2, y2, x3, y3) :
    x12 = x1 - x2;
    x13 = x1 - x3;
 
    y12 = y1 - y2;
    y13 = y1 - y3;
 
    y31 = y3 - y1;
    y21 = y2 - y1;
 
    x31 = x3 - x1;
    x21 = x2 - x1;
 
    # x1^2 - x3^2
    sx13 = pow(x1, 2) - pow(x3, 2);
 
    # y1^2 - y3^2
    sy13 = pow(y1, 2) - pow(y3, 2);
 
    sx21 = pow(x2, 2) - pow(x1, 2);
    sy21 = pow(y2, 2) - pow(y1, 2);
 
    f = (((sx13) * (x12) + (sy13) *
          (x12) + (sx21) * (x13) +
          (sy21) * (x13)) / (2 *
          ((y31) * (x12) - (y21) * (x13))));
             
    g = (((sx13) * (y12) + (sy13) * (y12) +
          (sx21) * (y13) + (sy21) * (y13)) /
          (2 * ((x31) * (y12) - (x21) * (y13))));
 
    c = (-pow(x1, 2) - pow(y1, 2) -
         2 * g * x1 - 2 * f * y1);
 
    # eqn of circle be x^2 + y^2 + 2*g*x + 2*f*y + c = 0
    # where centre is (h = -g, k = -f) and
    # radius r as r^2 = h^2 + k^2 - c
    h = -g;
    k = -f;
    sqr_of_r = h * h + k * k - c;
 
    # r is the radius
    r = round(sqrt(sqr_of_r), 5);
 
    print("Centre = (", h, ", ", k, ")");
    print("Radius = ", r);

originalPolyArea = signedAreaPolygon(pointsTuple)
#print(originalPolyArea)

#print(posNegativeList)
#list is kinda good, [-1] would be the start then go 0,1,2,3,4

#print('for loop break')
newPoints = [[0 for x in range(2)] for y in range(lineCount)] 

#print('testnewpoints', newPoints)

#print('testing', print())

for i in range(len(pointsArray)):
    #dist = math.hypot(x2-x1, y2-y1)
    #print('testing',(pointsArray[i][1]-y0))
    #print('testing2', (pointsArray[i][0]-x0))

    slope = ((pointsArray[i][1]-y0)/(pointsArray[i][0]-x0))
    #print('slope', slope)
    distPandO = math.hypot(pointsArray[i][0]-x0, pointsArray[i][1]-y0)
    #print('distPandO', distPandO)
    distPprimeandO = (z0*z0)/distPandO
    #print('distPprimeandO', distPprimeandO)
    #print('doing', distPprimeandO, pointsArray[i][0], pointsArray[i][1])
    xChange = distPprimeandO/sqrt(((slope**2) + 1))
    #print('xchange', xChange)
    yChange = xChange * slope
    #print('ychange', yChange)
    #new point x
    print(xChange)
    print('this is i', i)
    newPoints[i][0] = x0 + (xChange)
    print('points array 0', newPoints[i][0])
    print(newPoints[i][0])
    #new point y
    newPoints[i][1] = y0 + (yChange)
    #print('hello', newPoints[i])
    
print(newPoints)
#print(pointsArray)
#print('hello', len(newPoints))
#print('hello2', len(pointsArray))

for j in range(len(newPoints)):
    #line segment for loop
    #midpoint between j and next j point
    # THIS IS X VALUE print(pointsArray[j][0])
    if j == len(newPoints)-1:
        midpointX = (newPoints[j][0] + newPoints[0][0])/2
        midpointY = (newPoints[j][1] + newPoints[0][1])/2
        midpoint = [midpointX, midpointY]
        print('cur midpoint', midpoint)
        findCircle(newPoints[j][0], newPoints[j][1], newPoints[0][0], newPoints[0][1], midpoint[0], midpoint[1])
    else:
        midpointX = (newPoints[j][0] + newPoints[j+1][0])/2
        midpointY = (newPoints[j][1] + newPoints[j+1][1])/2
        midpoint = [midpointX, midpointY]
        print('cur midpoint', midpoint)
        print('j', newPoints[j][0], newPoints[j][1])
        print('j+1', newPoints[j+1][0], newPoints[j+1][1])
        findCircle(newPoints[j][0], newPoints[j][1], newPoints[j+1][0], newPoints[j+1][1], midpoint[0], midpoint[1])
        #print('cur midpoint', midpoint)
        #print(define_circle(pointsArray[j], pointsArray[j+1], midpoint))

    #found midpoint
