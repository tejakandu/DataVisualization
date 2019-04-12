from matplotlib import pyplot as plt
import pygal
from die import Die

die = Die()

results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

print(results)


frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

hist = pygal.Bar()

hist._title = "result of rolling one d6 dice 1000 times"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "results"
# hist.y_labels = "frequency of result"
hist.add('d6',frequencies)
hist.render_to_file('die_visual.svg')