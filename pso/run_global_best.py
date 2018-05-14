import numpy as np
import math
import sys
sys.path.append('../')
from pso.global_best_pso import global_best_pso
from common.functions.single_objective import *

def run_all_tests(algo, n, dims, c1, c2, w, iters):

    def run_20(algo, n, dims, c1, c2, w, iters, obj_func, val_min, val_max):
        vals = []
        for i in range(20):
            vals.append(algo(n, dims, c1, c2, w, iters, obj_func,\
                                                val_min, val_max))
        return np.mean(vals)

    funcs = [[sphere_func, -5.12, 5.12],
             [rosenbrock_func, -2.048, 2.048],
             [ackley_func, -32.768, 32.768],
             [griewank_func, -600, 600],
             [rastrigin_func, -5.12, 5.12],
             [weierstrass_func, -0.5, 0.5]]

    for func in funcs:
        print("--------------------------")
        print("Testing %s" %func[0])
        print("Single run test:", algo(n, dims, c1, c2, w, iters, func[0],\
                                                       func[1], func[2]))
        print("Run 20:", run_20(algo, n, dims, c1, c2, w, iters, func[0],\
                                                       func[1], func[2]))

run_all_tests(global_best_pso, n=30, dims=2, c1=0.5, c2=0.3, w=0.9, iters=2000)
