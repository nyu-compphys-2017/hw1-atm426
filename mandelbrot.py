import numpy as np
import matplotlib.pyplot as plt

def main(S, N):

    """ makes a density plot of the Mandelbrot set
    S : number of iteration steps for each point
    N : grid size """

    x, y = make_grid(N)
    # making grids

def check_man(z):

    """ checks z to see if it is in the Mandelbrot set """

    abs_z = sqrt( (z*z.conjugate()) )

    

def make_grid(N):
    
    """ makes two grids of N evenly spaced points for x & y
    where -2 <= x, y <= 2 """

    x = np.linspace(-2. , 2 , N)
    y = np.linspace(-2. , 2 , N)
    
    return x, y

def point_count(x, y):

    """ for each point, counts how many times z' is in the set
    given xi and yi """

    for xi in x:
        for yi in y:

            z = 0
            c = complex( xi , yi ) 
            
            
