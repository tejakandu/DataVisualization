from random import choice


class randomwalk():
    """A class to generate random walk"""

    def __init__(self,num_points = 50000):
        """initialize attribute of a walk"""
        self.num_points = num_points

        # all walks start at 0,0
        self.x_values = [0]
        self.y_values = [0]



    def fill_walk(self):
        """calculate all the points in the walk"""
        # keep taking the steps until the desired points are reached
        while len(self.x_values) <self.num_points:
            # decide which direction to move and how far to go in that directin
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction*x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # reject move that go nowhere
            if x_step == 0 and y_step == 0:
                continue
            # calculate the next x_step and next y_step
            next_x = self.x_values[-1]+x_step
            next_y = self.y_values[-1]+y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)