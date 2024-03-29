import numpy as np
import matplotlib.pyplot as plt
from ODE_Utils import *

def plot_sols(plot_sets):
    for plot_set in plot_sets:
        xs = [item[0] for item in plot_set[1]]
        plt.plot(plot_set[0], xs, label= plot_set[2])

    #plt.plot(np.linspace(0, 1, 100), np.exp(np.linspace(0, 1, 100)), label='Actual')
    plt.legend()
    plt.grid()
    #plt.yscale('log')
    plt.show()

def deriv_plot(plot_sets):
    for plot_set in plot_sets:
        xs = [item[0] for item in plot_set[1]]
        ys = [item[1] for item in plot_set[1]]
        plt.plot(ys, xs, label= plot_set[2])

    #plt.plot(np.linspace(0, 1, 100), np.exp(np.linspace(0, 1, 100)), label='Actual')
    plt.legend()
    plt.grid()
    #plt.yscale('log')
    plt.ylabel('xdot')
    plt.xlabel('x')
    plt.show()

def plot_errs(stepsize, err):
    plt.plot(stepsize, err)
    plt.yscale('log')
    plt.xscale('log')
    plt.show()

# set up the ode system in one python function
# must return as numpy array to work with
def dvdt(t, vect):
    x = vect[0]
    y = vect[1]
    return np.array([y, -x])

# Declare list of possible step sizes
steps = [0.1, 0.01, 0.001, 0.0001]
methods = ['Euler', 'RK4'] # List of methods to compare
solutions = []

for method in methods:
    tls, sols = solve_ode(dvdt, 0, 50, np.array([1, 0]), steps, method)
    # errs = [get_abs_err_av(tls[i], sols[i], f_actual) for i in range(len(tls))]
    # plot_errs(steps, errs)

    for i in range(len(tls)):
        # name = str(method) + ' ' + str(steps[i]) + '   Error: ' + str(get_abs_err_av(tls[i], sols[i], f_actual))
        name = str(method) + ' ' + str(steps[i])
        solutions.append([tls[i], sols[i], name])

#plot_sols(solutions)
deriv_plot(solutions)
