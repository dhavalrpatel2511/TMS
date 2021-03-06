import numpy as np
import matplotlib.pyplot as plt
def fun(x,y,x0,yo):
    distance= ((x-x0)**2+(y-y0)**2)**0.5
    return distance
x0 = 1
y0 = 2
#x = float(input('enter any value for x: '))
#y = float(input('enter any value for y: '))
#x = np.array([1,2,3])
#y = np.array([4,5,6])
x_start = -4
x_end = 10
y_start = 0
y_end = 12
n_pixelx = 14
n_pixely = 12

dx = (x_end-x_start)/n_pixelx
dy = (y_end-y_start)/n_pixely
xv = np.linspace(x_start, x_end, n_pixelx+1)
yv = np.linspace(y_start, y_end, n_pixely+1)
xc = np.linspace(x_start+dx/2, x_end-dx/2, n_pixelx)
yc = np.linspace(y_start+dy/2, y_end-dy/2, n_pixely)
xv_2d, yv_2d = np.meshgrid(xv,yv)
xc_2d, yc_2d = np.meshgrid(xc,yc)

values = fun(xc_2d,yc_2d,0,1)
print(values)
plt.pcolormesh(xv_2d,yv_2d,values)
plt.colorbar()
plt.show()
#plt.imshow(values, origin='lower', extent=(-4,10,0,12))
#plt.colorbar()
#plt.show()