class Snake:
    pass

class Apple:
    pass

class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def board_matrix(self):
        return [[ None for x in range(self.width)] for y in range(self.height)]

    def render(self):
        print('Height: ' + str(self.height))
        print('Width: ' + str(self.width))

        matrix = self.board_matrix()

        divider = ''
        out = ''

        for x in range(self.width + 2):
            if x == 0:
                divider += '+'
            elif x == self.width + 1:
                divider += '+'
            else:
                divider += '-'

        out += divider
        out += '\n'

        for y in range(self.height):
            out += '|' 
            for x in range(self.width):
                if matrix[y][x] == None:
                    out += ' '
                else:
                    out += str(matrix[y][x])
            out += '|\n'
        
        out += divider

        print(out)
        

game = Game(10, 20)
game.render()