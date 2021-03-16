## Lab 5 exercises, questions, and challenge

This weeks lab is about

### QUESTIONS

1. What is branching factor depth 0? At depth 1?
2. What is the maximal depth?
3. Will a MIN move attempt to minimize or maximize the utility?
4. Are states after a terminal state explored?
5. Are alle possible states explored to a terminal state?
6. Is this a depth-first or breadth-first search? How do you know? (See Python code)

### ANWSERS

not begun yet...

### EXERCISE 1

1. Run the MinMax TicTacToe program by implementing these functions in tictactoe_template.py: 1. is_terminal(state) 2. Utility_of(state)
   Succesors_of(state)
   Note: You will play as "O", and the computer plays "X".

### HOMEWORK 1

1. Write a nim game using minmax_decision from tic-tac-toe program. The state space of nim maybe exhaustively searched.

2. To play nim, a number of tokens are placed in a pile between two Opponents; at each move, the player must divide a pile into two nonempty piles of different sizes. Thus a pile of six tokens [6] may be divided into two piles of [5,1] or [4,2] but not [3,3].

   The first player who can no longer move loses.

   [The picture in the following slide ](NimSearchTree.png)illustrates a state space for a game with 7 tokens.

   MIN should start the game and, with 7 tokens is certain to lose if MAX divides the piles following the heavy arrows. Test using 15 in the startingpile.

3. Rewrite nim using Alpha_beta_decision and compare with minimax over a pile of 20
4. Modify nim to play the MIN position, i.e., utility_of should return +1 for MIN and -1 for MAX

note: MAX is stateless, no memory of previous piles is held. Any pile, e.g., [1,2,3,4], can be sent to MAX which will return its move.

### CHALLENGE

Solve breakthrough using alpha beta serach

- The game is played on a chessboard, every piece is a pawn.
- A piece may move one space straight or diagonally forward if the target square is empty.
- A piece may move into a square containing an opponents piece if and only if that square is one step diagonally foward. The opponent's piece is removed and the player's piece replaces it. Note that capturing is not compulsory, nor is it "chained" as in checkers.
- The first player to reach the opponent's home row - the one farthest from the player - is the winner. If all the pieces of a player are captured, that player loses.

Adapted from [link](<https://en.wikipedia.org/wiki/Breakthrough_(board_game)>)
