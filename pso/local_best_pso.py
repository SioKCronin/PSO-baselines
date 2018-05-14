'''
Local Best Particle Swarm Optimization (PSO)

Using a ring network topology, particle positions are updated in relation
to the performance of their neighbors.
'''

import numpy as np
import math
from common.utils.distance import euclideanDistance, getNeighbors

POS = 0
VEL = 1
B_POS = 2
B_COST = 3

def initialize_swarm(n, val_min, val_mx, dims, v_clamp):
    swarm = []
    for particle in range(n):
        pos = np.random.uniform(val_min, val_max, dims)
        velocity = np.random.uniform(-v_clamp, v_clamp, dims)
        p_best_pos = np.random.uniform(val_min, val_max, dims)
        if obj_func.__name__ == 'rosenbrock_func':
            p_best_cost = obj_func(p_best_pos, p_best_pos)
        else:
            p_best_cost = obj_func(p_best_pos)

        swarm.append([pos, velocity, p_best_pos, p_best_cost])
    return swarm

# Update your personal best based on the current
# positions of the particles
def update_pbest(swarm, idx):
    if obj_func.__name__ == 'rosenbrock_func':
        if idx == len(swarm) - 1:
            pass
        else:
            current_cost = obj_func(particle[0], swarm[idx + 1][0])
    else:
        current_cost = obj_func(particle[0])

    if current_cost < particle[3]:
        swarm[idx][2] = particle[0]
        swarm[idx][3] = current_cost
    return swarm

def generate_weights(swarm, idx, best_pos, c1, c2):
    cognitive = (c1 * np.random.uniform(0, 1, 2)) \
                * (swarm[idx][2] - swarm[idx][0])
    social = (c2 * np.random.uniform(0, 1, 2)) \
             * ( best_pos - swarm[idx][0])
    return cognitive, social

def calculate_best_pos(swarm, k):
    best_neighbors = getNeighbors(particle[2], swarm, k)
    best_cost = particle[3]
    best_pos = particle[2]

    for y in range(len(best_neighbors)):
        if swarm[y][3] < best_cost:
            return swarm[y][2]

    return best_pos

def update_position(swarm, idx, k, c1, c2, swarm_best_pos, swarm_best_cost):
    best_pos = calculate_best_pos(swarm, k)

    if particle[3] < swarm_best_cost:
        swarm_best_cost = particle[3]
        swarm_best_pos = particle[2]

    cognitive, social = generate_weights(swarm, idx, best_pos, c1, c2)

    swarm[idx][0] += (w * swarm[idx][1]) + cognitive + social

    return swarm, swarm_best_pos, swarm_best_cost

def calculate_swarm_best(dims):
    swarm_best_pos = np.array([0]*dims)

    if obj_func.__name__ == 'rosenbrock_func':
        swarm_best_cost = obj_func(swarm_best_pos, swarm_best_pos)
    else:
        swarm_best_cost = obj_func(swarm_best_pos)

    return swarm_best_pos, swarm_best_cost

def local_best_pso(n, dims, c1, c2, w, k, iters, obj_func, val_min, val_max):
    '''
    n : int
      number of particles in the swarm
    dims : int
      number of dimensions in the space
    c1 : float
      cognitive parameter
    c2: float
      social parameter
    w : float
      inertia parameter
    k : int
      number of neighbors to be considered
    iters: int
      number of iterations
    obj_func: function
      objective function
    val_min : float
      minimum evaluatable value for obj_func
    val_max : float
      maximum evaluatable value for obj_func
    '''
    v_clamp = 0.2 * (val_max - val_min)
    swarm = initialize_swarm(n, val_min, val_max, dims, v_clamp)
    swarm_best_pos, swarm_best_cost = calculate_swarm_best(dims)
    epoch = 1

    while epoch <= iters:
        for idx, particle in enumerate(swarm):
            # Compound function?
            swarm = update_pbest(swarm, idx)
            swarm, swarm_best_pos, swarm_best_cos = \
                    update_position(swarm, idx, k, c1, c2, swarm_best_pos, swarm_best_cost)

        epoch += 1

    return swarm_best_cost
