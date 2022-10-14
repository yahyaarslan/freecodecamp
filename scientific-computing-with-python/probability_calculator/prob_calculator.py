import random
import copy
#


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, num):
        if num >= len(self.contents):
            return self.contents
        else:
            balls = []
            for i in range(num):
                ball = random.choice(self.contents)
                balls.append(ball)
                self.contents.remove(ball)
            return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_no_of_balls = []
    successes = 0

    # create a list of expected balls
    for key in expected_balls:
        expected_no_of_balls.append(expected_balls[key])
    
    # run the experiment
    for i in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        balls = new_hat.draw(num_balls_drawn)

        no_of_balls = []

        # create a list of balls drawn
        for key in expected_balls:
            no_of_balls.append(balls.count(key))

        # check if the list of balls drawn is equal to the list of expected balls
        if no_of_balls >= expected_no_of_balls:
            successes += 1

    # calculate the probability    
    probability = successes / num_experiments
    return probability


