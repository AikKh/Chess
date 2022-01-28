import pygame, os

class Figure(pygame.sprite.Sprite):
    
    #figures = ['black_pin.png', 'white_pin.png']
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    first_pin_move = True
    
    x = {str(i): j for i, j in zip(letters, range(8))}
    y = {str(i): 8 - i for i in range(1, 9)}
    
    values = {'pin': 1, 'horse': 3, 'elef': 3, 'rook': 5, 'queen': 9, 'king': 'k'}
    
    
    game_folder = os.path.dirname(__file__)
    img_folder = os.path.join(game_folder, 'Sprites')
    
    
    elef_moves = [[(x, y) for x, y in zip(range(i, 8*i, i), range(j, 8*j, j))] for i, j in [(1, 1), (1, -1), (-1, 1), (-1, -1)]]
    rook_moves = [[(x*i, y*i) for i in range(1, 8)] for x, y in [(1, 0), (0, -1), (-1, 0), (0, 1)]]
    
    
    def __init__(self, img: str, pos: tuple[str, str], type: str, color: str):
        self._value = self.values[type]
        self._type = type
        self._color = color
        self._position = pos
        self._posible_moves = []
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(self.img_folder, img))
        self.rect = self.image.get_rect()
        self.rect.center = self.getCenterByPos(self._position)

        
    def getCenterByPos(self, position: tuple):
        x = self.x[position[0]] * 100 + 50
        y = self.y[position[1]] * 100 + 50
        return (x, y)
    
    def getMatrixPosByPos(self, position: tuple):
        x = self.x[position[0]]
        y = self.y[self._position[1]]
        return (x, y)

#######################################################################
            
    def detectOccupiedPlace(self, current_game: list[list], move: tuple, can_take = True):
        our_x, our_y = self.x[self._position[0]], self.y[self._position[1]]
        place_x, place_y = our_x + move[0], our_y + move[1]
        
        if place_x < 0 or place_y < 0 or place_x >= 8 or place_y >= 8:
            return False
        place = current_game[place_x][place_y]
            
        if place:
            if place._color == self._color:
                return False
            elif place._color != self._color:
                return ('eat', (place_x, place_y))
        else:
            return ('free', (place_x, place_y))
            
#######################################################################
    
    def move(self, *cors):
        self._position = (self.letters[cors[0]], str(8 - int(cors[1])))
        self.rect.x = cors[0]*100
        self.rect.y = cors[1]*100
            