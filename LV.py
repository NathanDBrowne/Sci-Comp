from loguru import logger
import numpy as np
import matplotlib.pyplot as plt
from ODE_Utils import *

#set up the ode system in one function
def dvdt(t, vect):

    a = 1
    d = 0.1

    x = vect[0]
    y = vect[1]

    dxdt = x*(1-x) - a*x*y/(d+x)
    dydt = b*y*(1- (y/x))

    return np.array([dxdt, dydt])

@logger.catch
def main():

    global b
    b = 0.1

    # solve the system
    tl, vl = solve_to(dvdt, 0, 150, [.3, .3], 0.001)
    vl = np.transpose(vl) # transpose to manipulate as we please

    # find start conds and period of a periodic orbit
    period, start_conds = isolate_orbit(tl, vl)
    print('Period: ', period)

    #### PLOT system wrt time
    plt.plot(tl, vl[0], label='Prey')
    plt.plot(tl, vl[1], label='Predator')
    plt.ylabel('Population')
    plt.xlabel('Time')
    plt.grid()
    plt.title('Lotka-Volterra, b = 0.1, no shoot')
    plt.legend()
    plt.show()

    #### PLOT orbit
    plt.plot(vl[0], vl[1], label='Orbit')
    plt.xlabel('Prey')
    plt.ylabel('Predator')
    plt.title('Phase portrait b = 0.1, no shoot')
    plt.grid()
    plt.show()

    # guess the right ICs
    guess = [.3, .3]
    # find the right ICs that lead to the same period orbit as earlier
    ics = shoot_ics(dvdt, period, guess)
    print('\nClosest ICs:')
    print('Prey:', ics[0], ' Pred: ', ics[1])

    # solve the system with new ICs
    tl, vl = solve_to(dvdt, 0, 150, ics, 0.001)
    vl = np.transpose(vl) # transpose to manipulate as we please

    #### PLOT system wrt time
    plt.plot(tl, vl[0], label='Prey')
    plt.plot(tl, vl[1], label='Predator')
    plt.ylabel('Population')
    plt.xlabel('Time')
    plt.grid()
    plt.title('Lotka-Volterra, b = 0.1 with shot ICs')
    plt.legend()
    plt.show()

    #### PLOT orbit
    plt.plot(vl[0], vl[1], label='Orbit')
    plt.xlabel('Prey')
    plt.ylabel('Predator')
    plt.title('Phase portrait b = 0.1 with shot ICs')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()