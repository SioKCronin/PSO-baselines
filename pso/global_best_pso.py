# Global Best PSO

import numpy as np
from random import shuffle
from common.utils.distance import euclideanDistance, getNeighbors

def global_best_pso(n, dims, c1, c2, w, iters, obj_func, val_min, val_max):

    search_range = val_max - val_min
    v_clamp_min = - (0.2 * search_range)
    v_clamp_max = 0.2 * search_range

    swarm = []
    swarm_best_pos = np.array([0]*dims)
    if obj_func.__name__ == 'rosenbrock_func':
        swarm_best_cost = obj_func(swarm_best_pos, swarm_best_pos)
    else:
        swarm_best_cost = obj_func(swarm_best_pos)

    P_POS_IDX = 0
    P_VELOCITY_IDX = 1
    P_BEST_POS_IDX = 2
    P_BEST_COST_IDX = 3

    # Initialize swarm
    for particle in range(n):
        pos = np.random.uniform(val_min, val_max, dims)
        velocity = np.random.uniform(val_min, val_max, dims)
        p_best_pos = np.random.uniform(val_min, val_max, dims)
        if obj_func.__name__ == 'rosenbrock_func':
            p_best_cost = obj_func(p_best_pos, p_best_pos)
        else:
            p_best_cost = obj_func(p_best_pos)

        swarm.append([pos, velocity, p_best_pos, p_best_cost])

    epoch = 1

    while epoch <= iters:
        for idx, particle in enumerate(swarm):
            if obj_func.__name__ == 'rosenbrock_func':
                if idx == len(swarm) - 1:
                    pass
                else:
                    current_cost = obj_func(particle[P_POS_IDX],\
                                   swarm[idx + 1][P_POS_IDX])
            else:
                current_cost = obj_func(particle[P_POS_IDX])
            personal_best_cost = swarm[idx][P_BEST_COST_IDX]
            if current_cost < personal_best_cost:
                swarm[idx][P_BEST_POS_IDX] = swarm[idx][P_POS_IDX]
                swarm[idx][P_BEST_COST_IDX] = current_cost

            # Update swarm global best
            if personal_best_cost < swarm_best_cost:
                swarm_best_cost = personal_best_cost
                swarm_best_pos = swarm[idx][P_BEST_POS_IDX]

            # Compute velocity
            cognitive = (c1 * np.random.uniform(0, 1, 2)) * \
                        (swarm[idx][P_BEST_POS_IDX] - swarm[idx][P_POS_IDX])
            social = (c2 * np.random.uniform(0, 1, 2)) * \
                     (swarm_best_pos - swarm[idx][P_POS_IDX])
            velocity = (w * swarm[idx][P_VELOCITY_IDX]) + cognitive + social
            if velocity[0] < v_clamp_min:
                swarm[idx][P_VELOCITY_IDX][0] = v_clamp_min
            if velocity[1] < v_clamp_min:
                swarm[idx][P_VELOCITY_IDX][1] = v_clamp_min
            if velocity[0] > v_clamp_max:
                swarm[idx][P_VELOCITY_IDX][0] = v_clamp_max
            if velocity[1] > v_clamp_max:
                swarm[idx][P_VELOCITY_IDX][1] = v_clamp_max
            else:
                swarm[idx][P_VELOCITY_IDX] = velocity

            # Update poss
            swarm[idx][P_POS_IDX] += swarm[idx][P_VELOCITY_IDX]

        epoch += 1

    return swarm_best_cost
