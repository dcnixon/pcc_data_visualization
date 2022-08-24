import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x ** 3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# use kwarg c to set colour, s to set dot size
# c takes names or RGB (as a tuple) where closer to 0 makes dark and 1 make lighter
# using a colour map to assign colours based on y_values
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and axis labels
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=10)

# Set the range for each axis
ax.axis([0, max(x_values) * 1.1, 0, max(y_values) * 1.1])

plt.show()
