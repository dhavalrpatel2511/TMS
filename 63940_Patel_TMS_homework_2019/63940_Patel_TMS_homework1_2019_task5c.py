import numpy as np 
import matplotlib.pyplot as plt 

def edge_dislocation_xy_interaction(dx,shear_modulus,poissons_ratio,burger_vector):
    sigma_xy_list = []
    for j in range(0,len(dx)):
        sigma_xy = 0
        for i in range(0,(len(dx))):
            if i != j:
                dis = dx[j]-dx[i]
                D = shear_modulus*burger_vector/(2*np.pi*(1-poissons_ratio))
                sigma_xy = sigma_xy + D*(1/(dis))
        sigma_xy_list.append(sigma_xy)
    return sigma_xy_list

shear_modulus = 26e9
poissons_ratio = 0.33
burger_vector = 0.256e-9
drag_coefficient = 1e-4
bu_dr = burger_vector/drag_coefficient
length = 2e-6
n_dislocations = 4
initial_position = length*np.array([0.1,0.13,0.16,0.3])
x_new = [initial_position]
velocities = []
stresses = []
delta_t = 0.1e-9
delta = 0
times = [0]
n_step = 300
for i in range(n_step):
    ans = edge_dislocation_xy_interaction(x_new[i],shear_modulus,poissons_ratio,burger_vector)
    external_stress = -25e6
    stresses.append(ans)
    velocity = [x * bu_dr for x in (np.array(ans)+external_stress)]
    delta +=delta_t
    times.append(delta)
    dt = np.array([x * delta_t for x in velocity])
    x_n = x_new[i] + dt
    current_position = x_n
    if current_position[0] <= 0:
        current_position[0] = 0
        x_new.append(current_position)
        velocity[0]=0
        velocities.append(np.array(velocity))
    else:
        x_new.append(current_position)
        velocities.append(np.array(velocity))

def plot_trajectories(times,velocities,positions):
    fig, ax = plt.subplots(ncols=2,figsize=(12,7))
    times = np.divide(times,1e-9)
    positions = np.divide(positions,1e-6)

    plt.subplot(1,2,1)
    plt.plot(velocities,times[1:],'-o',markevery = [0])
    plt.plot(velocities,times[1:],'D',markevery = [-1])
    plt.title('trajectory of dislocations velocities(t0: circles, tend: diamonds)')
    plt.legend(('dislocation_1','dislocation_2','dislocation_3','dislocation_4'))
    plt.xlabel('velocity [m/s]')
    plt.ylabel('time [ns]')
    plt.grid(True)
    
    plt.subplot(1,2,2)
    plt.plot(positions,times,'-o',markevery = [0])
    plt.plot(positions,times,'D',markevery = [-1])
    plt.title('trajectory of dislocations(t0: circles, tend: diamonds)')
    plt.legend(('dislocation_1','dislocation_2','dislocation_3','dislocation_4'))
    plt.xlabel('positions of dislocations [µm]')
    plt.ylabel('time [ns]')
    plt.grid(True)
    
    fig.savefig('Task_5c.png')
    plt.close(fig)

plot_trajectories(times,velocities,x_new)