"""
NOTE: You are only allowed to edit this file between the lines that say:
    # START EDITING HERE
    # END EDITING HERE

You need to complete the following methods:
    - give_pull(self): This method is called when the algorithm needs to
        select the arms to pull for the next round. The method should return
        two arrays: the first array should contain the indices of the arms
        that need to be pulled, and the second array should contain how many
        times each arm needs to be pulled. For example, if the method returns
        ([0, 1], [2, 3]), then the first arm should be pulled 2 times, and the
        second arm should be pulled 3 times. Note that the sum of values in
        the second array should be equal to the batch size of the bandit.
    
    - get_reward(self, arm_rewards): This method is called just after the
        give_pull method. The method should update the algorithm's internal
        state based on the rewards that were received. arm_rewards is a dictionary
        from arm_indices to a list of rewards received. For example, if the
        give_pull method returned ([0, 1], [2, 3]), then arm_rewards will be
        {0: [r1, r2], 1: [r3, r4, r5]}. (r1 to r5 are each either 0 or 1.)
"""

import numpy as np

# START EDITING HERE
# You can use this space to define any helper functions that you need.
def KL(x, y):
    return (x * np.log(1e-9 + x / (y + 1e-9)) + (1 - x) * np.log(1e-9 + (1 - x) / (1 - y + 1e-9)))
# END EDITING HERE

class AlgorithmBatched:
    def __init__(self, num_arms, horizon, batch_size):
        self.num_arms = num_arms
        self.horizon = horizon
        self.batch_size = batch_size
        assert self.horizon % self.batch_size == 0, "Horizon must be a multiple of batch size"
        # START EDITING HERE
        # Add any other variables you need here
        self.ucb_kl = np.zeros(self.num_arms)
        self.u = np.zeros(self.num_arms)
        self.p = np.zeros(self.num_arms)
        # END EDITING HERE
    
    def give_pull(self):
        # START EDITING HERE

        if np.sum(self.u) == 0:

            arr = np.arange(self.num_arms)
            np.random.shuffle(arr)
            arms_list = []

            if self.batch_size < self.num_arms:
                for i in range(self.batch_size):
                    arms_list.append(arr[i])

                pulls_list = np.ones(self.batch_size, dtype = int)

            else:
                for i in range(self.num_arms):
                    arms_list.append(arr[i])

                pulls_list = np.zeros(self.num_arms, dtype = int)

                bs = self.batch_size
                while (bs >= self.num_arms):
                    bs -= self.num_arms
                    for j in range(self.num_arms):
                        pulls_list[j] += 1
                
                rem_size = bs
                for k in range(rem_size):
                    pulls_list[k] += 1

            return arms_list, pulls_list

        else:
            if self.batch_size < self.num_arms:
                m = np.random.randint(1, self.batch_size)
            else:
                m = np.random.randint(1, self.num_arms)

            ucb_highest = np.argsort(self.ucb_kl)[::-1][:m]

            s_2 = 0
            for i in range(m):
                s_2 += self.ucb_kl[ucb_highest[i]]

            num_pulls = np.zeros(m, dtype = int)
            for j in range(m - 1):
                num_pulls[j] = int(np.ceil((self.ucb_kl[ucb_highest[j]] / s_2) * self.batch_size))
            num_pulls[m - 1] = int(self.batch_size - np.sum(num_pulls))

            return ucb_highest, num_pulls
        # END EDITING HERE
    
    def get_reward(self, arm_rewards):
        # START EDITING HERE
        self.arm_indexes = list(arm_rewards.keys())
        self.rewards = list(arm_rewards.values())

        for i in range(len(self.arm_indexes)):
            for j in range(len(self.rewards[i])):
                self.u[self.arm_indexes[i]] += 1
                n = self.u[self.arm_indexes[i]]

                value = self.p[self.arm_indexes[i]]
                new_value = ((n - 1) / n) * value + (1 / n) * self.rewards[i][j]
                self.p[self.arm_indexes[i]] = new_value

        for k in range(self.num_arms):
            tolerance = 0.1
            imax = 1
            imin = self.p[k]
            q = self.p[k]
            check = self.p[k]
            while((imax - imin) > tolerance):
                val = self.u[k] * KL(self.p[k], check) <= np.log(1e-9 + np.sum(self.u)) + 3 * np.log(1e-9 + np.log(1e-9 + np.sum(self.u)))
                if(val):
                    q = check
                    imin = check
                else:
                    imax = check
                check = (imax + imin) / 2

            self.ucb_kl[k] = q
        # END EDITING HERE
