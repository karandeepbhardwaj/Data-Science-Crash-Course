import matplotlib.pyplot as plt
from normal_distribution import *




xs = [x / 10.0 for x in range(-50, 50)]

plt.plot(xs,[normal_pdf(x, sigma=1) for x in xs],
         '-',label='mu=0,sigma=1')

plt.plot(xs,[normal_pdf(x, sigma=2) for x in xs],
         '--',label='mu=0,sigma=2')

plt.plot(xs,[normal_pdf(x, sigma=0.5) for x in xs],
         ':',label='mu=0,sigma=0.5')

plt.plot(xs,[normal_pdf(x, mu=-1) for x in xs],
         '-.',label='mu=-1,sigma=1')

plt.legend()
plt.title("Various normal pdfs")
plt.show()