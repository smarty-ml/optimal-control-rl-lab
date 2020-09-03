import numpy as np


class RegulatorProblem:
    def __init__(self, dt=0.001):
        self.done = False
        self.x_matrix = np.array(
            [[-0.2, 0.5, 0, 0, 0],
             [0, -0.5, 1.6, 0, 0],
             [0, 0, -1 / 7, 6 / 7, 0],
             [0, 0, 0, -0.25, 7.5],
             [0, 0, 0, 0, -0.1]])
        self.state = np.ones(5)
        self.u_vector = np.array([0, 0, 0, 0, 0.3])[np.newaxis].T
        self.dt = dt
        self.t = 0

    def reset(self):
        self.t = 0
        self.state = np.ones(5)
        self.done = False
        return self.state

    def step(self, u_action):
        u = u_action[0]
        state = self.state[np.newaxis].T
        dx = self.x_matrix.dot(state) + self.u_vector * u
        state = state + dx * self.dt
        self.t = self.t + self.dt
        self.state = state.reshape(state.shape[0])
        reward = (self.state[0] ** 2 + u ** 2) * self.dt
        return self.state, reward, int(self.done), None
