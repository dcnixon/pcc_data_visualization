from generate_data.random_walk import RandomWalk
import plotly.express as px


# Make a random walk
rw = RandomWalk()
rw.fill_walk()

x_values = rw.x_values
y_values = rw.y_values

fig = px.line(x=x_values, y=y_values, title='Random Walk in Plotly')
fig.show()