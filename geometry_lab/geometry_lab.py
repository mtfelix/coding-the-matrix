from mat import Mat
from vec import *
from matutil import rowdict2mat
import math

## Task 1
def identity(labels = {'x','y','u'}):
    '''
    In case you have never seen this notation for a parameter before,
    the way it works is that identity() now defaults to having labels 
    equal to {'x','y','u'}.  So you should write your procedure as if 
    it were defined 'def identity(labels):'.  However, if you want the labels of 
    your identity matrix to be {'x','y','u'}, you can just call 
    identity().  Additionally, if you want {'r','g','b'}, or another set, to be the
    labels of your matrix, you can call identity({'r','g','b'}).  
    '''
    return Mat((labels,labels),{(x,x):1 for x in labels})

## Task 2
def translation(x,y):
    '''
    Input:  An x and y value by which to translate an image.
    Output:  Corresponding 3x3 translation matrix.
    '''
    return Mat(({'x','y','u'},{'x','y','u'}),{('x','x'):1,('y','y'):1,('u','u'):1, ('x','u'):x, ('y','u'):y})

## Task 3
def scale(a, b):
    '''
    Input:  Scaling parameters for the x and y direction.
    Output:  Corresponding 3x3 scaling matrix.
    '''
    return Mat(({'x','y','u'},{'x','y','u'}),{('x','x'):a,('y','y'):b,('u','u'):1})


## Task 4
def rotation(angle):
    '''
    Input:  An angle in radians to rotate an image.
    Output:  Corresponding 3x3 rotation matrix.
    Note that the math module is imported.
    '''
    return Mat(({'x','y','u'},{'x','y','u'}),{('x','x'):math.cos(angle),('y','y'):math.cos(angle),('x','y'):-math.sin(angle),('y','x'):math.sin(angle),('u','u'):1})

## Task 5
def rotate_about(x,y,angle):
    '''
    Input:  An x and y coordinate to rotate about, and an angle
    in radians to rotate about.
    Output:  Corresponding 3x3 rotation matrix.
    It might be helpful to use procedures you already wrote.
    '''
    # first: center at (x,y) by translation(-x,-y)
    # second: rotation by angle 
    # third: translation back: translation(x,y)
    return translation(x,y)*rotation(angle)*translation(-x,-y)

## Task 6
def reflect_y():
    '''
    Input:  None.
    Output:  3x3 Y-reflection matrix.
    '''
    return scale(-1, 1)

## Task 7
def reflect_x():
    '''
    Inpute:  None.
    Output:  3x3 X-reflection matrix.
    '''
    return scale(1, -1)
    
## Task 8    
def scale_color(scale_r,scale_g,scale_b):
    '''
    Input:  3 scaling parameters for the colors of the image.
    Output:  Corresponding 3x3 color scaling matrix.
    '''
    return Mat(({'r','g','b'},{'r','g','b'}),{('r','r'):scale_r,('g','g'):scale_g,('b','b'):scale_b})

## Task 9
def grayscale():
    '''
    Input: None
    Output: 3x3 greyscale matrix.
    '''
    return rowdict2mat({color:Vec({'r','g','b'},{'r':77/256,'g':151/256,'b':28/256}) for color in {'r','g','b'}})


## Task 10
def reflect_about(p1,p2):
    '''
    Input: 2 points that define a line to reflect about.
    Output:  Corresponding 3x3 reflect about matrix.
    '''
    #step1: translate by -P2   (could use P1 instead)
    #step2: rotate by -theta    (theta is the angle between the x-axis and the line through the two given points)
    #step3: reflect through x-axis
    #step4: rotate by theta
    #step5: translate by P2   (could use P1 instead)
    x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
    theta = math.atan2(y2 - y1, x2 - x1)
    return translation(x2,y2)*rotation(theta)*reflect_x()*rotation(-theta)*translation(-x2,-y2)
