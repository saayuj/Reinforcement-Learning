from importlib.resources import path
from gym_driving.assets.car import *
from gym_driving.envs.environment import *
from gym_driving.envs.driving_env import *
from gym_driving.assets.terrain import *

import time
import pygame, sys
from pygame.locals import *
import random
import math
import argparse

# Do NOT change these values
TIMESTEPS = 1000
FPS = 30
NUM_EPISODES = 10

class Task1():

    def __init__(self):
        """
        Can modify to include variables as required
        """
        self.orientation = False
        super().__init__()

    def next_action(self, state):
        """
        Input: The current state
        Output: Action to be taken
        TO BE FILLED
        """

        # Replace with your implementation to determine actions to be taken

        x = state[0]
        y = state[1]
        velocity = state[2]
        heading_angle = state[3]

        target_angle = math.atan(- y / (350 - x)) * (180 / math.pi)
        if target_angle < 0:
            target_angle += 360

        if abs(heading_angle - target_angle) <= abs(360 - abs(heading_angle - target_angle)):
            error = heading_angle - target_angle
        else:
            if heading_angle >= target_angle:
                error = - (360 - heading_angle + target_angle)
            else:
                error = 360 + heading_angle - target_angle

        if velocity == 0:
            self.orientation = False

        if abs(error) > 4 and not self.orientation:
            if error < 0:
                action_steer = 2
                action_acc = 2
            else:
                action_steer = 0
                action_acc = 2
        else:
            self.orientation = True

        if self.orientation:
            action_steer = 1
            action_acc = 4

        action = np.array([action_steer, action_acc])  

        return action

    def controller_task1(self, config_filepath=None, render_mode=False):
        """
        This is the main controller function. You can modify it as required except for the parts specifically not to be modified.
        Additionally, you can define helper functions within the class if needed for your logic.
        """
    
        ######### Do NOT modify these lines ##########
        pygame.init()
        fpsClock = pygame.time.Clock()

        if config_filepath is None:
            config_filepath = '../configs/config.json'

        simulator = DrivingEnv('T1', render_mode=render_mode, config_filepath=config_filepath)

        time.sleep(3)
        ##############################################

        # e is the number of the current episode, running it for 10 episodes
        for e in range(NUM_EPISODES):
        
            ######### Do NOT modify these lines ##########
            
            # To keep track of the number of timesteps per epoch
            cur_time = 0

            # To reset the simulator at the beginning of each episode
            state = simulator._reset()
            
            # Variable representing if you have reached the road
            road_status = False
            ##############################################

            # The following code is a basic example of the usage of the simulator
            for t in range(TIMESTEPS):
        
                # Checks for quit
                if render_mode:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()

                action = self.next_action(state)
                state, reward, terminate, reached_road, info_dict = simulator._step(action)
                fpsClock.tick(FPS)

                cur_time += 1

                if terminate:
                    road_status = reached_road
                    break

            # Writing the output at each episode to STDOUT
            print(str(road_status) + ' ' + str(cur_time))

class Task2():

    def __init__(self):
        """
        Can modify to include variables as required
        """
        self.orientation = False
        self.x_init = 0
        self.y_init = 0
        self.marker = None
        self.mud_pit_centers = []
        super().__init__()

    def next_action(self, state):
        """
        Input: The current state
        Output: Action to be taken
        TO BE FILLED

        You can modify the function to take in extra arguments and return extra quantities apart from the ones specified if required
        """

        # Replace with your implementation to determine actions to be taken

        x = state[0]
        y = state[1]
        velocity = state[2]
        heading_angle = state[3]

        if velocity == 0:
            self.orientation = False
            self.x_init = x
            self.y_init = y
        else:
            self.orientation = True

        if ((x >= (self.mud_pit_centers[0][0] - 80) and x <= (self.mud_pit_centers[0][0] + 80) and y >= (self.mud_pit_centers[0][1] + 50))
            or (x >= (self.mud_pit_centers[1][0] - 80) and x <= (self.mud_pit_centers[1][0] + 80) and y <= (self.mud_pit_centers[1][1] - 50))
            or (x >= (self.mud_pit_centers[2][0] - 80) and x <= (self.mud_pit_centers[2][0] + 80) and y >= (self.mud_pit_centers[2][1] + 50))
            or (x >= (self.mud_pit_centers[3][0] - 80) and x <= (self.mud_pit_centers[3][0] + 80) and y <= (self.mud_pit_centers[3][1] - 50))):
            
            pass

        else:
            if self.timestep == 0 and velocity == 0:
                self.marker = 0
                self.timestep += 1
            
            if self.y_init == 0:
                target_angle = 0
            elif self.y_init < 0:
                target_angle = 90
            elif self.y_init > 0:
                target_angle = 270
            
            if abs(y) <= 20:
                target_angle = 0

                if velocity != 0 and self.run_only_once_again == 0 or self.run_only_once_again == 1:
                    self.run_only_once_again += 1
                    return np.array([1, 0])

            if self.run_only_once == 0 and target_angle == 0:
                self.marker = 1
                self.run_only_once += 1
            
            if abs(heading_angle - target_angle) <= abs(360 - abs(heading_angle - target_angle)):
                error = heading_angle - target_angle
            else:
                if heading_angle >= target_angle:
                    error = - (360 - heading_angle + target_angle)
                else:
                    error = 360 + heading_angle - target_angle
            
            if abs(error) > 4 and not self.orientation:
                if error < 0:
                    action_steer = 2
                    action_acc = 2
                else:
                    action_steer = 0
                    action_acc = 2
            else:
                self.orientation = True

            if self.orientation:
                action_steer = 1

                if abs(y) <= 20 and self.marker == 0:
                    action_acc = 0
                elif abs(y) <= 20 and self.marker == 1:
                    action_acc = 4
                else:
                    action_acc = 4

        action = np.array([action_steer, action_acc])  

        return action

    def controller_task2(self, config_filepath=None, render_mode=False):
        """
        This is the main controller function. You can modify it as required except for the parts specifically not to be modified.
        Additionally, you can define helper functions within the class if needed for your logic.
        """
        
        ################ Do NOT modify these lines ################
        pygame.init()
        fpsClock = pygame.time.Clock()

        if config_filepath is None:
            config_filepath = '../configs/config.json'

        time.sleep(3)
        ###########################################################

        # e is the number of the current episode, running it for 10 episodes
        for e in range(NUM_EPISODES):

            self.timestep = 0
            self.run_only_once = 0
            self.run_only_once_again = 0
            ################ Setting up the environment, do NOT modify these lines ################
            # To randomly initialize centers of the traps within a determined range
            ran_cen_1x = random.randint(120, 230)
            ran_cen_1y = random.randint(120, 230)
            ran_cen_1 = [ran_cen_1x, ran_cen_1y]

            ran_cen_2x = random.randint(120, 230)
            ran_cen_2y = random.randint(-230, -120)
            ran_cen_2 = [ran_cen_2x, ran_cen_2y]

            ran_cen_3x = random.randint(-230, -120)
            ran_cen_3y = random.randint(120, 230)
            ran_cen_3 = [ran_cen_3x, ran_cen_3y]

            ran_cen_4x = random.randint(-230, -120)
            ran_cen_4y = random.randint(-230, -120)
            ran_cen_4 = [ran_cen_4x, ran_cen_4y]

            ran_cen_list = [ran_cen_1, ran_cen_2, ran_cen_3, ran_cen_4]            
            eligible_list = []

            # To randomly initialize the car within a determined range
            for x in range(-300, 300):
                for y in range(-300, 300):

                    if x >= (ran_cen_1x - 110) and x <= (ran_cen_1x + 110) and y >= (ran_cen_1y - 110) and y <= (ran_cen_1y + 110):
                        continue

                    if x >= (ran_cen_2x - 110) and x <= (ran_cen_2x + 110) and y >= (ran_cen_2y - 110) and y <= (ran_cen_2y + 110):
                        continue

                    if x >= (ran_cen_3x - 110) and x <= (ran_cen_3x + 110) and y >= (ran_cen_3y - 110) and y <= (ran_cen_3y + 110):
                        continue

                    if x >= (ran_cen_4x - 110) and x <= (ran_cen_4x + 110) and y >= (ran_cen_4y - 110) and y <= (ran_cen_4y + 110):
                        continue

                    eligible_list.append((x,y))

            simulator = DrivingEnv('T2', eligible_list, render_mode=render_mode, config_filepath=config_filepath, ran_cen_list=ran_cen_list)
        
            # To keep track of the number of timesteps per episode
            cur_time = 0

            # To reset the simulator at the beginning of each episode
            state = simulator._reset(eligible_list=eligible_list)
            ###########################################################

            # The following code is a basic example of the usage of the simulator
            road_status = False

            self.mud_pit_centers = ran_cen_list

            for t in range(TIMESTEPS):
        
                # Checks for quit
                if render_mode:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()

                action = self.next_action(state)
                state, reward, terminate, reached_road, info_dict = simulator._step(action)
                fpsClock.tick(FPS)

                cur_time += 1

                if terminate:
                    road_status = reached_road
                    break

            print(str(road_status) + ' ' + str(cur_time))


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="config filepath", default=None)
    parser.add_argument("-t", "--task", help="task number", choices=['T1', 'T2'])
    parser.add_argument("-r", "--random_seed", help="random seed", type=int, default=0)
    parser.add_argument("-m", "--render_mode", action='store_true')
    parser.add_argument("-f", "--frames_per_sec", help="fps", type=int, default=30) # Keep this as the default while running your simulation to visualize results
    args = parser.parse_args()

    config_filepath = args.config
    task = args.task
    random_seed = args.random_seed
    render_mode = args.render_mode
    fps = args.frames_per_sec

    FPS = fps

    random.seed(random_seed)
    np.random.seed(random_seed)

    if task == 'T1':
        
        agent = Task1()
        agent.controller_task1(config_filepath=config_filepath, render_mode=render_mode)

    else:

        agent = Task2()
        agent.controller_task2(config_filepath=config_filepath, render_mode=render_mode)
