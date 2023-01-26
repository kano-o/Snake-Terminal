UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1 , 0)

class Snake:
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction

    def take_step(self, input, height, width):
        
        if input == '':
            input = self.direction

        if input == 'w':
            position = ((self.head()[0] + UP[0]) % height, (self.head()[1] + UP[1]) % height)
        elif input == 'a':
            position = ((self.head()[0] + LEFT[0]) % width, (self.head()[1] + LEFT[1]) % width)
        elif input == 's':
            position = ((self.head()[0] + DOWN[0]) % height, (self.head()[1] + DOWN[1]) % height)
        elif input == 'd':
            position = ((self.head()[0] + RIGHT[0]) % width, (self.head()[1] + RIGHT[1]) % width)

        print(self.is_self_intersecting())

        if not self.is_self_intersecting():
            self.direction = input
            self.body = self.body[1:] + [position]
        
    def is_self_intersecting(self):
        return len(self.body) != len(set(self.body))
    
    def set_direction(self, direction):
        self.direction = direction

    def contains(self, x, y):
        return (x, y) in self.body
    
    def head(self):
        return self.body[-1]

class Apple:
    pass

class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.snake = Snake([(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)], UP)
    
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
                if (x, y) == self.snake.head():
                    out += 'X'
                elif self.snake.contains(x, y):
                    out += 'O'
                elif matrix[y][x] == None:
                    out += ' '
                else:
                    out += str(matrix[y][x])
            out += '|\n'
        
        out += divider

        print(out)

height = 20
width = 40

game = Game(height, width)
game.render()

turn = 0
    
while(True):
        
    move = input()
        
    game.snake.take_step(move, height, width)

    game.render()

    #turn += 1
    if turn == 10:
        break