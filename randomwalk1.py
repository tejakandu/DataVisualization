from random import choice

class randomwalk1():
    def __init__(self,num_points = 5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values)<self.num_points:

                x_direction = choice[-1,1]
                x_step = choice[0,1,2,3,4]
                x_distance = x_step+x_direction

                y_direction = choice[-1, 1]
                y_step = choice[0, 1, 2, 3, 4]
                y_distance = self.y_step + self.y_direction


                if x_distance == 0 and self.y_distance == 0 :
                    continue

                next_x = self.x_values[-1] + x_step
                next_y = self.y_values[-1] + self.y_step

                self.x_values.append(next_x)
                self.y_values.append(next_y)