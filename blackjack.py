# William Zhu (wzhu4@uchicago.edu)


import tkinter as tk
from abc import ABC, abstractmethod
from card import Card
from deck import Deck
from hand import Hand

class GameGUI(ABC):

    def __init__(self, window):
        self._window = window
        self._canvas_width = 1024
        self._canvas_height = 400
        self._canvas = tk.Canvas(window, width=self._canvas_width, height=self._canvas_height)
        self._canvas.pack()
        window.bind("<Key>", self._keyboard_event)


    def _keyboard_event(self, event):
        key = str(event.char)

        if key == 'h':
            self.player_hit()
        elif key == 's':
            self.player_stand()
        elif key == 'r':
            self.reset()

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def player_hit(self):
        pass

    @abstractmethod
    def player_stand(self):
        pass



class BlackJack(GameGUI):
    '''
    This class inherits from GameGUI class.
    It implements the blackjack game and display relevant information.
    '''
    def __init__(self, window):
        super().__init__(window)
        Card.load_images()
        self.dk = Deck()
        self.phand = Hand() #player hand
        self.dhand = Hand() #dealer hand

        #2 cards for both player and dealer hands to begin with.
        for i in range(2):
            self.phand.add(self.dk.deal())
            self.dhand.add(self.dk.deal())

        self.pwin = 0
        self.dwin = 0
        self.statdic = {0: "In Progress... Press 'h' to hit, 's' to stand", 
                        1: "Player WINS... Press 'r' to start a new game",
                        2: "Dealer WINS... Press 'r' to start a new game",
                        3: "TIE Game...Press 'r' to start a new game"}
        self.game_status = self.statdic[0]

        self.text_color1 = 'black'
        self.text_color2 = "green"
        self.drawing()
        
        
    def drawing(self):
        '''
        This method draws relevant information on the canvas.
        '''
        #player section visualization
        self._canvas.create_text(176,20, fill=self.text_color1, font=('Copperplate', 26, 'bold'),
                                text=f'Player Hand Total: {self.phand.total}')
        self.phand.draw(self._canvas, 100, 40, self._canvas_width, self._canvas_height)

        #dealer section visualization
        self._canvas.create_text(176,175, fill=self.text_color1, font=('Copperplate', 26, 'bold'), 
                                text=f'Dealer Hand Total: {self.dhand.total}')
        self.dhand.draw(self._canvas, 100, 200, self._canvas_width, self._canvas_height)


        #referee section visualization
        self._canvas.create_text(600,360, fill=self.text_color2, font=('Baskerville', 27, 'bold'),
                                text=f'Game Status: {self.game_status}')
        self._canvas.create_text(110,350, fill=self.text_color1, font=('Copperplate', 24),
                                text=f'Dealer Wins: {self.dwin}')
        self._canvas.create_text(110,380, fill=self.text_color1, font=('Copperplate', 24),
                                text=f'Player Wins: {self.pwin}')      

        #title
        self._canvas.create_text(830,150, fill='black', font=('Luminari',72, 'bold'),
                                text=f'Blackjack')
        self._canvas.create_text(830,220, fill='black', font=('Luminari',20),
                                text=f'By William Zhu')                    


    def reset(self):
        '''
        This method resets the game and updates the canvas.
        '''
        self.phand.reset()
        self.dhand.reset()
        self.game_status = self.statdic[0]
        self.text_color2 = "green"
        #2 cards for both player and dealer hands
        for i in range(2):
            self.phand.add(self.dk.deal())
            self.dhand.add(self.dk.deal())

        self._canvas.delete(tk.ALL)
        self.drawing()

        
    def player_hit(self):
        '''
        This method performs 'hits'.
        If the game is going on, it adds a card to player's hand.
        Then it checks the outcome of each game.
        Then it updates the canvas.
        '''
        if self.game_status == self.statdic[0]:
            self.phand.add(self.dk.deal())
        if self.phand.total > 21 and self.game_status == self.statdic[0]:
            self.game_status = self.statdic[2]
            self.dwin += 1
            self.text_color2 = "red"

        self._canvas.delete(tk.ALL)
        self.drawing()

    def player_stand(self):
        '''
        This method performs 'stands'.
        If the game is going on and the sum of the cards in the dealer's hand are smaller than 17,
        the game adds new card to dealer's hand.
        Then it checks the result of the game.
        Finally, it updates the canvas.
        '''
        while self.game_status == self.statdic[0] and self.dhand.total < 17:
            self.dhand.add(self.dk.deal())
        if self.dhand.total > 21 or self.dhand.total < self.phand.total:
            if self.game_status == self.statdic[0]:
                self.pwin += 1
            self.game_status = self.statdic[1]
            
        elif self.dhand.total > self.phand.total:
            if self.game_status == self.statdic[0]:
                self.dwin += 1
            self.game_status = self.statdic[2]
            
        elif self.dhand.total == self.phand.total:
            self.game_status = self.statdic[3]
        self.text_color2 = "red"
        self._canvas.delete(tk.ALL)
        self.drawing()




def main():
    window = tk.Tk()
    window.title("Blackjack")
    game = BlackJack(window)
    window.mainloop()


if __name__ == "__main__":
    main()
