#   Amirkabir Univesity of Technology
#   Department of Physics
#   Random Processes Course
#   Behnood Bandi - Aria Naieni - Amir Kermanshahani

import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np


def expon_pdf(x, lmabd=1):
    """PDF of exponential distribution."""
    return lmabd*np.exp(-lmabd*(x))
def expon_cdf(x, lambd=1):
    """CDF of exponetial distribution."""
    return 1 - np.exp(-lambd*x)
def expon_icdf(p, lambd=1):
    """Inverse CDF of exponential distribution - i.e. quantile function."""
    return -np.log(1-p)/lambd


dist = stats.expon()
x = np.linspace(0,4,200)
y = np.linspace(0,4,200)

plt.figure(figsize=(12, 4))
plt.subplot(121)
plt.plot(x, expon_cdf(x))
plt.axis([0, 4, 0, 1])
'''for q in [0.5, 0.8]:
    plt.arrow(0, q, expon_icdf(q) - 0.1, 0, head_width=0.05, head_length=0.1, fc='b', ec='b')
    plt.arrow(expon_icdf(q), q, 0, -q + 0.1, head_width=0.1, head_length=0.05, fc='b', ec='b')
'''
plt.ylabel('1: Generate a (0,1) uniform PRNG')
plt.xlabel('2: Find the inverse CDF')
plt.title('Inverse transform method');

plt.subplot(122)
u = np.random.random(10000)
v = expon_icdf(u)
plt.hist(v, histtype='step', bins=100, density=True, linewidth=2)
plt.plot(x, expon_pdf(x), linewidth=2)
plt.axis([0, 4, 0, 1])
plt.title('Histogram of exponential PRNGs');

plt.show()