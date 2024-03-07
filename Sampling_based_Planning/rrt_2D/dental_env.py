"""
Environment for rrt_2D
@author: huiming zhou
"""

import numpy as np

class Env:
    def __init__(self):
        self.x_range = (0, 50)
        self.y_range = (0, 30)
        self.obs_boundary = self.obs_boundary()
        self.obs_circle = self.obs_circle()
        self.obs_rectangle = self.obs_rectangle()
        self.decay = self.decay()
        self.enamel = self.enamel()

    @staticmethod
    def decay():
        x = np.random.uniform(10, 20, 100)
        y = np.random.uniform(10, 20, 100)
        decay = np.column_stack((x, y))
        return decay

    @staticmethod
    def enamel():
        x = np.random.uniform(10, 25, 100)
        y = np.random.uniform(5, 10, 100)
        enamel1 = np.column_stack(x, y)
        x = np.random.uniform(10, 25, 100)
        y = np.random.uniform(20, 25, 100)
        enamel2 = np.column_stack(x, y)
        x = np.random.uniform(20, 25, 100)
        y = np.random.uniform(10, 20, 100)
        enamel3 = np.column_stack(x, y)
        enamel = np.column_stack((enamel1, enamel2, enamel3))
        return enamel

    @staticmethod
    def obs_boundary():
        obs_boundary = [
            [0, 0, 1, 30],
            [0, 30, 50, 1],
            [1, 0, 50, 1],
            [50, 1, 1, 30]
        ]
        return obs_boundary

    @staticmethod
    def obs_rectangle():
        obs_rectangle = [
            [14, 12, 8, 2],
            [18, 22, 8, 3],
            [26, 7, 2, 12],
            [32, 14, 10, 2]
        ]
        return obs_rectangle

    @staticmethod
    def obs_circle():
        obs_cir = [
            [7, 12, 3],
            [46, 20, 2],
            [15, 5, 2],
            [37, 7, 3],
            [37, 23, 3]
        ]

        return obs_cir
