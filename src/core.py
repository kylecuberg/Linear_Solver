import numpy as np


class lin_solver:
    def __init__(self, x, y, names=[], print_it=True):
        self.x_l = len(x)
        self.x_w = len(x[0])
        self.y_l = len(y)

        if self.x_l == self.x_w and self.x_l == self.y_l:
            if len(names) == len(x):
                self.names = names
            else:
                self.names = [None] * len(x)

            answer = list(np.linalg.inv(x).dot(y))

            if print_it:
                for var in answer:
                    a = answer.index(var)
                    print(self.names[a], answer[a])
        else:
            print(f"{self.x_l} by {self.x_w} matrix with {self.y_l} was input. All must be equal to work")


if __name__ == "__main__":
    """[summary]"""
    y = [10 * 5, 60 * 5, 20 * 5, 4 * 5, 0, 7 * 5, 24000]

    """ c       Y1  Y2  Y3  Y4  Y5  Y6"""
    x = [
        [
            1.667,
            -1,
            0,
            0,
            0,
            0,
            0,
        ],
        [
            2.5,
            0,
            -1,
            0,
            0,
            0,
            0,
        ],
        [
            2.333,
            0,
            0,
            -1,
            0,
            0,
            0,
        ],
        [
            3.5,
            0,
            0,
            0,
            -1,
            0,
            0,
        ],
        [
            4,
            0,
            0,
            0,
            0,
            -1,
            0,
        ],
        [
            2,
            0,
            0,
            0,
            0,
            0,
            -1,
        ],
        [
            0,
            1,
            1,
            1,
            1,
            1,
            1,
        ],
    ]

    vars = ["c", "y1", "y2", "y3", "y4", "y5", "y6"]

    lin_solver(x=x, y=y, names=vars, print_it=True)
