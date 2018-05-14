# Unified PSO

import numpy as np
from random import shuffle
from common.utils.distance import euclideanDistance, getNeighbors

def unified_pso(n, dims, c1, c2, w, u, k, mu, std, weight,
                           iters, obj_func, val_min, val_max):

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

    for particle in range(n):
        pos = np.random.uniform(val_min, val_max, dims)
        velocity = np.random.uniform(val_min, val_max, dims)
        p_best_pos = np.random.uniform(val_min, val_max, dims)
        if obj_func.__name__ == 'rosenbrock_func':
            p_best_cost = obj_func(p_best_pos, p_best_pos)
        else:
            p_best_cost = obj_func(p_best_pos)

        swarm.append([pos, velocity, p_best_pos, p_best_cost])

    x = 0

    while x < iters:
        for idx, particle in enumerate(swarm):
            if obj_func.__name__ == 'rosenbrock_func':
                if idx == len(swarm) - 1:
                    pass
                else:
                    current_cost = obj_func(particle[P_POS_IDX], swarm[idx + 1][P_POS_IDX])
            else:
                current_cost = obj_func(particle[P_POS_IDX])
            personal_best_cost = swarm[idx][P_BEST_COST_IDX]
            if current_cost < personal_best_cost:
                swarm[idx][P_BEST_POS_IDX] = swarm[idx][P_POS_IDX]
                swarm[idx][P_BEST_COST_IDX] = current_cost

            # Update global best
            if personal_best_cost < swarm_best_cost:
                swarm_best_cost = personal_best_cost
                swarm_best_pos = swarm[idx][P_BEST_POS_IDX]

            # Update local best
            best_neighbors = getNeighbors(particle[P_BEST_POS_IDX], swarm, k)
            best_cost = particle[P_BEST_COST_IDX]
            best_pos = particle[P_BEST_POS_IDX]
            for y in range(len(best_neighbors)):
                if swarm[y][P_BEST_COST_IDX] < best_cost:
                    best_pos = swarm[y][P_BEST_POS_IDX]

            # Compute velocity
            cognitive = (c1 * np.random.uniform(0, 1, 2)) * (swarm[idx][P_BEST_POS_IDX] - swarm[idx][P_POS_IDX])
            social_global = (c2 * np.random.uniform(0, 1, 2)) * (swarm_best_pos - swarm[idx][P_POS_IDX])
            social_local = (c2 * np.random.uniform(0, 1, 2)) * (best_pos - swarm[idx][P_POS_IDX])
            if weight == g:
                unified = np.random.normal(mu, std, dims) * u * social_global \
                          + (1-u) * social_local
            else:
                unified = u * social_global + \
                        np.random.normal(mu, std, dims) * (1-u) * social_local
            velocity = (w * swarm[idx][P_VELOCITY_IDX]) + unified
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

        x += 1

    return swarm_best_cost
