from card import Card
import random

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        first_card (int): save the value of the first card.
        next_card (int): save the value of the next card.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card = Card()
        self.first_card = 0
        self.next_card = 0
        self.is_playing = True
        self.guess = ""
        self.score = 300
        self.total_score = 0
        

        
        print("Welcome to Hilo Game")
        print("You start the game with 300 points")

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """

        self.card.draw_card()
        self.first_card = self.card.value
        print(f"Your first card is: {self.first_card}")
        self.guess = input("Guess, the next card is Higher or Lower [h/l]? ")
        
    
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        

        if not self.is_playing:
            return 

        self.card.draw_card()
        self.next_card = self.card.value

    
        if (self.next_card < self.first_card and self.guess.lower() == "l"):
            self.score = self.score + 100
        elif (self.next_card > self.first_card and self.guess.lower() == "h"):
            self.score = self.score + 100
        elif (self.next_card < self.first_card and self.guess.lower() == "h"):
            self.score = self.score - 75
        elif (self.next_card > self.first_card and self.guess.lower() == "l"):
            self.score = self.score - 75 
        else: 
            print("Wow, you got the same card again! Super lucky!")
            print("Nothing happens and we will keep playing!")        
        
        self.first_card = self.next_card
        

        
    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        
        print(f"The next card was: {self.next_card}")
        print(f"Your score is: {self.score} \n")
        
        play_again = input("Do you want to play again (y/n)? ")
        self.is_playing = (play_again.lower() == "y" or self.score <= 0)

        if not self.is_playing:
            print("Game Over. \nCome to play soon")
            return

        
        