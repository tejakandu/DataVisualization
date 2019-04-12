import matplotlib.pyplot as plt
from random_walk import randomwalk


# make a random walk and plot points
while True:
    rw = randomwalk()

    rw.fill_walk()
    plt.figure(dpi=128,figsize=(16, 10))
    point_number = list(range(rw.num_points))


    plt.scatter(rw.x_values,rw.y_values,c = point_number,edgecolors='none',s=1,cmap=plt.cm.Blues)

    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1], c='red', edgecolors='none', s=100)
    # plt.scatter(point_number,c='red')
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keeprunning = input("make another walk ? (y/n):")

    if keeprunning == "n":
          break


