class Scrabble:
    def __init__(self):
        noLetterYet = ' '
        self.points = 0
        self.direction = ['x+', 'x-', 'y+', 'y-']
        self.boardSize = 10
        self.board = [[noLetterYet for i in range(self.boardSize)] for j in range(self.boardSize)]
        # Where (0,0) is the top left and (self.boardSize-1, self.boardSize-1) is the bottom right
        # Indexed by zero
        self.tileSet = {
                'O' : 0,
                'L' : 1,
                'Z' : 2,
                'E' : 3,
                'A' : 4,
                'S' : 5,
                'G' : 6,
                'T' : 7,
                'B' : 8,
                'P' : 9
            }

    def placeTile(self, x, y, direction, tiles):
        assert set(tiles).issubset(set(self.tileSet.keys())), "Not a list of proper tiles"
        assert direction in self.direction, "Not a valid direction"
        assert x - len(tiles) >= 0 or len(tiles) + x < self.boardSize, "Cannot place off the board in the x direction"
        assert y - len(tiles) >= 0 or len(tiles) + y < self.boardSize, "Cannot place off the board in the y direction"
        assert 0 <= x < self.boardSize, "Not a valid x position on the board"
        assert 0 <= y < self.boardSize, "Not a valid y position on the board"
        assert self.board[y][x] == ' ', "Can't place a tile here!"

        if 'x' in list(direction):
            if '+' in list(direction):
                for letter in range(len(tiles)):
                    self.board[y][x+letter] = tiles[letter]
            else:
                for letter in range(len(tiles)):
                    self.board[y][x-letter] = tiles[-1-letter]
        else:
            if '+' in list(direction):
                for letter in range(len(tiles)):
                    self.board[y+letter][x] = tiles[letter]
                    self.points += self.tileSet[tiles[letter]]
            else:
                for letter in range(len(tiles)):
                    self.board[y-letter][x] = tiles[-1-letter]

        self.tallyPoints(tiles)

    def tallyPoints(self, tiles):
        for i in range(len(tiles)):
            self.points += self.tileSet[tiles[i]]

    def hasWordBeenMade(self):
        wordListR = []
        wordListC = []
        # Doesn't actually check if a word has been made yet, just joins the rows and coloumns to see what
        # strings are built from current state of the board
        for i in range(self.boardSize):
            wordListR.append(''.join(self.board[i]))
            wordListC.append(''.join(row[i] for row in self.board))
        print('Words by row:', wordListR)
        print('Words by coloum:', wordListC)
        wordList = wordListR + wordListC
        print('Combined words found: ')
        for word in range(len(wordList)):
            if (word == len(wordList)/2):
                print()
            print('[' + wordList[word] + ']')

def main():
    board = Scrabble()
    b = board.board

    print()

    word1 = ['L','E','E','T']
    board.placeTile(9,3,'x-',word1)
    # board.placeTile(1,2,'L')

    print()
    for rows in b:
        print(rows)

    print()
    print(board.points)
main()
