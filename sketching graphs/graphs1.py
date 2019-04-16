"""
    exponential graphs in python
    x = e^t
    x1 = e^(-t)

"""
import numpy
import matplotlib.pyplot

t= numpy.linspace(-1,1,500)
x = numpy.exp(t)
x1 = numpy.exp(-t)

matplotlib.pyplot.plot(t,x,label = "x = e^t")
matplotlib.pyplot.plot(t,x1,label = "x1 = e^(-t)")

matplotlib.pyplot.xlabel("$t$")
matplotlib.pyplot.ylabel("$\exp(t)$")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
