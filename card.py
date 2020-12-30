# William Zhu (wzhu4@uchicago.edu)

from PIL import ImageTk
import os

class Card:
    '''
    The Card class specify information for the 52 cards.
    '''
    CLUBS = "clubs"
    DIAMONDS = "diamonds"
    HEARTS = "hearts"
    SPADES = "spades"

    card_images = {}

    def __init__(self, suits, value, type='n'):
        self.suits = suits
        self.ivalue = value
        self.type = type #'n', 'j', 'q', 'k'

    @classmethod
    def load_images(cls):
        '''
        This class method loads the 52 images to the card_image class attribute.
        '''
        for j in ["clubs", "hearts", "diamonds", "spades"]:
            for i in range(2, 11):
                address = os.getcwd() + f'/images/{i}_of_{j}.gif'
                cls.card_images[(j, i, 'n')] = ImageTk.PhotoImage(file=address)
            
            add_ace = os.getcwd() + f'/images/1_of_{j}.gif'
            cls.card_images[(j, 11, 'n')] = ImageTk.PhotoImage(file=add_ace)

            add_j = os.getcwd() + f'/images/11_of_{j}.gif'
            cls.card_images[(j, 10, 'j')] = ImageTk.PhotoImage(file=add_j)

            add_q = os.getcwd() + f'/images/12_of_{j}.gif'
            cls.card_images[(j, 10, 'q')] = ImageTk.PhotoImage(file=add_q)

            add_k = os.getcwd() + f'/images/13_of_{j}.gif'
            cls.card_images[(j, 10, 'k')] = ImageTk.PhotoImage(file=add_k)


    @property
    def value(self):
        '''
        This method returns the value for each card.
        '''
        return self.ivalue

    @property
    def image(self):
        '''
        This method returns the image of each card.
        '''
        return Card.card_images[(self.suits, self.value, self.type)]
