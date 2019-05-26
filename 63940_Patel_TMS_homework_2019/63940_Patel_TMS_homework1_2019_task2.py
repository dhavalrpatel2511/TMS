import numpy as np 
import matplotlib.pyplot as plt 

def get_internal_stress(dx,shear_modulus,poissons_ratio,burgers_vector):
    sigma_xy_list = []
    for j in range(0,len(dx)):
        sigma_xy = 0
        for i in range(0,(len(dx))):
            if i != j:
                dis = dx[j]-dx[i]
                D = shear_modulus*burgers_vector/(2*np.pi*(1-poissons_ratio))
                sigma_xy = sigma_xy + D*(1/(dis))
        sigma_xy_list.append(sigma_xy)
    return sigma_xy_list

shear_modulus = 26e9  #pa
poissons_ratio = 0.33   #unit_less
burgers_vector = 0.256e-9   #m
drag_coefficient = 1e-4   
bu_dr = burgers_vector/drag_coefficient
length = 2e-6    #m
n_dislocations = 4
initial_position = length*np.array([0.1,0.13,0.16,0.3])
x_new = [initial_position]  #n-dimensional array
stresses = []    #n-dimensional array
velocities = []   #n-dimensional array
total_time = 10e-9  # s
delta_t = 0.1e-9   # s
n_step = 100
delta = 0
times = [0]    #1D array

for i in range(n_step):
    stress = get_internal_stress(np.copy(x_new[i]),shear_modulus,poissons_ratio,burgers_vector)
    stresses.append(stress)
    velocity = [x * bu_dr for x in stress]
    velocities.append(velocity)
    dt = np.array([x * delta_t for x in velocity])
    x_n = x_new[i] + dt
    x_new.append(x_n)
    delta += delta_t
    times.append(delta)

print(x_new[-2])