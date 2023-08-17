import numpy as np
import argparse
parser = argparse.ArgumentParser()


def print_to_file():

    with open('mdpfile.txt', 'w') as file:
        file.write('numStates ' + str(numStates) + '\n')
        file.write('numActions ' + str(numActions) + '\n')
        file.write('end ' + str(end[0]) + ' ' + str(end[1]) + '\n')

        for i in range(1, numStates - 1):
            if i < 151:
                for j in range(numActions):
                    for k in range(7):
                        if P_A[j][k]:
                            if k == 0:
                                reward = 0
                                file.write('transition ' + str(i) + ' ' + str(j) + ' ' + str(0) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                            elif k == 2 or k == 4:
                                if i <= 10:
                                    if k != 6 and k - 1 < i:
                                        reward = 0
                                        file.write('transition ' + str(i) + ' ' + str(j) + ' ' + str(0) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                    elif k == 6 and k < i:
                                        reward = 0
                                        file.write('transition ' + str(i) + ' ' + str(j) + ' ' + str(0) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                    else:
                                        reward = 1
                                        file.write('transition ' + str(i) + ' ' + str(j) + ' ' + str(301) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                else:
                                    if i % 10:
                                        if k != 6 and k - 1 < (i % 10):
                                            runs_left = (i % 10) - k + 1
                                            reward = 0
                                            file.write('transition ' + str(i) + ' ' + str(j) + ' ' + str(i - 10 - (i % 10) + runs_left + 150) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                        elif k == 6 and k < (i % 10):
                                            runs_left = (i % 10) - k
                                            reward = 0
                                            file.write('transition ' + str(i) + ' ' + str(j) + ' ' + str(i - 10 - (i % 10) + runs_left + 150) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                        else:
                                            reward = 1
                                            file.write('transition ' + str(i) + ' ' + str(j) + ' ' + str(301) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                    else:
                                        if k != 6:
                                            runs_left = 10 - k + 1
                                            reward = 0
                                            file.write('transition ' + str(i) + ' ' + str(j) + ' ' + str(i - 20 + runs_left + 150) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                        else:
                                            runs_left = 10 - k
                                            reward = 0
                                            file.write('transition ' + str(i) + ' ' + str(j) + ' ' + str(i - 20 - (i % 10) + runs_left + 150) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                            else:
                                if i <= 10:
                                    if k != 6 and k - 1 < i:
                                        reward = 0
                                        file.write('transition ' + str(i) + ' ' + str(j) + ' ' + str(0) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                    elif k == 6 and k < i:
                                        reward = 0
                                        file.write('transition ' + str(i) + ' ' + str(j) + ' ' + str(0) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                    else:
                                        reward = 1
                                        file.write('transition ' + str(i) + ' ' + str(j) + ' ' + str(301) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                else:
                                    if i % 10:
                                        if k != 6 and k - 1 < (i % 10):
                                            runs_left = (i % 10) - k + 1
                                            reward = 0
                                            file.write('transition ' + str(i) + ' ' + str(j) + ' ' + str(i - 10 - (i % 10) + runs_left) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                        elif k == 6 and k < (i % 10):
                                            runs_left = (i % 10) - k
                                            reward = 0
                                            file.write('transition ' + str(i) + ' ' + str(j) + ' ' + str(i - 10 - (i % 10) + runs_left) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                        else:
                                            reward = 1
                                            file.write('transition ' + str(i) + ' ' + str(j) + ' ' + str(301) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                    else:
                                        if k != 6:
                                            runs_left = 10 - k + 1
                                            reward = 0
                                            file.write('transition ' + str(i) + ' ' + str(j) + ' ' + str(i - 20 + runs_left) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
                                        else:
                                            runs_left = 10 - k
                                            reward = 0
                                            file.write('transition ' + str(i) + ' ' + str(j) + ' ' + str(i - 20 - (i % 10) + runs_left) + ' ' + str(reward) + ' ' + str(P_A[j][k]) + '\n')
            else:
                for k in range(3):
                    if k == 0:
                        reward = 0
                        file.write('transition ' + str(i) + ' ' + str(k) + ' ' + str(0) + ' ' + str(reward) + ' ' + str(P_B[k]) + '\n')
                    elif k == 1:
                        if i <= 160:
                            reward = 0
                            file.write('transition ' + str(i) + ' ' + str(k) + ' ' + str(0) + ' ' + str(reward) + ' ' + str(P_B[k]) + '\n')
                        else:
                            reward = 0
                            file.write('transition ' + str(i) + ' ' + str(k) + ' ' + str(i - 10) + ' ' + str(reward) + ' ' + str(P_B[k]) + '\n')
                    else:
                        if i <= 160:
                            if k - 1 < i:
                                reward = 0
                                file.write('transition ' + str(i) + ' ' + str(k) + ' ' + str(0) + ' ' + str(reward) + ' ' + str(P_B[k]) + '\n')
                            else:
                                reward = 1
                                file.write('transition ' + str(i) + ' ' + str(k) + ' ' + str(301) + ' ' + str(reward) + ' ' + str(P_B[k]) + '\n')
                        else:
                            if i % 10:
                                if k - 1 < (i % 10):
                                    runs_left = (i % 10) - k + 1
                                    reward = 0
                                    file.write('transition ' + str(i) + ' ' + str(k) + ' ' + str(i - 10 - (i % 10) + runs_left - 150) + ' ' + str(reward) + ' ' + str(P_B[k]) + '\n')
                                else:
                                    reward = 1
                                    file.write('transition ' + str(i) + ' ' + str(k) + ' ' + str(301) + ' ' + str(reward) + ' ' + str(P_B[k]) + '\n')
                            else:
                                runs_left = 10 - k + 1
                                reward = 0
                                file.write('transition ' + str(i) + ' ' + str(k) + ' ' + str(i - 20 + runs_left - 150) + ' ' + str(reward) + ' ' + str(P_B[k]) + '\n')


        file.write('mdptype ' + mdptype + '\n')
        file.write('discount ' + str(gamma))



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
