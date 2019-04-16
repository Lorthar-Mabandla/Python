import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-1,2,50)
# -1 is the lower limit, 2 is the upperlimit, 50 is the number of segments in the lines, 
# the more the number of segments, the smoother the graph
y= 30*np.exp((0.4*x))
y1= 30*np.exp(-(1*x))
y2=10*np.exp((.2*x))

#just like any other graph, we change values in the y axis.
plt.plot(x, y,label='y')
# 'y' labels the respective graph.
plt.plot(x, y1,label='y1')
plt.plot(x, y2,label='y2')
plt.xlabel('$x$')
plt.ylabel('$\exp(x)$')
plt.legend()
plt.show() 
#legend is like the map, 
# .show shows the graph, graphics












