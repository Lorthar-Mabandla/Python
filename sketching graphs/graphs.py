"""
    *************************************************************************************************************
                    file name:  class_graphs.py
                    Purpose:    plotting exponential graphs (Computational Modelling)
                    Date:       03 April 2019
                    Author:     Lorthar Mabandla

                    Equations:  y  = Ae^(xB)     B = 0.2, A = 10
                                y1 = 30e^(0.4x)
                                y2 = 30e^(-x)
    *************************************************************************************************************
"""
import numpy
import matplotlib.pyplot

A = 10
B = 0.2

x = numpy.linspace(-0.5,1.5,500)

y  = A*numpy.exp(B*x)
y1 = 30*numpy.exp(0.4*x)
y2 = 30*numpy.exp(-x)

matplotlib.pyplot.plot(x,y,  label = " y = Ae^(xB)")
matplotlib.pyplot.plot(x,y1, label = "y1 = 30e^(0.4x)")
matplotlib.pyplot.plot(x,y2, label = "y2 = 30e(-x)")

matplotlib.pyplot.xlabel("$x$")
matplotlib.pyplot.ylabel("$\exp(x)$")
matplotlib.pyplot.legend()

matplotlib.pyplot.show()
