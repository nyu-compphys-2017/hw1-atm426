import numpy as np
import matplotlib.pyplot as plt

def main(S, N):

    """ makes a density plot of the Mandelbrot set
    S : number of iteration steps for each point
    N : grid size """

    z_binary, z_density = point_count(N, S)

    extent = [-2, 2, -2, 2]
    plt.imshow(z_binary, extent=extent, cmap='Greys')
    plt.show()
    plt.close('all')

    log_zd = np.log10(z_density)
    plt.imshow(z_density, extent=extent, cmap='jet')
    plt.show()
    plt.close('all')

    log_zd = np.log10(z_density)
    plt.imshow(log_zd, extent=extent, cmap='jet')
    plt.show()
    plt.close('all')


    

def make_grid(N):
    
    """ makes two grids of N evenly spaced points for x & y
    where -2 <= x, y <= 2 """

    x = np.linspace(-2. , 2 , N)
    y = np.linspace(-2. , 2 , N)
    # two evenly spaced grids from -2 to 2

    return x, y

def point_count(N, S):

    """ for each point, counts how many times z' is in the set
    given xi and yi """

    x, y = make_grid(N)

    xc, yc = np.zeros_like(x), np.zeros_like(y)
    # grids for holding result of mandelbrot check
    
    z_binary = np.zeros( (N, N) )
    z_density = np.zeros( (N, N) )

    for (xi, i) in zip(x, xrange(N)):
        for (yi, j) in zip(y, xrange(N)):

            z = 0 ; s = 0
            c = complex( xi , yi ) 
            abs_z = np.sqrt( z*z.conjugate() )
            # initial values for z, c, |z|, and step count

            for k in xrange(S):

                if abs_z > 2:
                    break
                else:
                    z_prim = z*z + c
                    abs_z = np.sqrt( z_prim*z_prim.conjugate() )
                    z = z_prim 
                    s += 1
                    z_density[j, i] += 1
                


            if abs_z < 2:
                z_binary[j, i] = 1
                
    return z_binary, z_density







