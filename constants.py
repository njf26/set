import pygame as pygame

display_width = 1300
display_height = 550

background_color = (34,139,34)
grey = (220,220,220)
black = (0,0,0)
green = (0, 200, 0)
red = (255,0,0)
light_slat = (119,136,153)
dark_slat = (47, 79, 79)
dark_red = (255, 0, 0)
pygame.init()
font = pygame.font.SysFont("Arial", 20)
textfont = pygame.font.SysFont('Comic Sans MS', 35)
game_end = pygame.font.SysFont('dejavusans', 100)
setfont = pygame.font.SysFont('roboto', 70)

NUMBERS = ['1', '2', '3']
SHAPES = ['diamond','oval','squiggle']
COLORS = ['green','red','purple']
FILL_PATTERNS = ['empty','filled','striped']

CARD_SIZE = (20, 40)
CARD_CENTER = (36, 48)
CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
