"""Blackjack Card Deck Management.
This module provides the Cards class to manage a standard 52-card deck
for the game of Blackjack. It handles deck initialization, shuffling,
card drawing, and deck inspection.
Classes:
    Cards: Manages the state and operations of the card deck.

Author:
    Nikolai Sandbeck
"""


from itertools import chain
import random


class Cards:
    """Manages a standard 52-card deck for Blackjack.
    This class handles deck initialization, shuffling, card drawing, and inspection.
    Each card is represented as a tuple of (suit_symbol, value).

    Attributes:
        __deck: Internal list storing the current state of the deck.

    Usage Example:
        deck = Cards()
        deck.set_deck()
        deck.shuffle_cards()
        deck.pick_card()
    """
    def __init__(self):
        self.__deck: list[list, str] = []


    def set_deck(self) -> None:
        """Initialize the deck with a standard 52-card Blackjack set.

        This method constructs the deck from a structured dictionary containing
        number cards, picture cards (all valued at 10), and Aces (valued at 11).
        The dictionary structure allows for easy verification of card counts
        and simple modification of card values or suits.

        The internal list is flattened from the dictionary values, resulting in
        a list of lists where each tuple contains:
            - suit: I.e a unicode string ('♣', '♦', '♥', '♠').
            - value: An integer representing the card's point value.

        Returns:
            None  
        """

        deck = {
            "number_cards_clubs": [["♣", 2], ["♣", 3], ["♣", 4], ["♣", 5], ["♣", 6], ["♣", 7], ["♣", 8], ["♣", 9], ["♣", 10]],
            "number_cards_diamonds": [["♦", 2], ["♦", 3], ["♦", 4], ["♦", 5], ["♦", 6], ["♦", 7], ["♦", 8], ["♦", 9], ["♦", 10]],
            "number_cards_hearts": [["♥", 2], ["♥", 3], ["♥", 4], ["♥", 5], ["♥", 6], ["♥", 7], ["♥", 8], ["♥", 9], ["♥", 10]],
            "number_cards_spades": [["♠", 2], ["♠", 3], ["♠", 4], ["♠", 5], ["♠", 6], ["♠", 7], ["♠", 8], ["♠", 9], ["♠", 10]],
            "picture_cards_clubs": [["Jack ♣", 10], ["Queen ♣", 10], ["King ♣", 10]],
            "picture_cards_diamonds": [["Jack ♦", 10], ["Queen ♦", 10], ["King ♦", 10]],
            "picture_cards_hearts": [["Jack ♥", 10], ["Queen ♥", 10], ["King ♥", 10]],
            "picture_cards_spades": [["Jack ♠", 10], ["Queen ♠", 10], ["King ♠", 10]],
            "ace_clubs": [["Ace ♣", 11]],
            "ace_diamonds": [["Ace ♦", 11]],
            "ace_hearts": [["Ace♥", 11]],
            "ace_spades": [["Ace ♠", 11]]
        }

        self.__deck = list(chain.from_iterable(deck.values()))

    def shuffle_cards(self) -> None:
        """Method for shuffling the card deck.
    
        This method randomizes the order of cards in the internal deck list
        using Python's `random.shuffle`.

        It updates the __deck attribute with the randomized list.

        Note:
            This method should be called after `set_deck()` and before
            drawing any cards to ensure a fair random distribution.

        Returns:
            None
        """

        deck = self.__deck

        # This changes the updates of total_deck with a shuffled list
        random.shuffle(deck)

        self.__deck = deck

    def pick_card(self) -> tuple[str, int] | None:
        """Draw a random card from the deck.

        This method selects a random card from the current deck, removes it
        from the deck, and returns it. If the deck is empty, it
        returns `None`.

        Returns:
            A tuple containing (suit, value) of the drawn card, or None if
            the deck is empty.
        """

        if not self.__deck:
            return None

        card_number = random.randrange(len(self.__deck))

        return self.__deck.pop(card_number)

    def get_deck(self) -> tuple[str, int] | None:
        """Return the current state of the deck.

        This method provides a snapshot of the remaining cards in the deck.
        If the deck is empty, it returns `None`.

        Returns:
            A tuple of (suit, value) tuples representing the remaining cards,
            or None if the deck is empty.
        """

        if not self.__deck:
            return None

        return tuple(self.__deck)
