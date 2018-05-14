import numpy as np
import math
import sys
sys.path.append('../')
from pso.local_best_pso import local_best_pso
from common.functions.single_objective import *

# Run Local Best PSO 20 times on each function and take an average

def run_20(n, dims, c1, c2, w, k, iters, obj_func):
    '''
    n: Number of particles in swarm
    dims: Number of dimensions
    c1: Cognitive weight (how much each particle references their memory)
    c2: Social weight (how much each particle references swarm/group memory)
    w: Velocity weight
    k: number of nearest neighbors to evaluate
    iters: Number of iterations
    '''
    vals = []
    for i in range(20):
        vals.append(local_best_pso(n, dims, c1, c2, w, k, iters, obj_func))
    print("Mean value:",np.mean(vals))

algo = local_best_pso

def run_20(n, dims, c1, c2, w, k, iters, obj_func, val_min, val_max):
    '''
    n: Number of particles in swarm
    dims: Number of dimensions
    c1: Cognitive weight (how much each particle references their memory)
    c2: Social weight (how much each particle references swarm/group memory)
    w: Velocity weight
    iters: Number of iterations
    '''
    vals = []
    for i in range(20):
        vals.append(algo(n, dims, c1, c2, w, k, iters, obj_func,\
                                            val_min, val_max))
    print("Mean value:",np.mean(vals))

def run_all_tests(obj_func, val_min, val_max):
    n = 30
    dims = 2
    c1 = 0.5
    c2 = 0.3
    w = 0.9
    k = 4
    iters = 2000

    print("--------------------------")
    print("Testing %s" %obj_func)
    print("Single run test:", algo(n, 2, c1, c2, w, k, iters, obj_func,\
                                                   val_min, val_max))
    print("Run 20:", run_20(n, 2, c1, c2, w, k, iters, obj_func, \
                                                   val_min, val_max))

run_all_tests(sphere_func, -5.12, 5.12)
run_all_tests(rosenbrock_func, -2.048, 2.048)
run_all_tests(ackley_func, -32.768, 32.768)
run_all_tests(griewank_func, -600, 600)
run_all_tests(rastrigin_func, -5.12, 5.12)
run_all_tests(weierstrass_func, -0.5, 0.5)
