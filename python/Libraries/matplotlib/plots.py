import matplotlib.pyplot as plt

# Create plot along points y=1,2,3
plt.plot([1,2,3])

# Create subplot with 2x1 (row x col) dimensions, labeled plot 1
plt.subplot(211)

# Set x range of plot ro 12
plt.plot(range(12))

# Create a 2nd subplot, 2x1 dimensions, labeled as plot 2 (below plot 1)
# background of plot will be yellow
plt.subplot(212, axisbg='y') 

# show the plots
plt.show()

