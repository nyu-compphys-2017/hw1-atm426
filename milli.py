import numpy as np
import matplotlib.pyplot as plt

def main():

    freq, volts = load_data()
    # load data from milikan.txt

    bf = best_fit(freq, volts)
    # calculate m, c and return best fit y-array

    plot_shit(freq, volts, bf)
    # plot shit
    
def load_data():

    data = np.genfromtxt('millikan.txt')
    
    volts = data[:,1] ; freq = data[:,0]
    # separating columns into correct values

    return freq, volts

def plot_shit(freq, volts, bf):
#plot shit

    plt.title(r'V vs $\nu$')
    plt.xlabel(r'$\nu$ [hertz]') ; plt.ylabel('V [volts]')
    plt.plot(freq, volts, 'ko')
    plt.plot(freq, bf, 'k--')
    plt.show()
    plt.close('all')


def best_fit(x, y):

    N = len(x)
    # number of points

    Ex = np.sum(x)/N ; Ey = np.sum(y)/N ; Exx = np.sum(x*x)/N ; Exy = np.sum(x*y)/N
    # quantities for best fit parameters

    m = (Exy - Ex*Ey) / (Exx - Ex*Ex) ; c = (Exx*Ey - Ex*Exy) / (Exx - Ex*Ex)
    # best fit parameters

    print 'slope = '+str(m)
    print 'intercept = '+str(c)

    bf = m*x + c
    # best fit line

    C = 1.602e-19 
    # charge of electron, coulombs

    print "planck's constant = "+str( m*C )+" [ m^2 kg s^-2 ]"

    h = 6.626e-34
    print "error = "+str( round((abs(m*C - h))/h, 3)*100 )+" %" 

    return bf
