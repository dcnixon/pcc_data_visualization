import matplotlib.pyplot as plt

from generate_data.random_walk import RandomWalk

while True:
    # Make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    x_values = rw.x_values
    y_values = rw.y_values

    plt.style.use('seaborn')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)

    # Show the path on a line graph
    ax.plot(x_values, y_values, linewidth=1)
    ax.plot(0, 0, c='green', linewidth=400)
    ax.plot(x_values[-1], y_values[-1], c='red', linewidth=400)
    # ax.scatter(x_values, y_values, c=point_numbers, cmap=plt.cm.Blues,
    #            edgecolors='none', s=5)
    #
    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(x_values[-1], y_values[-1], c='red',
               edgecolors='none', s=100)

    # Set chart title and axis labels
    ax.set_title("Random Walk", fontsize=24)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
