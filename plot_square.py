import matplotlib.pyplot as plt

x_values = list(range(100))

y_values = [x**2 for x in x_values]

plt.plot(x_values,y_values,linewidth=5)

# Set the title and x and y labels

plt.tilte("Square",fontsize=25)

plt.xlabel("Values",fontsize=15)

plt.ylabel("Square values",fontsize=15)

plt.show()
