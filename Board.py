import time
import pygame, sys, os
from Figures import *


class Board():
    
    width = height = 800
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    index_letters = {str(i): j for i, j in zip(letters, range(1, 9))}
    
    players = ['white', 'black'] 
    move = 0
    
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Chess")
    
    clock = pygame.time.Clock()
    fps = 15
    all_sprites = pygame.sprite.Group()
    
    #list with color and cordinates of each squere
    color_cor = [[(['w', 'b'][x%2], (int((x-y)*100+50), int(800-(y/7)*100 - 50))) for x in range(y, y+8)] for y in range(0, 50, 7)]
    #current_game = [[{'color': None, 'type': None} for _ in range(8)] for i in range(8)]
    current_game = [[None for _ in range(8)] for i in range(8)]

    figures = []
    
    choosed_figrue = None
    choosed_exist = False
    
    class _Squares(pygame.sprite.Sprite):
        
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'Sprites')
        
        squeres = {'w': 'white_squere.png', 'b': 'black_squere.png'}
        
        class _ChoosedPoint(pygame.sprite.Sprite):
            game_folder = os.path.dirname(__file__)
            img_folder = os.path.join(game_folder, 'Sprites')
            
            def __init__(self, cors: tuple):
                self._color = 'yellow'
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load(os.path.join(self.img_folder, 'yellow_squere.png'))
                self.rect = self.image.get_rect()
                self.rect.center = (cors[0] * 100 + 50, cors[1] * 100 + 50)
        
        def __init__(self, color, cors: tuple):
            x = (cors % 8) * 100 + 50
            y = (cors // 8) * 100 + 50
            pygame.sprite.Sprite.__init__(self)
            self._color = color
            self.image = pygame.image.load(os.path.join(self.img_folder, self.squeres[self._color]))
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            
        
    def __init__(self):
        
        x = 0
        for i in range(64):
            if i % 8 != 0:
                x ^= 1
            self.all_sprites.add(Board._Squares(['w', 'b'][x], i))
           
        for figure in self.figures:
            x, y = figure._position
            # place = self.current_game[self.index_letters[x] - 1][8-int(y)]
            self.current_game[self.index_letters[x] - 1][8-int(y)] = figure
            # place['color'] = figure._color
            # place['type'] = figure._type 
                
        # for y, color in zip([0, 7], ['black', 'white']):
        #     for x, type in zip(range(8), ['rook', 'horse', 'elef', 'queen', 'king', 'elef', 'horse', 'rook']):
        #         self.current_game[y][x]['color'] = color
        #         self.current_game[y][x]['type'] = type
        
                
        for y, color in zip([2, 7], ['white', 'black']):
            for x in self.letters:
                pos = (x, str(y))
                self.addFigure(Pin(pos, color))
        
        self.addFigure(King(('e', '1'), 'white'))
        self.addFigure(King(('e', '8'), 'black'))
        
        self.addFigure(Queen(('d', '1'), 'white'))
        self.addFigure(Queen(('d', '8'), 'black'))
        
        self.addFigure(Rook(('a', '1'), 'white'))
        self.addFigure(Rook(('h', '1'), 'white'))
        self.addFigure(Rook(('a', '8'), 'black'))
        self.addFigure(Rook(('h', '8'), 'black'))
        
        self.addFigure(Horse(('b', '1'), 'white'))
        self.addFigure(Horse(('g', '1'), 'white'))
        self.addFigure(Horse(('b', '8'), 'black'))
        self.addFigure(Horse(('g', '8'), 'black'))
        
        self.addFigure(Elef(('c', '1'), 'white'))
        self.addFigure(Elef(('f', '1'), 'white'))
        self.addFigure(Elef(('c', '8'), 'black'))
        self.addFigure(Elef(('f', '8'), 'black'))
        
        self.updatePosition()
        self.definePosibleMoves()
        
#############################################################################
                  
    def definePosibleMoves(self):
        for figure in self.figures:
            figure._posible_moves.clear()
            figure.PosibleMoves(self.current_game)
            
    def addFigure(self, fig):
        self.figures.append(fig)
        self.all_sprites.add(fig)
        
    def removeFigure(self, fig):
        self.all_sprites.remove(fig)
        self.figures.remove(fig)
        
    def updatePosition(self):
        self.current_game = [[None for _ in range(8)] for i in range(8)]
        for figure in self.figures:
            
            x, y = figure._position
            # place = self.current_game[self.index_letters[x] - 1][8-int(y)]
            self.current_game[self.index_letters[x] - 1][8-int(y)] = figure
            
    def removeYellow(self):
        for spr in self.all_sprites:
            if spr._color == 'yellow':
                self.all_sprites.remove(spr)
            
    def showPosibleMoves(self, *moves):
        if self.choosed_exist:
            self.removeYellow()
            for cor in moves:
                self.all_sprites.add(Board._Squares._ChoosedPoint(cor[1]))
            
#############################################################################
                    
    def main(self):

        while True:
            
            self.all_sprites.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(self.fps)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x = pos[0]//100
                y = pos[1]//100
                
                if not self.choosed_exist:
                    for figure in self.figures:
                        if figure._type == 'pin':
                            if figure.become_queen:
                                self.removeFigure(figure)
                                self.addFigure(Queen(figure._position, figure._color))
                        if figure._position == (self.letters[x], str(8 - y)) and figure._color == self.players[self.move % 2]:
                            self.choosed_figrue = figure
                            self.choosed_exist = True
                            self.showPosibleMoves(*self.choosed_figrue._posible_moves)
                                       
                elif self.choosed_figrue:
                    for figure in self.figures:
                        if figure._position == (self.letters[x], str(8 - y)) and figure._color == self.choosed_figrue._color:
                            self.choosed_figrue = figure
                            self.showPosibleMoves(*self.choosed_figrue._posible_moves)
                        
                    for cors in self.choosed_figrue._posible_moves:
                        if cors[1] == (x, y):
                            if cors[0] == 'eat':
                                for spr in self.figures:
                                    if spr._position == (self.letters[x], str(8 - int(y))):
                                        self.removeFigure(spr)
                            self.choosed_figrue.move(x, y)
                            self.move += 1
                            self.updatePosition()
                            self.definePosibleMoves()
                            self.choosed_exist = False
                            self.removeYellow()
                            continue
                            
chess = Board()
chess.main()
