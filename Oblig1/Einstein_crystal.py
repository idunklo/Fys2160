import numpy as np    
from scipy.special import factorial
import matplotlib.pyplot as plt   

def Omega(q, N):
    """ calculating number of microstates """
    omega = factorial(q + N - 1)/(factorial(q) * factorial(N-1))  
    return omega

def Omega_tot(q, N_A, N_B): 

    """ calculating number of microstates for
    several macrostates """

    omega_sum = 0
    
    q_A = np.arange(q+1)
    q_B = q - q_A    

    omega_A = Omega(q_A, N_A)
    omega_B = Omega(q_B, N_B)

    omega_tot = omega_A * omega_B

    omega_sum = np.sum(omega_tot)

    return q_A, omega_tot, omega_sum
                          
def prob_plot(q = 100, N_A = 50, N_B = 50):
    """calculates and plots the probability"""  

    q_A, omega_tot, omega_sum = Omega_tot(q, N_A, N_B)
    omega_prob = omega_tot/omega_sum 

    plt.plot(q_A, omega_prob)
    plt.xlabel("macrostates, q_A")
    plt.ylabel("probability")
    plt.savefig("part1.png")
    plt.show()
    
    
    


# Omega_tot(6, 2, 2)  

# print Omega(5,2) * Omega(1,2)  

prob_plot()





    




