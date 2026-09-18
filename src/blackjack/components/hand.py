"""Blackjack Hand Management Module.

This module provides the `Hand` class for managing a player's or dealer's cards
in a game of Blackjack. It tracks individual cards, calculates the total hand value
(considering Ace flexibility if implemented later), and enforces maximum value limits
to detect busts.

Classes:
    Hand: Manages the hand of the player or dealer.

Author:
    Nikolai Sandbeck
"""


class Hand:
    """Represents a hand for a player or dealer.

    This class manages the cards held by a single entity (player or dealer) in a game of Blackjack.
    It tracks the individual cards, calculates the current total value of the hand, and enforces
    a maximum allowed value to detect when a hand has 'busted' (exceeded 21 or 17).

    Attributes:
        __cards: A list of cards, where each card is represented as a [suit, value] pair.
        __max_total_value: The maximum allowed total value for the hand
                           (typically 21 for a player and 17 for a dealer).
        __value: The current sum of the values of all cards in the hand.

    Example:
        hand = Hand()
        hand.set_max_total_value(21)
        hand.add_card(["♥", 10])
        hand.add_card(["♣", 5])
        hand.get_hand_value()
    """

    def __init__(self):

        self.__cards: list[str, int] = []
        self.__max_total_value: int = 0
        self.__value: int = 0


    def set_max_total_value(self, max_total_value: int) -> None:
        """Sets the maximum allowed total value for the hand.
        
        For players it is 21 and for dealers it is 17.
        
        Args:
            max_total_value: The integer limit for the sum of card values. Must be either 17 or 21.

        Raises:
            ValueError: If max_total_value is not an integer, or if it is not 17 or 21.
        """

        if not isinstance(max_total_value, int):
            raise ValueError("Error: max_total_value has to be an integer.")

        if max_total_value not in (17, 21):
            raise ValueError("Error: the max_total_value has to be either 17 or 21.")

        self.__max_total_value = max_total_value


    def add_card(self, card: list) -> None:
        """Adds a card to the hand and updates the total value.

        Args:
            card: A list containing [suit (str), value (int)].

        Raises:
            ValueError: If card is not a list, or if max_total_value has not been set.
        """

        if not isinstance(card, list):
            raise ValueError("Error: cards has to be a list of lists with an integer and a string.")

        if not self.__max_total_value:
            raise ValueError("Error: You must set a max total value first. " \
                            "Use `set_max_total_value`."
                            )

        self.__cards.append(card)
        self.__value += card[1]


    def clear_hand(self) -> None:
        """Removes all cards from the hand and resets the total value to zero.

        This method clears the internal list of cards and sets the current hand value back to 0.
        It does not reset the `max_total_value`.
        """

        self.__cards = []
        self.__value = 0


    def clear_max_total_value(self) -> None:
        """Resets the maximum allowed total value to zero."""

        self.__max_total_value = 0


    def get_hand_value(self) -> int:
        """Returns the current total value of all cards in the hand.

        Returns:
            The integer sum of the values of all cards currently in the hand.
        """

        return self.__value


    def get_max_total_value(self) -> int:
        """Returns the maximum allowed total value for the hand.

        Returns:
            The integer limit set via `set_max_total_value`.
        """

        return self.__max_total_value


    def get_cards_on_hand(self) -> tuple[str, int] | None:
        """Returns the cards the dealer or player has.

        This method provides a snapshot of the cards in the hand.
        If the hand is empty, it returns `None`.

        Returns:
            A tuple of (suit, value) tuples representing the remaining cards,
            or None if the deck is empty.
        """

        if not self.__cards:
            return None

        if len(self.__cards) == 1:
            return tuple(self.__cards[0])

        return tuple(self.__cards)
