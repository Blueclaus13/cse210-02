from card import Card
import random

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        guess (string): The User's guess
        card (Object): The object is to control all related with cards
        
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card = Card()
        self.is_playing = True
        self.guess = ""
        self.score = 300
        

        print("     Welcome to Hilo Game\n")
        print("You start the game with 300 points")

        #We assigned the first value
        self.card.get_firstCard()
        self.first_card = self.card.f_card

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

        print("-----------------------------------------")
        print(f"\nYour card is: {self.card.f_card}")
        self.guess = input("Guess, the next card is Higher or Lower [h/l]? ")
        
    
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """

        #We drawcard
        self.card.get_nextCard()
        self.next_card = self.card.n_card

        #Call Card instance to compare the value of cards and the points 
        round_points = self.card.compare_cards(self.guess)
        self.score += round_points
 
        
        
    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        #Result of round
        print(f"The next card was: {self.next_card}")
        print(f"Your score is: {self.score} \n")
        print("-----------------------------------------")
        
        #The user decides if to keep playing. 
        play_again = input("Do you want to play again (y/n)? ")
        self.is_playing = (play_again.lower() == "y" or self.score <= 0)

        #Good bye message
        if not self.is_playing:
            print("\n     Game Over. \nCome to play soon")
            return

        
        