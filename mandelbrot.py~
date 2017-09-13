import numpy as np
import matplotlib.pyplot as plt

def main(S, N):

    """ makes a density plot of the Mandelbrot set
    S : number of iteration steps for each point
    N : grid size """

    point_count(N, S)

def make_grid(N):
    
    """ makes two grids of N evenly spaced points for x & y
    where -2 <= x, y <= 2 """

    x = np.linspace(-2. , 2 , N)
    y = np.linspace(-2. , 2 , N)
    
    return x, y

def point_count(N, S):

    """ for each point, counts how many times z' is in the set
    given xi and yi """

    x, y = make_grid(N)

    xc, yc = np.zeros_like(x), np.zeros_like(y)

    
    for (xi, i) in zip(x, xrange(N)):
        for (yi, j) in zip(y, xrange(N)):

            z = 0 ; s = 0
            c = complex( xi , yi ) 
            abs_z = np.sqrt( z*z.conjugate() )
            eps = 10**-12

            for k in xrange(S):
                
                if abs_z > 2:
                    break
                else:
                    z_prim = z*z + c
                    abs_z = np.sqrt( z_prim*z_prim.conjugate() )
                    z = z_prim 
                    s += 1

            if abs_z < 2:
                xc[i] += 1
                yc[j] += 1
                

    return xc, yc







