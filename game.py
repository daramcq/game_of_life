#! /usr/bin/python

class Game(object):
    
    def __init__(self, dimensions, cell_set):
        self.dimensions = dimensions
        self.cell_set = cell_set 
    
    def is_adjacent(self, a, b):
        return abs(a[0] - b[0]) < 2 and abs(a[1] - b[1]) < 2

    def getLiveNeighbours(self, pos):
        alive = self.cell_set.difference(set([pos]))
        live_neighbours = [t for t in alive 
                           if self.is_adjacent(t, pos)]
        return len(live_neighbours)

    def survives(self, live_neighbours):
        return live_neighbours > 1 and live_neighbours < 4

    def is_born(self, live_neighbours):
        return live_neighbours == 3

    def positionLives(self, pos):        
        neighbours = self.getLiveNeighbours(pos)
        is_alive = pos in self.cell_set

        return (self.survives(neighbours) if is_alive
                else self.is_born(neighbours)) 

    def stepGame(self):
        new_cell_set = set([pos for pos 
                            in getGrid(*self.dimensions) 
                            if self.positionLives(pos)])
        return Game(self.dimensions, new_cell_set)

def getGrid(w,h):
    for x in range(w):
        for y in range(h):
            yield (x,y)

def getChar(pos, game):
    is_alive = pos in game.cell_set
    char = " X" if is_alive else " _"
    is_end_cell = pos[1] is game.dimensions[1] - 1
    char += "\n" if is_end_cell else ""
    return char

def drawGame(game):
    chars = [getChar(pos, game) for pos in getGrid(*game.dimensions)]
    print "".join(chars)
    
if __name__ == '__main__':

    steps = 5
    dimensions = (5,5)
    cell_set = set([(1,2),(3,3),(2,1),(2,2),(4,5)])
    game = Game(dimensions, cell_set)
        
    for i in range(steps):
        game = game.stepGame()
        drawGame(game)
        print ""
