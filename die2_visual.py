# from die2 import die
# import pygal
#
# die1 = die()
# die2 = die()
#
# results = []
#
# for roll_num in range(10000):
#     result = die1.roll() + die2.roll()
#
#     results.append(result)
#
# print(results)
#
# frequencies = []
# max_result = die1.num_sides+die2.num_sides
# # print(max_result)
# for values in range(2,max_result+1):
#     frequency = results.count(values)
#     frequencies.append(frequencies)
#
# hisst = pygal.Bar()
#
# hisst.title = "results of rolling two dice 1000 times"
# hisst.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
# # hist.y_labels = frequencies
# hisst.y_title = "frequency of result"
# hisst.add('d6+d6',frequencies)
# hisst.render_to_file('diejjj_visual.svg')





from matplotlib import pyplot as plt
import pygal
from die2 import die

die1 = die()
die2 = die()

results = []

for roll_num in range(1000):
    result = die1.roll()+die2.roll()
    results.append(result)

print(results)


frequencies = []
max_result = die1.num_sides+die2.num_sides

for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

hist = pygal.Bar()

hist._title = "result of rolling two d6 + d6 dice 1000 times"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "results"
# hist.y_labels = "frequency of result"
hist.add('d6+d6',frequencies)
hist.render_to_file('2 die_visual.svg')