# Common methods
import numpy as np

def render_to_main(data):
    title = data[0]
    desc = data[1]
    dictionary = data[2]

    print """
        {}
        =======
    """.format(title)
    print """
        {}
    """.format(desc)

    for d in dictionary:
        print """
            {} : {}""".format(d, dictionary[d])

    return dictionary

def average_returns(*arg):
    periodic_returns = []
    for x in xrange(1, len(arg[0])):
        monthly_returns.append(
        100*((arg[0][x] - arg[0][x-1])/arg[0][x-1]))
    average_m = np.average(monthly_returns)

    return average_m*arg[1]
