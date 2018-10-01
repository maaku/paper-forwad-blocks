#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

t = np.arange(0.0, 210000*6+0.5)
t /= 144 * 365.25
h = [50.0/(2**i) for i in range(10)]
f = [interp1d(np.asarray([period,period+2])*210000,
              np.asarray([h[period]-h[period+1],0]),
              kind="linear")
     for period in range(len(h)-1)]

sold = []
snew = []
for i in range(0, 210000*6+1):
    period = i // 210000;
    sold.append(h[period])
    snew.append(0.0)
    if period > 0:
        snew[-1] += f[period-1](i)
    snew[-1] += f[period](i)
    snew[-1] += h[period+1]

TODAY = 543744

plt.plot(t,sold)
plt.plot(t,snew)
plt.plot(np.asarray([t[TODAY],]),
         np.asarray([(sold[TODAY]+snew[TODAY])/2]), 'D')
plt.legend(['Satoshi','Linear Interp.','1 Oct 2018'], loc='best')
plt.xlabel('Time (years)')
plt.ylabel('Subsidy (bitcoin)')
plt.savefig('subsidycurve.eps',format='eps',dpi=1200)

print('sum(sold) = %f' % sum(sold))
print('sum(snew) = %f' % sum(snew))
