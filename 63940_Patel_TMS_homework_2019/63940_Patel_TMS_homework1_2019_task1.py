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
poissons_ratio = 0.33   
burgers_vector = 0.256e-9   #m
length = 2e-6  #m
n_dislocations = 4  
initial_position = length*np.array([0.1,0.13,0.16,0.3])

test_1 = get_internal_stress(np.array([0,2,3.5,4]),20,0.3,0.1)
print('The answer of test_1 is: ',test_1)

test_2 = get_internal_stress(initial_position,shear_modulus,poissons_ratio,burgers_vector)
print('The answer of test_2 is: ',test_2)