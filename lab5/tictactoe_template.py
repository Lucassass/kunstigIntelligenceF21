import numpy as np
def minmax_decision(state):

    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for (a, s) in successors_of(state):
            v = max(v, min_value(s))
        print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for (a, s) in successors_of(state):
            v = min(v, max_value(s))
        return v

    infinity = float('inf')
    action, state = argmax(successors_of(state), lambda a: min_value(a[1]))
    return action


def is_terminal(state):
    """
    returns True if the state is either a win or a tie (board full)
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    pass


def utility_of(state):
    # top right to bot left 
    print([state[i][len(state)-i-1] for i in range(len(state))])

    # top left to bot right
    print([state[i][i] for i in range(len(state))])

    for i in j 
        np.concatenate(
            np.sum(state[i])
        )
    # first row
    print(state[0])
    np.sum(state[0])

    # second row 
    print(state[1])

    #third row
    print(state[2])

    #collum 1
    print(state[:,0])

    # collum 2
    print(state[:,1])

    # collum 3
    print(state[:,2])

    winner = state.sum
    print(np.sum(state[0:2]))
    if (winner > 1):
        return print('Max Player won')
    elif(winner <1):
        return print('Min Player won')
    elif(winner == 0):
        return print('Draw, Play again!')
    """
    returns +1 if winner is X (MAX player), -1 if winner is O (MIN player), or 0 otherwise
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """


def successors_of(state):
    """
    returns a list of tuples (move, state) as shown in the exercise slides
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    pass


def display(state):
    print("-----")
    for c in [0, 3, 6]:
        print(state[c + 0], state[c + 1], state[c + 2])


def main():
    board = np.array([[0, 1, 2], 
                      [3, 4, 5], 
                      [6, 7, 8]])

    while not is_terminal(board):
        board[minmax_decision(board)] = 'X'
        if not is_terminal(board):
            display(board)
            board[int(input('Your move? '))] = 'O'
    display(board)


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
