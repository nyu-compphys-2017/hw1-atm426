import numpy as np
import matplotlib.pyplot as plt

def main():

    freq, volts = load_data()
    
    plot_shit(freq, volts)
    
def load_data():

    data = np.genfromtxt('millikan.txt')
    
    volts = data[:,1] ; freq = data[:,0]

    return freq, volts

def plot_shit(freq, volts):

    plt.title(r'V vs $\nu$')
    plt.xlabel(r'$\nu$ [hertz]') ; plt.ylabel('V [volts]')
    plt.plot(freq, volts, 'ko')
    plt.show()
    plt.close('all')



