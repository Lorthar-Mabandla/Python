"""     Lorthar Mabandla
        Trial.py
        Plotting graphs in python
        equation : y = 30e^(0.4*x)
"""

#step 1 (import libraries)

import numpy
import matplotlib.pyplot

#step 2 (set x axis)

x = numpy.linspace(-1, 2, 50)

#step 3 (set y axis)

y = 30*numpy.exp(0.4*x)

#step 4 (plot graph)

matplotlib.pyplot.plot(x,y, label = 'y')

#step 5 (label the axis & legend)

matplotlib.pyplot.xlabel('$x$')
matplotlib.pyplot.ylabel('$exp(x)$')
matplotlib.pyplot.legend()

matplotlib.pyplot.show()

