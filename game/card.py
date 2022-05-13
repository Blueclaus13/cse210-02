import random

class Card:
    """
    Attributes:
        value (int): Save the value of the drawcard
        f_card (int): Save the value of the first card
        n_card (int): Save the value of the next card
        score (int): Save the score gained in the round
    
    """

    def __init__(self):

        self.value = 0
        self.f_card = 0
        self.n_card = 0
        self.score = 0
        
    
    def draw_card(self):
     
        self.value = random.randint(1, 13)

    def get_firstCard(self):
        self.draw_card()
        self.f_card = self.value 

    def get_nextCard(self):
        self.draw_card()
        self.n_card = self.value

    def compare_cards(self, user_guess):

        self.score = 0
        comparation_result = ""
    
        #The next card is Lower
        if(self.n_card < self.f_card):
            comparation_result = "l"
        #The next card is higher
        elif(self.n_card > self.f_card):
            comparation_result = "h"
        #The cards are the same value
        else:
            comparation_result = "s"

        #Compare the User's answer with the value comparation

        #User's guess is correct
        if (user_guess.lower() == comparation_result):
            self.score = self.score + 100
        #The value of the cards was the same. Score doesn't change
        elif (comparation_result == "s"):
            print("\nWow, you got the same card again! Super lucky!")
            print("Nothing happens and we will keep playing!") 
        #User's guess was incorrect
        else: 
            self.score = self.score - 75
        #we change the value of the cards for the next round
        self.f_card = self.n_card

        return self.score
        


         
    





