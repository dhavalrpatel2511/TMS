import numpy as np
x0 = -2
y0 = 1
#x = float(input('enter any value for x: '))
#y = float(input('enter any value for y: '))
x = np.array([1,2,3])
y = np.array([4,5,6])
def fun(x,y,x0,yo):
    distance= ((x-x0)**2+(y-y0)**2)**0.5
    return distance
print(fun(x,y,x0,y0))