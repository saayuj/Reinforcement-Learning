import numpy as np
import argparse
parser = argparse.ArgumentParser()



if __name__ == "__main__":
    parser.add_argument('--value-policy', type=str, required=True)
    parser.add_argument('--states', type=str, required=True)
    args = parser.parse_args()

    with open(args.states, 'r') as file:
        start_state = file.readline().strip()

    balls = 10 * int(start_state[0]) + int(start_state[1])
    runs = 10 * int(start_state[2]) + int(start_state[3])

    numStates = balls * runs

    values = np.zeros(numStates)
    actions = np.zeros(numStates, dtype=int)
    bbrr = []

    with open(args.value_policy, 'r') as file:
        lines = file.readlines()[1 : numStates + 1]
        i = 0
        for line in lines:
            if not line.isspace():
                splitLine = line.split()
                values[i] = float(splitLine[0])

                if int(splitLine[1]) == 0 or int(splitLine[1]) == 1 or int(splitLine[1]) == 2:
                    actions[i] = int(splitLine[1])
                elif int(splitLine[1]) == 3:
                    actions[i] = int(splitLine[1]) + 1
                elif int(splitLine[1]) == 4:
                    actions[i] = int(splitLine[1]) + 2
                
                bbrr.append("{number:02}".format(number=int(np.floor(i / runs)) + 1) + "{number:02}".format(number=(i % runs) + 1))
                i += 1

    for i in range(numStates):
        print(bbrr[numStates - 1 - i] + ' ' + str(actions[numStates - 1 - i]) + ' ' + str(values[numStates - 1 - i]))
