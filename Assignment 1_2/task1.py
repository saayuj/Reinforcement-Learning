"""
NOTE: You are only allowed to edit this file between the lines that say:
    # START EDITING HERE
    # END EDITING HERE

This file contains the base Algorithm class that all algorithms should inherit
from. Here are the method details:
    - __init__(self, num_arms, horizon): This method is called when the class
        is instantiated. Here, you can add any other member variables that you
        need in your algorithm.
    
    - give_pull(self): This method is called when the algorithm needs to
        select an arm to pull. The method should return the index of the arm
        that it wants to pull (0-indexed).
    
    - get_reward(self, arm_index, reward): This method is called just after the 
        give_pull method. The method should update the algorithm's internal
        state based on the arm that was pulled and the reward that was received.
        (The value of arm_index is the same as the one returned by give_pull.)

We have implemented the epsilon-greedy algorithm for you. You can use it as a
reference for implementing your own algorithms.
"""

import numpy as np
import math
# Hint: math.log is much faster than np.log for scalars

class Algorithm:
    def __init__(self, num_arms, horizon):
        self.num_arms = num_arms
        self.horizon = horizon
    
    def give_pull(self):
        raise NotImplementedError
    
    def get_reward(self, arm_index, reward):
        raise NotImplementedError

# Example implementation of Epsilon Greedy algorithm
class Eps_Greedy(Algorithm):
    def __init__(self, num_arms, horizon):
        super().__init__(num_arms, horizon)
        # Extra member variables to keep track of the state
        self.eps = 0.1
        self.counts = np.zeros(num_arms)
        self.values = np.zeros(num_arms)
    
    def give_pull(self):
        if np.random.random() < self.eps:
            return np.random.randint(self.num_arms)
        else:
            return np.argmax(self.values)
    
    def get_reward(self, arm_index, reward):
        self.counts[arm_index] += 1
        n = self.counts[arm_index]
        value = self.values[arm_index]
        new_value = ((n - 1) / n) * value + (1 / n) * reward
        self.values[arm_index] = new_value


# START EDITING HERE
# You can use this space to define any helper functions that you need
def KL(x, y):
    return (x * math.log(1e-9 + x / (y + 1e-9)) + (1 - x) * math.log(1e-9 + (1 - x) / (1 - y + 1e-9)))
# END EDITING HERE

class UCB(Algorithm):
    def __init__(self, num_arms, horizon):
        super().__init__(num_arms, horizon)
        # You can add any other variables you need here
        # START EDITING HERE
        self.ucb = np.zeros(self.num_arms)
        self.u = np.zeros(self.num_arms)
        self.p = np.zeros(self.num_arms)
        # END EDITING HERE
    
    def give_pull(self):
        # START EDITING HERE
        if np.sum(self.u) < self.num_arms:
            return int(np.sum(self.u))
        else:
            return np.argmax(self.ucb)
        # END EDITING HERE
    
    def get_reward(self, arm_index, reward):
        # START EDITING HERE
        self.u[arm_index] += 1
        n = self.u[arm_index]

        value = self.p[arm_index]
        new_value = ((n - 1) / n) * value + (1 / n) * reward
        self.p[arm_index] = new_value

        for i in range(self.num_arms):
            self.ucb[i] = self.p[i] + math.sqrt(2 * math.log(1e-9 + np.sum(self.u)) / (1e-9 + self.u[i]))
        # END EDITING HERE

class KL_UCB(Algorithm):
    def __init__(self, num_arms, horizon):
        super().__init__(num_arms, horizon)
        # You can add any other variables you need here
        # START EDITING HERE
        self.ucb_kl = np.zeros(self.num_arms)
        self.u = np.zeros(self.num_arms)
        self.p = np.zeros(self.num_arms)
        # END EDITING HERE
    
    def give_pull(self):
        # START EDITING HERE
        if np.sum(self.u) < self.num_arms:
            return int(np.sum(self.u))
        else:
            return np.argmax(self.ucb_kl)
        # END EDITING HERE
    
    def get_reward(self, arm_index, reward):
        # START EDITING HERE
        self.u[arm_index] += 1
        n = self.u[arm_index]

        value = self.p[arm_index]
        new_value = ((n - 1) / n) * value + (1 / n) * reward
        self.p[arm_index] = new_value

        for i in range(self.num_arms):
            tolerance = 0.05
            imax = 1
            imin = self.p[i]
            q = self.p[i]
            check = self.p[i]
            while((imax - imin) > tolerance):
                val = self.u[i] * KL(self.p[i], check) <= math.log(1e-9 + np.sum(self.u)) + 3 * math.log(1e-9 + math.log(1e-9 + np.sum(self.u)))
                if(val):
                    q = check
                    imin = check
                else:
                    imax = check
                check = (imax + imin) / 2

            self.ucb_kl[i] = q
        # END EDITING HERE


class Thompson_Sampling(Algorithm):
    def __init__(self, num_arms, horizon):
        super().__init__(num_arms, horizon)
        # You can add any other variables you need here
        # START EDITING HERE
        self.s = np.zeros(self.num_arms)
        self.f = np.zeros(self.num_arms)
        self.x = np.zeros(self.num_arms)
        # END EDITING HERE
    
    def give_pull(self):
        # START EDITING HERE
        if int(np.sum(self.s)) == 0 and int(np.sum(self.f)) == 0:
            return np.random.randint(self.num_arms)
        else:
            return np.argmax(self.x)
        # END EDITING HERE
    
    def get_reward(self, arm_index, reward):
        # START EDITING HERE
        if reward == 0:
            self.f[arm_index] += 1
        elif reward == 1:
            self.s[arm_index] += 1

        for i in range(self.num_arms):
            self.x[i] = np.random.beta(self.s[i] + 1, self.f[i] + 1)
        # END EDITING HERE
