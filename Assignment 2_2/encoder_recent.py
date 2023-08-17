import numpy as np
import argparse
parser = argparse.ArgumentParser()


def print_to_file():
    print('numStates ' + str(numStates) + '\n')
    print('numActions ' + str(numActions) + '\n')
    print('end ' + str(end[0]) + ' ' + str(end[1]) + '\n')

    for i in range(1, numStates - 1):
        if i < int(numStates/2):
            if 6 * runs + 1 <= i <= 7 * runs or 12 * runs + 1 <= i <= 13 * runs:
                for j in range(numActions):
                    for k in range(7):
                        if P_A[j][k]:
                            if k == 0:
                                reward = 0
                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(0) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                            elif k == 2 or k == 4:
                                if i <= runs:
                                    if k - 1 < i:
                                        reward = 0
                                        print('transition ' + str(i) + ' ' + str(j) + ' ' + str(0) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                    else:
                                        if k == 2:
                                            reward = 1
                                            print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                        elif k == 4:
                                            if i == 3:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                            elif i == 2:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1]) + '\n')
                                            elif i == 1:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1] + P_A[j][k - 2]) + '\n')
                                else:
                                    if i % runs:
                                        if k - 1 < (i % runs):
                                            runs_left = (i % runs) - k + 1
                                            reward = 0
                                            print('transition ' + str(i) + ' ' + str(j) + ' ' + str(i - runs - (i % runs) + runs_left) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                        else:
                                            if k == 2:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                            elif k == 4:
                                                if i % runs == 3:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                                elif i % runs == 2:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1]) + '\n')
                                                elif i % runs == 1:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1] + P_A[j][k - 2]) + '\n')
                                    else:
                                        runs_left = runs - k + 1
                                        reward = 0
                                        print('transition ' + str(i) + ' ' + str(j) + ' ' + str(i - 2 * runs + runs_left) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                            else:
                                if i <= runs:
                                    if k != 6 and k - 1 < i:
                                        reward = 0
                                        print('transition ' + str(i) + ' ' + str(j) + ' ' + str(0) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                    elif k == 6 and k < i:
                                        reward = 0
                                        print('transition ' + str(i) + ' ' + str(j) + ' ' + str(0) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                    else:
                                        if k == 3:
                                            if i == 2:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                            elif i == 1:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1]) + '\n')
                                        elif k == 5:
                                            if i == 4:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                            elif i == 3:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1]) + '\n')
                                            elif i == 2:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1] + P_A[j][k - 2]) + '\n')
                                            elif i == 1:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1] + P_A[j][k - 2] + P_A[j][k - 3]) + '\n')
                                        elif k == 6:
                                            if i == 5 or i == 6:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                            elif i == 4:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1]) + '\n')
                                            elif i == 3:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1] + P_A[j][k - 2]) + '\n')
                                            elif i == 2:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1] + P_A[j][k - 2] + P_A[j][k - 3]) + '\n')
                                            elif i == 1:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1] + P_A[j][k - 2] + P_A[j][k - 3] + P_A[j][k - 4]) + '\n')
                                else:
                                    if i % runs:
                                        if k != 6 and k - 1 < (i % runs):
                                            runs_left = (i % runs) - k + 1
                                            reward = 0
                                            print('transition ' + str(i) + ' ' + str(j) + ' ' + str(i - runs - (i % runs) + runs_left + balls * runs) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                        elif k == 6 and k < (i % runs):
                                            runs_left = (i % runs) - k
                                            reward = 0
                                            print('transition ' + str(i) + ' ' + str(j) + ' ' + str(i - runs - (i % runs) + runs_left + balls * runs) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                        else:
                                            if k == 3:
                                                if i % runs == 2:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                                elif i % runs == 1:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1]) + '\n')
                                            elif k == 5:
                                                if i % runs == 4:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                                elif i % runs == 3:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1]) + '\n')
                                                elif i % runs == 2:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1] + P_A[j][k - 2]) + '\n')
                                                elif i % runs == 1:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1] + P_A[j][k - 2] + P_A[j][k - 3]) + '\n')
                                            elif k == 6:
                                                if i % runs == 5 or i % runs == 6:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                                elif i % runs == 4:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1]) + '\n')
                                                elif i % runs == 3:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1] + P_A[j][k - 2]) + '\n')
                                                elif i % runs == 2:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1] + P_A[j][k - 2] + P_A[j][k - 3]) + '\n')
                                                elif i % runs == 1:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1] + P_A[j][k - 2] + P_A[j][k - 3] + P_A[j][k - 4]) + '\n')
                                    else:
                                        if k != 6:
                                            runs_left = runs - k + 1
                                            reward = 0
                                            print('transition ' + str(i) + ' ' + str(j) + ' ' + str(i - 2 * runs + runs_left + balls * runs) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                        else:
                                            runs_left = runs - k
                                            reward = 0
                                            print('transition ' + str(i) + ' ' + str(j) + ' ' + str(i - 2 * runs - (i % runs) + runs_left + balls * runs) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
            else:
                for j in range(numActions):
                    for k in range(7):
                        if P_A[j][k]:
                            if k == 0:
                                reward = 0
                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(0) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                            elif k == 2 or k == 4:
                                if i <= runs:
                                    if k - 1 < i:
                                        reward = 0
                                        print('transition ' + str(i) + ' ' + str(j) + ' ' + str(0) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                    else:
                                        if k == 2:
                                            reward = 1
                                            print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                        elif k == 4:
                                            if i == 3:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                            elif i == 2:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1]) + '\n')
                                            elif i == 1:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1] + P_A[j][k - 2]) + '\n')
                                else:
                                    if i % runs:
                                        if k - 1 < (i % runs):
                                            runs_left = (i % runs) - k + 1
                                            reward = 0
                                            print('transition ' + str(i) + ' ' + str(j) + ' ' + str(i - runs - (i % runs) + runs_left + balls * runs) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                        else:
                                            if k == 2:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                            elif k == 4:
                                                if i % runs == 3:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                                elif i % runs == 2:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1]) + '\n')
                                                elif i % runs == 1:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1] + P_A[j][k - 2]) + '\n')
                                    else:
                                        runs_left = runs - k + 1
                                        reward = 0
                                        print('transition ' + str(i) + ' ' + str(j) + ' ' + str(i - 2 * runs + runs_left + balls * runs) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                            else:
                                if i <= runs:
                                    if k != 6 and k - 1 < i:
                                        reward = 0
                                        print('transition ' + str(i) + ' ' + str(j) + ' ' + str(0) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                    elif k == 6 and k < i:
                                        reward = 0
                                        print('transition ' + str(i) + ' ' + str(j) + ' ' + str(0) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                    else:
                                        if k == 3:
                                            if i == 2:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                            elif i == 1:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1]) + '\n')
                                        elif k == 5:
                                            if i == 4:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                            elif i == 3:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1]) + '\n')
                                            elif i == 2:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1] + P_A[j][k - 2]) + '\n')
                                            elif i == 1:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1] + P_A[j][k - 2] + P_A[j][k - 3]) + '\n')
                                        elif k == 6:
                                            if i == 5 or i == 6:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                            elif i == 4:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1]) + '\n')
                                            elif i == 3:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1] + P_A[j][k - 2]) + '\n')
                                            elif i == 2:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1] + P_A[j][k - 2] + P_A[j][k - 3]) + '\n')
                                            elif i == 1:
                                                reward = 1
                                                print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1] + P_A[j][k - 2] + P_A[j][k - 3] + P_A[j][k - 4]) + '\n')
                                else:
                                    if i % runs:
                                        if k != 6 and k - 1 < (i % runs):
                                            runs_left = (i % runs) - k + 1
                                            reward = 0
                                            print('transition ' + str(i) + ' ' + str(j) + ' ' + str(i - runs - (i % runs) + runs_left) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                        elif k == 6 and k < (i % runs):
                                            runs_left = (i % runs) - k
                                            reward = 0
                                            print('transition ' + str(i) + ' ' + str(j) + ' ' + str(i - runs - (i % runs) + runs_left) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                        else:
                                            if k == 3:
                                                if i % runs == 2:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                                elif i % runs == 1:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1]) + '\n')
                                            elif k == 5:
                                                if i == 34:
                                                    print('here1', i%runs, j, k)
                                                if i % runs == 4:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                                elif i % runs == 3:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1]) + '\n')
                                                elif i % runs == 2:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1] + P_A[j][k - 2]) + '\n')
                                                elif i % runs == 1:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1] + P_A[j][k - 2] + P_A[j][k - 3]) + '\n')
                                            elif k == 6:
                                                if i == 34:
                                                    print(j, k, P_A[j][k])
                                                    print('here2', i%runs, j, k)
                                                if i % runs == 5 or i % runs == 6:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                                elif i % runs == 4:
                                                    # print(i)
                                                    # print(i % runs)
                                                    # print(runs)
                                                    # print(P_A[j][k], P_A[j][k-1])
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1]) + '\n')
                                                elif i % runs == 3:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1] + P_A[j][k - 2]) + '\n')
                                                elif i % runs == 2:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1] + P_A[j][k - 2] + P_A[j][k - 3]) + '\n')
                                                elif i % runs == 1:
                                                    reward = 1
                                                    print('transition ' + str(i) + ' ' + str(j) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_A[j][k] + P_A[j][k - 1] + P_A[j][k - 2] + P_A[j][k - 3] + P_A[j][k - 4]) + '\n')
                                    else:
                                        if k != 6:
                                            runs_left = runs - k + 1
                                            reward = 0
                                            print('transition ' + str(i) + ' ' + str(j) + ' ' + str(i - 2 * runs + runs_left) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                        else:
                                            runs_left = runs - k
                                            reward = 0
                                            print('transition ' + str(i) + ' ' + str(j) + ' ' + str(i - 2 * runs - (i % runs) + runs_left) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
        else:
            if (balls + 6) * runs + 1 <= i <= (balls + 7) * runs or (balls + 12) * runs + 1 <= i <= (balls + 13) * runs:
                for k in range(3):
                    if k == 0:
                        reward = 0
                        print('transition ' + str(i) + ' ' + str(k) + ' ' + str(0) + ' ' + str(reward) + ' ' + str(P_B[k]) + '\n')
                    elif k == 1:
                        if i <= (balls + 1) * runs:
                            reward = 0
                            print('transition ' + str(i) + ' ' + str(k) + ' ' + str(0) + ' ' + str(reward) + ' ' + str(P_B[k]) + '\n')
                        else:
                            reward = 0
                            print('transition ' + str(i) + ' ' + str(k) + ' ' + str(i - runs - balls * runs) + ' ' + str(reward) + ' ' + str(P_B[k]) + '\n')
                    else:
                        if i <= (balls + 1) * runs:
                            if k - 1 < i:
                                reward = 0
                                print('transition ' + str(i) + ' ' + str(k) + ' ' + str(0) + ' ' + str(reward) + ' ' + str(P_B[k]) + '\n')
                            else:
                                reward = 1
                                print('transition ' + str(i) + ' ' + str(k) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_B[k]) + '\n')
                        else:
                            if i % runs:
                                if k - 1 < (i % runs):
                                    runs_left = (i % runs) - k + 1
                                    reward = 0
                                    print('transition ' + str(i) + ' ' + str(k) + ' ' + str(i - runs - (i % runs) + runs_left) + ' ' + str(reward) + ' ' + str(P_B[k]) + '\n')
                                else:
                                    reward = 1
                                    print('transition ' + str(i) + ' ' + str(k) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_B[k]) + '\n')
                            else:
                                runs_left = runs - k + 1
                                reward = 0
                                print('transition ' + str(i) + ' ' + str(k) + ' ' + str(i - 2 * runs + runs_left) + ' ' + str(reward) + ' ' + str(P_B[k]) + '\n')
            else:
                for k in range(3):
                    if k == 0:
                        reward = 0
                        print('transition ' + str(i) + ' ' + str(k) + ' ' + str(0) + ' ' + str(reward) + ' ' + str(P_B[k]) + '\n')
                    elif k == 1:
                        if i <= (balls + 1) * runs:
                            reward = 0
                            print('transition ' + str(i) + ' ' + str(k) + ' ' + str(0) + ' ' + str(reward) + ' ' + str(P_B[k]) + '\n')
                        else:
                            reward = 0
                            print('transition ' + str(i) + ' ' + str(k) + ' ' + str(i - runs) + ' ' + str(reward) + ' ' + str(P_B[k]) + '\n')
                    else:
                        if i <= (balls + 1) * runs:
                            if k - 1 < i:
                                reward = 0
                                print('transition ' + str(i) + ' ' + str(k) + ' ' + str(0) + ' ' + str(reward) + ' ' + str(P_B[k]) + '\n')
                            else:
                                reward = 1
                                print('transition ' + str(i) + ' ' + str(k) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_B[k]) + '\n')
                        else:
                            if i % runs:
                                if k - 1 < (i % runs):
                                    runs_left = (i % runs) - k + 1
                                    reward = 0
                                    print('transition ' + str(i) + ' ' + str(k) + ' ' + str(i - runs - (i % runs) + runs_left - balls * runs) + ' ' + str(reward) + ' ' + str(P_B[k]) + '\n')
                                else:
                                    reward = 1
                                    print('transition ' + str(i) + ' ' + str(k) + ' ' + str(numStates - 1) + ' ' + str(reward) + ' ' + str(P_B[k]) + '\n')
                            else:
                                runs_left = runs - k + 1
                                reward = 0
                                print('transition ' + str(i) + ' ' + str(k) + ' ' + str(i - 2 * runs + runs_left - balls * runs) + ' ' + str(reward) + ' ' + str(P_B[k]) + '\n')


    print('mdptype ' + mdptype + '\n')
    print('discount ' + str(gamma))


if __name__ == "__main__":
    parser.add_argument('--states', type=str, required=True)
    parser.add_argument('--parameters', type=str, required=True)
    parser.add_argument('--q', type=float, required=True)
    args = parser.parse_args()


    with open(args.states, 'r') as file:
        start_state = file.readline().strip()

    balls = 10 * int(start_state[0]) + int(start_state[1])
    runs = 10 * int(start_state[2]) + int(start_state[3])

    numStates = 2 * balls * runs + 2

    end = np.array([0, numStates - 1])

    mdptype = 'episodic'

    gamma = 1.0

    numActions = 5
    P_A = np.zeros(shape=(5, 7))

    with open(args.parameters, 'r') as file:
        lines = file.readlines()
        for line in lines:
            splitLine = line.split()
            if splitLine[0] == '0':
                P_A[0] = splitLine[1:8]
            if splitLine[0] == '1':
                P_A[1] = splitLine[1:8]
            if splitLine[0] == '2':
                P_A[2] = splitLine[1:8]
            if splitLine[0] == '4':
                P_A[3] = splitLine[1:8]
            if splitLine[0] == '6':
                P_A[4] = splitLine[1:8]

    q = args.q

    P_B = np.array([q, (1 - q)/2, (1 - q)/2])

    print_to_file()
