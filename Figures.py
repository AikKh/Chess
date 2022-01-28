from Base_figure import Figure
import os

class Pin(Figure):
    
    game_folder = os.path.dirname(__file__)
    img_folder = os.path.join(game_folder, 'Sprites')
    
    imgs = ['BlackPin.png', 'WhitePin.png']
    moves = {'white': [[(0, -1), (0, -2)], [(-1, -1), (1, -1)]], 'black': [[(0, 1), (0, 2)], [(1, 1), (-1, 1)]]}
    
    become_queen = False
    
    def __init__(self, pos: tuple[str, str], color: str):
        self._image = None
        self._type = 'pin'
        
        
        if color == 'black':
            self._image = self.imgs[0]
        elif color == 'white':
            self._image = self.imgs[1]
            
        super().__init__(self._image, pos, self._type, color)
        
    def boolQueen(self):
        return self._color == 'black' and self._position[1] == '1' or self._color == 'white' and self._position[1] == '8'
        
    def PosibleMoves(self, current_game):
        if self.boolQueen():
            print('become_queen')
            self.become_queen = True
        for moves_cors, can_take in zip(self.moves[self._color], [False, True]):
            for cors in moves_cors:
                if self._color == 'white' and not can_take and moves_cors.index(cors) == 1:
                    if self._position[1] != '2':
                        break
                elif self._color == 'black' and not can_take and moves_cors.index(cors) == 1:
                    if self._position[1] != '7':
                        break
                move = self.detectOccupiedPlace(current_game, cors, can_take)
                if move:
                    if can_take and move[0] == 'eat' or not can_take and move[0] == 'free':
                        self._posible_moves.append(move)

class Horse(Figure):
    
    game_folder = os.path.dirname(__file__)
    img_folder = os.path.join(game_folder, 'Sprites')
    
    imgs = ['BlackHorse.png', 'WhiteHorse.png']
    moves = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]
    
    def __init__(self, pos: tuple[str, str], color: str):
        self._image = None
        self._type = 'horse'
        
        
        if color == 'black':
            self._image = self.imgs[0]
        elif color == 'white':
            self._image = self.imgs[1]
            
        super().__init__(self._image, pos, self._type, color)
        
    def PosibleMoves(self, current_game):
        
        for move_cors in self.moves:
            move = self.detectOccupiedPlace(current_game, move_cors)
            if move:
                self._posible_moves.append(move)
    
class Elef(Figure):  
       
    game_folder = os.path.dirname(__file__)
    img_folder = os.path.join(game_folder, 'Sprites')
    
    imgs = ['BlackElef.png', 'WhiteElef.png']  
    moves = [[(x, y) for x, y in zip(range(i, 8*i, i), range(j, 8*j, j))] for i, j in [(1, 1), (1, -1), (-1, 1), (-1, -1)]]
    
    def __init__(self, pos: tuple[str, str], color: str):
        self._image = None
        self._type = 'elef'
        
        if color == 'black':
            self._image = self.imgs[0]
        elif color == 'white':
            self._image = self.imgs[1]
            
        super().__init__(self._image, pos, self._type, color)
        
    
    def PosibleMoves(self, current_game):
        
        for dir in self.moves:
            for move_cors in dir:
                move = self.detectOccupiedPlace(current_game, move_cors)
                if move:
                    if move[0] == 'eat':
                        self._posible_moves.append(move)
                        break
                    self._posible_moves.append(move)
                else:
                    break
                
class Rook(Figure):
    
    game_folder = os.path.dirname(__file__)
    img_folder = os.path.join(game_folder, 'Sprites')
    
    imgs = ['BlackRook.png', 'WhiteRook.png']  
    moves = [[(x*i, y*i) for i in range(1, 8)] for x, y in [(1, 0), (0, -1), (-1, 0), (0, 1)]]
    
    def __init__(self, pos: tuple[str, str], color: str):
        self._image = None
        self._type = 'rook'
        
        if color == 'black':
            self._image = self.imgs[0]
        elif color == 'white':
            self._image = self.imgs[1]
            
        super().__init__(self._image, pos, self._type, color)
        
    
    def PosibleMoves(self, current_game):
        
        for dir in self.moves:
            for move_cors in dir:
                move = self.detectOccupiedPlace(current_game, move_cors)
                if move:
                    if move[0] == 'eat':
                        self._posible_moves.append(move)
                        break
                    self._posible_moves.append(move)
                else:
                    break
                
class Queen(Figure):
    
    game_folder = os.path.dirname(__file__)
    img_folder = os.path.join(game_folder, 'Sprites')
    
    imgs = ['BlackQueen.png', 'WhiteQueen.png']  
    moves = Rook.moves + Elef.moves
    
    def __init__(self, pos: tuple[str, str], color: str):
        self._image = None
        self._type = 'queen'
        
        if color == 'black':
            self._image = self.imgs[0]
        elif color == 'white':
            self._image = self.imgs[1]
            
        super().__init__(self._image, pos, self._type, color)
        
    
    def PosibleMoves(self, current_game):
        
        for dir in self.moves:
            for move_cors in dir:
                move = self.detectOccupiedPlace(current_game, move_cors)
                if move:
                    if move[0] == 'eat':
                        self._posible_moves.append(move)
                        break
                    self._posible_moves.append(move)
                else:
                    break
                
class King(Figure):
    
    game_folder = os.path.dirname(__file__)
    img_folder = os.path.join(game_folder, 'Sprites')
    
    imgs = ['BlackKing.png', 'WhiteKing.png']  
    moves = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (0, -1), (-1, 0), (0, 1)]
    
    def __init__(self, pos: tuple[str, str], color: str):
        self._image = None
        self._type = 'queen'
        
        if color == 'black':
            self._image = self.imgs[0]
        elif color == 'white':
            self._image = self.imgs[1]
            
        super().__init__(self._image, pos, self._type, color)
        
    
    def PosibleMoves(self, current_game):
        
        for move_cors in self.moves:
            move = self.detectOccupiedPlace(current_game, move_cors)
            if move:
                self._posible_moves.append(move)