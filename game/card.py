import random

class Card:

    def __init__(self):
      
        self.value = 0
        self.f_card = 0
        self.n_card = 0
        self.comparation_result = ""
        
    
    def draw_card(self):
     
        self.value = random.randint(1, 13)

    def get_firstCard(self):
        self.draw_card()
        self.f_card = self.value 

    def get_nextCard(self):
        self.draw_card()
        self.n_card = self.value

    def compare_cards(self):
    
    #The next card is Lower
        if(self.n_card < self.f_card):
            self.comparation_result = "l"
    #The next card is higher
        elif(self.n_card > self.f_card):
            self.comparation_result = "h"
    #The cards are the same value
        else:
            self.comparation_result = "s"

        self.f_card = self.n_card
        


         
    





