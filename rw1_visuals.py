from randomwalk1 import randomwalk1
from matplotlib import pyplot as plt

while True:
    rw = randomwalk1
    rw.fill_walk()
    point_numbers = list[range(rw.num_points)]
    plt.scatter(rw.x_values,rw.y_values,cmap=plt.cm.Blues,c= point_numbers)

    plt.show()
