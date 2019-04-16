# y1 = 5e^(2x), y2 = 5e^(-2x)

import numpy
import matplotlib.pyplot

x = numpy.linspace(-1, 1, 500)

y1= 5*numpy.exp(2*x)
y2= 5*numpy.exp(-2*x)

matplotlib.pyplot.plot(x,y1, label = 'y1 = 5e^(2x)')
matplotlib.pyplot.plot(x,y2, label = "y2 = 5e^(-2x)")

matplotlib.pyplot.xlabel('$x$')
matplotlib.pyplot.ylabel('$\exp(x)$')
matplotlib.pyplot.legend()

matplotlib.pyplot.show()
