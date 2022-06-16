from set_deck import *
from constants import *
import sys

class Play:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.board = Board(self.deck)
        self.selected_cards = []
    
    def select_no_set(self):
      self.selected_cards = []
      return self.board.check_if_no_set() #true or false if game continues or not

    def select_card(self, card):
      for selected_card in self.selected_cards:
        if card == selected_card: 
          #self.board.removePoint()
          return True
      self.selected_cards.append(card)

      if len(self.selected_cards) == 3:
        continue_game = self.board.play_round(self.selected_cards[0],self.selected_cards[1],self.selected_cards[2])
        self.selected_cards = []
        if not continue_game:
          return False
      
      return True

    def exit(self):
        sys.exit()
    
    def step(self, action):
      points_so_far = self.board.points
      done = 0
      #action is the index of self.board.index_subsets. If it's equal to the length of that, then it's no set
      if action == len(self.board.index_subsets):
        done = not self.select_no_set()
      else:
        card0 = self.board.cards[self.board.index_subsets[action][0]]
        card1 = self.board.cards[self.board.index_subsets[action][1]]
        card2 = self.board.cards[self.board.index_subsets[action][2]]

        self.select_card(card0)
        self.select_card(card1)
        done = not self.select_card(card2)
      
      reward = self.board.points - points_so_far
      
      return reward, self.get_state(), done
    
    def get_state(self):
      #state consists of 48 observations: number, shape, color, fill pattern for all 12 cards
      state = []
      for i in range(len(self.board.cards)):
        state.append(NUMBERS.index(self.board.cards[i][0]))
        state.append(SHAPES.index(self.board.cards[i][1]))
        state.append(COLORS.index(self.board.cards[i][2]))
        state.append(FILL_PATTERNS.index(self.board.cards[i][3]))
      return state