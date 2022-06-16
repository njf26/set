import random
import itertools
from constants import *

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for num in NUMBERS:
            for shape in SHAPES:
                for color in COLORS:
                    for pattern in FILL_PATTERNS:
                        self.cards.append((num, shape, color, pattern))

    def shuffle(self):
        random.shuffle(self.cards)


    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()

    def isGameOver(self):
        return len(self.cards) == 39 #10 sets of 3 have been removed from the board, end game early

class Board:
    def __init__(self, deck):
        self.deck = deck
        self.cards = [self.deck.deal() for i in range(12)]
        self.card_img = []
        self.points = 0
        self.display_cards()
        self.index_subsets = [i for i in itertools.combinations({j for j in range(12)}, 3)]

    def add_3_cards(self, card1, card2, card3):
        self.cards.append(card1)
        self.cards.append(card2)
        self.cards.append(card3)

    def check_if_set(self, card1, card2, card3):
        #check if 3 cards are a set
        if (card1[0] == card2[0] and card2[0] == card3[0]) or (card1[0] != card2[0] and card2[0] != card3[0] and card1[0] != card3[0]):
            if (card1[1] == card2[1] and card2[1] == card3[1]) or (card1[1] != card2[1] and card2[1] != card3[1] and card1[1] != card3[1]):
                if (card1[2] == card2[2] and card2[2] == card3[2]) or (card1[2] != card2[2] and card2[2] != card3[2] and card1[2] != card3[2]):
                    if (card1[3] == card2[3] and card2[3] == card3[3]) or (card1[3] != card2[3] and card2[3] != card3[3] and card1[3] != card3[3]):
                        return True
        return False

    def check_if_no_set(self):
      l = len(self.cards)
      for subset in self.index_subsets:
        if self.check_if_set(self.cards[subset[0]],self.cards[subset[1]],self.cards[subset[2]]):
          self.points -= 1
          return True

      self.points += 5
      self.remove_3_cards(self.cards[l-1], self.cards[l-2], self.cards[l-3])
      self.add_3_cards(self.deck.deal(), self.deck.deal(), self.deck.deal())
      self.display_cards()
      return not self.deck.isGameOver()

    def play_round(self, card1, card2, card3):
        if self.check_if_set(card1, card2, card3):
            self.points += 5
            self.remove_3_cards(card1, card2, card3)
            self.add_3_cards(self.deck.deal(), self.deck.deal(), self.deck.deal())
            self.display_cards()
        else:
          self.points -= 1

        return not self.deck.isGameOver()

    def remove_3_cards(self, card1, card2, card3):
        self.cards.remove(card1)
        self.cards.remove(card2)
        self.cards.remove(card3)

    def display_cards(self):
        self.card_img = []
        for card in self.cards:
            cards = card[0] + "_" + card[1] + "_" + card[2] + "_" + card[3] + ".png"
            self.card_img.append(cards)
    
    def addPoint(self):
      self.points += 1

    def removePoint(self):
      self.points -= 1
