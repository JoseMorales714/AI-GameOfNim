## Two players take turns removing objects from distinct heaps or rows
## In each turn, a player must remove at least one object from the same row
## The winner is the player that takes the last object(s).
# Represent the state by a list which represents the number of objects in each pile/row.
# E.g., [5, 3, 1] represents 5 objects in the first row, 3 in the second, and 1 in the third row.
# An action in this game is removing a certain number of objects from one pile.
# Represent an action by a 2-tuple (r, n) where r represents the row number (start counting from 0 for convenience as Python uses 0-based indexing)
# and n represents the number of objects to remove. E.g., (1,2) means remove 2 objects from row with index 1 (the second row).
# Submission will be via Gradescope. Upload a single file with your class. The name of the file must be game_of_nim.py.
# The name of the class should be GameOfNim. Gradescope will run a few unit tests automatically and show you the results.
# You can submit multiple times.

# Members-> Jose Morales and Hongfei Wang
# Date-> 04/14/2023


from games import *

class GameOfNim(Game):

    # E.g., [5, 3, 1] represents 5 objects in the first row, 3 in the second, and 1 in the third row.


    def __init__(self, board):
        moves1 = [(x, y) for x in range(0, 1)
                  for y in range(1, board[0] + 1)]

        moves2 = [(x, y) for x in range(1,2)
                 for y in range(1, board[1] + 1)]

        moves3 = [(x, y) for x in range(2,3)
                 for y in range(1, board[2] + 1)]

        moves4 = [(x, y) for x in range(3,4)
                 for y in range(1, board[3] + 1)]

        moves = moves1 + moves2 + moves3 + moves4

        self.initial = GameState(to_move='', utility=0, board=[7,5,3,1], moves=moves)

    def result(self, state, move): pass


    def actions(self, state):
        """Legal moves are any square not yet taken."""
        return state.moves




    def terminal_test(self, state):
        """A state is terminal if it is won or there are no empty squares."""
        return state.utility != 0 or len(state.moves) == 0

    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        return state.utility if player == 'X' else -state.utility

    def to_move(self, state):
        """Return the player whose move it is in this state."""
        return state.to_move


if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1]) # Creating the game instance
    #nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search

    print(nim.initial.board) # must be [0, 5, 3, 1]
    print(nim.initial.moves) # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2,1), (2, 2), (2, 3), (3, 1)]
    print(nim.result(nim.initial, (1,3) ))

    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
