import numpy as np
x0 = 1
y0 = 2
#x = float(input('enter any value for x: '))
#y = float(input('enter any value for y: '))
#x = np.array([1,2,3])
#y = np.array([4,5,6])
x_start = -2
x_end = 2
y_start = 0
y_end = 3
n_points1 = 5
n_points2 = 4
x = np.linspace(x_start, x_end, n_points1)
y = np.linspace(y_start, y_end, n_points2)
xx, yy = np.meshgrid(x,y)
def fun(x,y,x0,yo):
    distance= ((x-x0)**2+(y-y0)**2)**0.5
    return distance
print(fun(xx,yy,x0,y0))
