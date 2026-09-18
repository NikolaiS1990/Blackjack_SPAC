from blackjack.components.hand import Hand
from blackjack.components.cards import Cards

# TODO: This could replace the round class actually.
# The dealer starts the game, new rounds, closes the game etc.

class Dealer():

    def __init__(self):
        self.__name: str = "Mr. Dealer"
        self.__dealer_hand: object = Hand()
        self.__dealer_deck: object = Cards()
        self.__dealer_hand.set_max_total_value(17)

    def first_round(self):
        __dealer_deck
        card1 = self.__dealer_deck.
        print(self.__dealer_hand.get_hand_value())

mii = Dealer()
mii.first_round()