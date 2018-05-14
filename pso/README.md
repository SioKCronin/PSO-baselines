# Particle Swarm Optimization (PSO)

Particle Swarm Optimization (PSO) is a stochastic population-based
optimization method. There are two key methods that each handle
information exchange differently, local best and global best, and both
are implemented here. Both methods begin by initializing a swarm of
"particles" (randomly assigned vectors) that will canvas the solutions
landscape across a number of iterations, wich velocities updated between
iterations based on the updating procedure defined by the method.

## Global Best PSO

In Global Best, velocities are updated by comparing personal historical bests
(the positions visited by the particle that yield the most optimal
results) with historical global bests. The weighting of each is
determined by scalar multiples (cognitive factor and social factor)
that are defined during intitialization.

### Mean cost of 20 runs

|Function|  Mean cost |
|--- |---|
|  Sphere | 4.6114e-003|
|  Rosenbrock | 1.0707e+000 |
|  Ackley | 1.3570e-001 |
|  Griewank | 2.0263e-003 |
|  Rastrigin | 9.4401e-001 |
|  Weierstrass | 4.5357e-001 |

## Local Best PSO

In Local Best, velocities are updated by comparing personal historical bests
(the positions visited by the particle that yield the most optimal
results) with historical bests from neighboring particles. The weighting of each is
determined by scalar multiples (cognitive factor and social factor)
that are defined during intitialization. There are different approaches
one can take in defining a neighbor in this context, yet common practice
is to use either L1 distance (Manhattan) or L2 distance (Euclidean).

### Mean cost of 20 runs

|Function|  Mean cost |
|--- |---|
|  Sphere | 2.4401e-004 |
|  Rosenbrock | 7.4795e-001 |
|  Ackley | 1.5596e-003 |
|  Griewank | 2.0057e-004 |
|  Rastrigin | 7.4248e-001 |
|  Weierstrass | 4.8002e-001|
