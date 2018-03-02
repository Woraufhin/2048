from random import randint
from BaseAI import BaseAI
from heuristics import utilityf


class RandomAI(BaseAI):
    """IA idiota que mueve aleatoriamente"""

    def getMove(self, grid):
        moves = grid.getAvailableMoves()
        return moves[randint(0, len(moves) - 1)] if moves else None


# < >

class PlayerAI(BaseAI):
    """Implementar minimax con alpha-beta pruning"""

    MAX_DEPTH_RECURSION = 3

    def __init__(self):
        self.best_move = None

    def minimize(self, state, depth):
        """
        Min ply

        :param state
        :return (state, utility)
        """

        min_child, min_utility = (None, float('inf'))

        for move in state.getAvailableMoves():
            new_grid = state.clone()
            insert_random_tile(new_grid)

            if depth >= self.MAX_DEPTH_RECURSION:
                utility = utilityf(new_grid)
            else:
                _, utility = self.maximize(new_grid, depth + 1)

            if utility < min_utility:
                min_child, min_utility = new_grid, utility
        return min_child, min_utility

    def maximize(self, state, depth=0):
        """
        Max ply

        :param state
        :return (state, utility)
        """

        max_child, max_utility = (None, float('-inf'))

        for move in state.getAvailableMoves():
            new_grid = state.clone()
            new_grid.move(move)

            _, utility = self.minimize(new_grid, depth + 1)

            if utility > max_utility:
                max_child, max_utility = new_grid, utility

                if depth == 0:
                    self.best_move = move

        return max_child, max_utility


    def getMove(self, grid):
        child, ut = self.maximize(grid)
        return self.best_move


# Yep, I need to COPY this functions because I can't import them...
# I even fixed a typo, you had ONE JOB AI COURSE
def get_new_tile_values():
    possibleNewTiles = [2, 4]
    if randint(0,99) < 100 * 0.9:
        return possibleNewTiles[0]
    else:
        return possibleNewTiles[1];


def insert_random_tile(grid):
    tileValue = get_new_tile_values()
    cells = grid.getAvailableCells()
    cell = cells[randint(0, len(cells) - 1)]
    grid.setCellValue(cell, tileValue)
