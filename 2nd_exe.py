import numpy as np 
import matplotlib.pyplot as plt 

def edge_dislocation_xy(x,y,shear_modulus,poissons_ratio,burger_vector):
    D = shear_modulus*burger_vector/(2*np.pi*(1-poissons_ratio))
    sigma_xy = D*x*(x**2-y**2)/(x**2+y**2)**2
    return sigma_xy
def edge_dislocation_xx(x,y,shear_modulus,poissons_ratio,burger_vector):
    D = shear_modulus*burger_vector/(2*np.pi*(1-poissons_ratio))
    sigma_xx = -D*y*(3*x**2+y**2)/(x**2+y**2)**2
    return sigma_xx
def edge_dislocation_yy(x,y,shear_modulus,poissons_ratio,burger_vector):
    D = shear_modulus*burger_vector/(2*np.pi*(1-poissons_ratio))
    sigma_yy = D*y*(x**2-y**2)/(x**2+y**2)**2
    return sigma_yy
def edge_dislocation_zz(x,y,shear_modulus,poissons_ratio,burger_vector):
    #D = shear_modulus*burger_vector/(2*np.pi*(1-poissons_ratio))
    sigma_zz = poissons_ratio*(edge_dislocation_xx(x,y,shear_modulus,poissons_ratio,burger_vector)+edge_dislocation_yy(x,y,shear_modulus,poissons_ratio,burger_vector))
    return sigma_zz
shear_modulus = 90e9
poissons_ratio = 0.3
burger_vector = 0.25e-9

x_start = -100e-9
x_end = 100e-9
y_start = -100e-9
y_end = 100e-9
x0 = 50e-9
y0 = 20e-9
n_pixelx = 50
n_pixely = 50

dx = (x_end-x_start)/n_pixelx
dy = (y_end-y_start)/n_pixely

xv = np.linspace(x_start, x_end, n_pixelx+1)
yv = np.linspace(y_start, y_end, n_pixely+1)

xc = np.linspace(x_start+(dx/2), x_end-(dx/2), n_pixelx)
yc = np.linspace(y_start+(dy/2), y_end-(dy/2), n_pixely)

xv_2d, yv_2d = np.meshgrid(xv,yv)
xc_2d, yc_2d = np.meshgrid(xc,yc)

sigma_xy = edge_dislocation_xy(xc_2d,yc_2d,shear_modulus,poissons_ratio,burger_vector)
sigma_xy_1=edge_dislocation_xy(xc_2d-x0,yc_2d-y0,shear_modulus,poissons_ratio,burger_vector)
sigma_xx = edge_dislocation_xx(xc_2d,yc_2d,shear_modulus,poissons_ratio,burger_vector)
sigma_yy = edge_dislocation_yy(xc_2d,yc_2d,shear_modulus,poissons_ratio,burger_vector)
sigma_zz = edge_dislocation_zz(xc_2d,yc_2d,shear_modulus,poissons_ratio,burger_vector)
#plt.pcolormesh(xv_2d,yv_2d,stress_xy)
#im = plt.imshow(stress_xy, origin='lower', extent=(x_start,x_end,y_start,y_end),aspect ='equal' ,vmin=-0.1e9,cmap='RdBu')
#plt.colorbar()
#cs = plt.contour(xc_2d,yc_2d,stress_xy,levels=np.linspace(-0.1e9,0.1e9,11),cmap='gray_r')
#plt.clabel(cs, fmt='%1.1e')
#plt.show()

fig,ax=plt.subplots(nrows=2,ncols=3,figsize=(15,10))
im_kwargs={'origin':'lower','extent':(x_start,x_end,y_start,y_end),'aspect':'equal','vmin':-0.1e9,'vmax':-0.1e9, 'cmap':'RdBu'}
im = ax[0][0].imshow(sigma_xy, **im_kwargs)
cs = ax[0][0].contour(xc_2d,yc_2d,sigma_xy,levels=np.linspace(-0.1e9,0.1e9,11),cmap='YlOrRd_r')
ax[0][0].clabel(cs, fmt='%1.1e')
im = ax[0][1].imshow(sigma_xx, **im_kwargs)
cs = ax[0][1].contour(xc_2d,yc_2d,sigma_xx,levels=np.linspace(-0.1e9,0.1e9,11),cmap='YlOrRd_r')
ax[0][1].clabel(cs, fmt='%1.1e')
im = ax[0][2].imshow(sigma_yy, **im_kwargs)
cs = ax[0][2].contour(xc_2d,yc_2d,sigma_yy,levels=np.linspace(-0.1e9,0.1e9,11),cmap='YlOrRd_r')
ax[0][2].clabel(cs, fmt='%1.1e')
im = ax[1][0].imshow(sigma_zz, **im_kwargs)
cs = ax[1][0].contour(xc_2d,yc_2d,sigma_zz,levels=np.linspace(-0.1e9,0.1e9,11),cmap='YlOrRd_r')
ax[1][0].clabel(cs, fmt='%1.1e')
im = ax[1][1].imshow(sigma_xy_1, **im_kwargs)
cs = ax[1][1].contour(xc_2d,yc_2d,sigma_xy_1,levels=np.linspace(-0.1e9,0.1e9,11),cmap='YlOrRd_r')
ax[1][1].clabel(cs, fmt='%1.1e')
im = ax[1][2].imshow(sigma_xy_1+sigma_xy, **im_kwargs)
cs = ax[1][2].contour(xc_2d,yc_2d,sigma_xy_1+sigma_xy,levels=np.linspace(-0.1e9,0.1e9,11),cmap='YlOrRd_r')
ax[1][2].clabel(cs, fmt='%1.1e')
for i in range(2):
    for j in range(3):
        fig.colorbar(im,ax=ax[i,j])
plt.show()

#cs = plt.contour(xc_2d,yc_2d,sigma_xy,levels=np.linspace(-0.1e9,0.1e9,11),cmap='gray_r')
#plt.clabel(cs, fmt='%1.1e')

#fig, ax=plt.subplots(figsize=(10,10))

#x0=10e-9
#y0=10e-9
#fig, ax=plt.subplots(ncols=3, figsize=(20,7))
#sigma_xy_0=edge_dislocation_xy(xc_2d,yc_2d,shear_modulus,burger_vector,poissons_ratio)
#sigma_xy_1=edge_dislocation_xy(xc_2d-x0,yc_2d-y0,shear_modulus,burger_vector,poissons_ratio)
#ax[0].imshow(sigma_xy_0, **im_kwargs)
#ax[0].contour(xc_2d,yc_2d,sigma_xy_0,levels=np.linspace(-0.1e9,0.1e9,11),cmap='YlOrRd_r')
#ax[1].imshow(sigma_xy_1, **im_kwargs)
#ax[1].contour(xc_2d,yc_2d,sigma_xy_1,levels=np.linspace(-0.1e9,0.1e9,11),cmap='YlOrRd_r')
#ax[2].imshow(sigma_xy_0+sigma_xy_1, **im_kwargs)
#ax[2].contour(xc_2d,yc_2d,(sigma_xy_0+sigma_xy_1),levels=np.linspace(-0.1e9,0.1e9,11),cmap='YlOrRd_r')
#plt.show()
