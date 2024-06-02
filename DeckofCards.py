import random
from re import S
from socketserver import DatagramRequestHandler

class card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
class Deck:
    def __init__(self):
        self.ranks = {'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'}
        self.suits = {'Hearts', 'Diamonds', 'Clubs', 'Spades'}
        self.reset()
        
    def reset(self):
        self.deck = [card(rank, suit) for suit in self.suits for rank in self.ranks]
        
    def shuffle(self):
        random.shuffle(self.deck)
            
    def deal(self):
        if len(self.deck) == 0:
            return None
        return self.deck.pop()
    
    def count(self):
        return len(self.deck)
    
    print("Welcome to the Deck of Cards!")
    print("There is a deck of 52 cards")
    
    deck = deck()
    
    deck.shuffle()
    
    num_cards_to_deal = int(input("How many cards would you like?"))
    dealt_cards = []
    
    for _ in range(num_cards_to_deal):
        card = deck.deal()
        if card is not None:
            dealt_cards.appeal(f"{card.rank} of {card.suit}")
        else:
            print("No more cards in the deck")
     
        if dealt_cards:
            print("Death cards:")
        for card in dealt_cards:
            print(card)
            
    remanining_count = deck.count()
    print(f"There are {remanining_count} cards left in the deck")

    print("Good Luck")
    
          
