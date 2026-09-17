

class Hand:

    def __init__(self):

        self.__cards: list[str, int] = []
        self.__max_total_value: int = 0
        self.__value: int = 0


    def set_max_total_value(self, max_total_value: int) -> None:

        if not isinstance(max_total_value, int):
            raise ValueError("Error: max_total_value has to be an integer.")

        self.__max_total_value = max_total_value


    def add_card(self, card: list) -> None:

        if not isinstance(card, list):
            raise ValueError("Error: cards has to be a list of lists with an integer and a string")

        if not self.__max_total_value:
            raise ValueError("Error: You must set a max total value first. Use `set_max_total_value`.")

        self.__cards.append(card)
        self.__value += card[1]


    def clear_hand(self) -> None:

        self.__cards = []
        self.__value = 0


    def clear_max_total_value(self) -> None:

        self._max_total_value = 0


    def get_hand_value(self):

        return self.__value


    def get_max_total_value(self) -> int:

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
