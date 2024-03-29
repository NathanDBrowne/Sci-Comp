from loguru import logger
import numpy as np
import matplotlib.pyplot as plt
from ODE_Utils3 import *

#set up the ode system in one function
def dvdt(t, vect, b=2., s=-1.):

    x = vect[0]
    y = vect[1]

    dxdt = b*x - y + s*x*(x**2 + y**2)
    dydt = x + b*y + s*y*(x**2 + y**2)

    return np.array([dxdt, dydt])

def sol(tl, phase, b=2., s=-1.):

    u1, u2 = [], []
    for t in tl:
        u1.append(np.sqrt(b) * np.cos(t + phase))
        u2.append(np.sqrt(b) * np.sin(t + phase))
    return np.transpose(np.array([u1, u2]))

#set up the ode system in one function
def dv2dt(t, vect, b=2., s=-1.):

    x, y, z = vect

    dxdt = b*x - y + s*x*(x**2 + y**2)
    dydt = x + b*y + s*y*(x**2 + y**2)
    dzdt = -1 * z

    return np.array([dxdt, dydt, dzdt])


def known_sol_test(tl, vl, phase, errtol=1e-02):
    u_actual = sol(tl, phase)

    closeness = np.isclose(vl, u_actual, atol=errtol)

    if False in closeness:
        print('KNOWN SOLUTION: Test failed')
    else:
        print('KNOWN SOLUTION: Test passed')

def test_3D_system():
    try:
        u0 = np.array([.1, .1, .1])
        tl, vl = solve_to(dv2dt, 0, 100, u0)

        shot = shoot_root(dv2dt, u0)

        tl, vl = solve_to(dv2dt, 0, shot.period, shot.ics)
        print('3D SYSTEM:      Test passed')

        #### PLOT system wrt time
        plt.plot(tl, vl[:, 0], label='x')
        plt.plot(tl, vl[:, 1], label='y')
        plt.plot(tl, vl[:, 2], label='z')
        plt.ylabel('Value')
        plt.xlabel('Time')
        plt.grid()
        plt.title('Test System')
        plt.legend()
        plt.show()

    except:
        print('3D SYSTEM:      Test failed')

def test_dimension_err():
    try:
        u0 = np.array([10, 10])
        shot = shooting(dv2dt, u0)
        ics = shot.ics
        period = shot.period
        tl, vl = solve_to(dv2dt, 0, period, ics)
        print('DIM ERR:        Test failed')
    except:
        print('DIM ERR:        Test passed')

@logger.catch
def main():

    # Known solution test
    u0 = np.array([.7, 1.])

    shot = shoot_root(dvdt, u0, plot=True)
    print('Period found: ', shot.period)
    tl, vl = solve_to(dvdt, 0, shot.period, shot.ics)

    phase = 0

    known_sol_test(tl, vl, phase)

    #### PLOT orbit
    plt.plot(vl[:, 0], vl[:, 1], label='Shot orbit')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Phase portrait')
    plt.grid()
    plt.legend()
    plt.show()

    ##########  3d test ############################################
    test_3D_system()

    test_dimension_err()


if __name__ == '__main__':
    main()
