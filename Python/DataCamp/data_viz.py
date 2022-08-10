## Intro Section 

import matplotlib.pyplot as plt
 
year = [1950,1970,1990,2010]
pop = [2.519,3.692,5.263,6.972]

plt.plot(year,pop)
plt.show()

## Scatter Plot

plt.scatter(year, pop)
plt.show()

### Plotting Data on a Logarithmic Scale

plt.xscale('log')
plt.show()


