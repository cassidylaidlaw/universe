import numpy as np

class Hardcoded(object):
    def __init__(self, actions):
        self.actions = actions

    def contains(self, action):
        return action in self.actions

    def sample(self):
        i = np.random.randint(len(self.actions))
        return self.actions[i]

    def __getitem__(self, i):
        return self.actions[i]
