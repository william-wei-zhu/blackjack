# William Zhu (wzhu4@uchicago.edu)

import random
from card import Card

class Deck:
    '''
    This class hold the collection of cards in the game.
    '''
    def __init__(self):
        self.deck = []
        self.dealt = []
        
        for j in ["clubs", "diamonds", "hearts", "spades"]:
            for i in range(2, 12):
                self.deck.append(Card(j, i, 'n'))
            self.deck.append(Card(j, 10, 'j'))
            self.deck.append(Card(j, 10, 'q'))
            self.deck.append(Card(j, 10, 'k'))
        random.shuffle(self.deck)

    def deal(self):
        '''
        This method removes the first card from the deck list, 
        returns it, and add it to the dealt list.
        The method also checks that, if the size of the deck is 13,
        shuffle method is ran.
        '''
        self.dealt.append(self.deck[0])
        out = self.deck.pop(0)
        if self.size == 13:
            self.shuffle()
        return out
        
    @property
    def size(self):
        '''
        This property returns the number of cards in the deck list.
        '''
        return len(self.deck)

    def shuffle(self):
        '''
        This property randomly shuffles the cards in dealt list.
        It then adds all the cards in dealt list to the end of deck list.
        Then it clears the dealt list.
        '''
        random.shuffle(self.dealt)
        self.deck.extend(self.dealt)
        self.dealt = []