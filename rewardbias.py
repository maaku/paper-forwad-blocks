#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(-.25,.2505,.001)
v = 2 * t - 4 * t * t

plt.plot(t,v)
plt.xticks([-0.25,-0.15,-0.05,0,0.05,0.15,0.25])
plt.yticks([-0.75,-0.50,-0.25,0,.25])
plt.xlabel('Proof-of-Work Difficulty Bias (%)')
plt.ylabel('Block Reward Adjustment (%)')
plt.grid(True)
plt.savefig('rewardbias.eps',format='eps',dpi=1200)
