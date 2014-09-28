import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli


T = 10000
n = 10
x = range(0, T)

def RandomWalk():
	S = np.zeros(T, np.dtype(int)) # create empty vector for values
	r = bernoulli.rvs(0.5, loc=0, size=T) # generate Bernouli Discrete Random Variables
	for i in x:
		if r[i] == 1:
			S[i] = S[i-1] + 1
		else:
			S[i] = S[i-1] - 1
	plt.plot(x,S)


for i in range(1,n):
	RandomWalk()

# Add title
plt.title('Discrete Random Walk - ' + str(n) + ' Paths')

# Display the chart
plt.show()