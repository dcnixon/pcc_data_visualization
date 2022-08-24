from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create D6 and D10 die_visual
die_1 = Die()
die_2 = Die()

# Make some rolls and store the results in a list.
results = [(die_1.roll() * die_2.roll()) for roll_num in range(50000)]
# for roll_num in range(50000):
#     result = die_1.roll() * die_2.roll()
#     results.append(result)

# Analyze the results.
max_result = max(results)
min_result = min(results)
frequencies = [results.count(value) for value in
               range(min_result, max_result + 1)]

# for value in range(min_result, max_result + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)


# Visualize the results.
x_values = list(range(min_result, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of multiplying the rolls of two D6 50,000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_times_d6.html')
