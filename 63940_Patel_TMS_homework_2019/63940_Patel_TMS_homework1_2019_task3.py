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

shear_modulus = 26e9
poissons_ratio = 0.33
burgers_vector = 0.256e-9
drag_coefficient = 1e-4
bu_dr = burgers_vector/drag_coefficient
length = 2e-6
n_dislocations = 4
initial_position = length*np.array([0.1,0.13,0.16,0.3])
#initial_position = [0.20e-6,0.25e-6]
x_new = [initial_position]
stresses = []
velocities = []
delta_t = 0.1e-9
delta = 0
times = [0]
n_step = 100

for i in range(n_step):
    ans = get_internal_stress(x_new[i],shear_modulus,poissons_ratio,burgers_vector)
    stresses.append(ans)
    velocity = [x * bu_dr for x in (np.array(ans))]
    velocities.append(velocity)
    delta +=delta_t
    times.append(delta)
    dt = np.array([x * delta_t for x in velocity])
    x_n = x_new[i] + dt
    x_new.append(x_n)

def plot_trajectories(times,positions):
    fig, ax = plt.subplots()
    positions = np.divide(positions,1e-6)
    times = np.divide(times,1e-9)
    ax.plot(positions,times,'-o',markevery = [0])
    ax.plot(positions,times,'D',markevery = [-1])
    plt.title('trajectory of dislocations (t0: circles, tend: diamonds)')
    plt.xlabel('positions of dislocations [µm]')
    plt.ylabel('time [ns]')
    plt.legend(('dislocation_1','dislocation_2','dislocation_3','dislocation_4'))                                   
    fig.savefig('Task_3.png')
    plt.close(fig)
    
plot_trajectories(times,x_new)