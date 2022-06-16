import pygame as pygame
from set_deck import *
from constants import *
from set_game import *
import sys
pygame.init()

###text object render
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def end_text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


#game text display
def game_texts(text, x, y):
    TextSurf, TextRect = text_objects(text, textfont)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

 
def game_finish(text, x, y, color):
    TextSurf, TextRect = end_text_objects(text, game_end, color)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def set(text, x, y, color):
    TextSurf, TextRect = end_text_objects(text, setfont, color)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    
#button display
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    TextSurf, TextRect = text_objects(msg, font)
    TextRect.center = ((x + (w/2)), (y + (h/2)))
    gameDisplay.blit(TextSurf, TextRect)

#point counter display
def point_counter(msg, x, y, w, h, ic):
    pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    TextSurf, TextRect = text_objects(msg, font)
    TextRect.center = ((x + (w/2)), (y + (h/2)))
    gameDisplay.blit(TextSurf, TextRect)

#card button display
def card_button(img, x, y, w, h, ic, ac, action, card):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 != None:
            action(card)
            pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    gameDisplay.blit(pygame.image.load('img/' + img).convert(), (x,y))

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Set')
gameDisplay.fill(background_color)
pygame.draw.rect(gameDisplay, grey, pygame.Rect(0, 0, 250, 700))
        
play_set = Play()

running = True

while running:
    # reward, state, done = play_set.step(int(input()))
    # print(reward, done)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        x = 270
        y = 30
        w = 250
        h = 150
        for i in range(len(play_set.board.card_img)):
          if i % 4 == 0 and i != 0:
            y = y + h
            x = 270
          elif i != 0:
            x = x + w
          card_button(play_set.board.card_img[i], x, y, w, h, light_slat, dark_slat, play_set.select_card, play_set.board.cards[i])

        button("No set", 30, 100, 150, 50, light_slat, dark_slat, play_set.select_no_set)
        point_counter("Points: " + str(play_set.board.points), 30, 170, 150, 50, light_slat)
    
    pygame.display.flip()