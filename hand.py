
# William Zhu (wzhu4@uchicago.edu)

import tkinter as tk

class Hand:
    '''
    This class describes the collection of cards.
    '''
    def __init__(self):
        self.hand = []

    def reset(self):
        '''
        This method clears the items in the hand list.
        '''
        self.hand = []

    def add(self, card):
        '''
        This method adds a card object to the hand list.
        '''
        self.hand.append(card)

    @property
    def total(self):
        '''
        This property returns the sum of values of the cards in the hand.
        '''
        sum = 0
        for i in self.hand:
            sum += i.value
        return sum

    def draw(self, canvas, start_x, start_y, canvas_width, canvas_height):
        '''
        This method creates draw on canvas all the card images in the hand.
        '''
        for i in range(len(self.hand)):
            x = start_x + 100*i
            canvas.create_image(x, start_y, anchor=tk.NW, image=self.hand[i].image)

        self._canvas = canvas

    