


class Cards:

    def __init__(self):
        self.__deck: dict[str, list[int]] = {}


    def set_deck(self):

        deck = {
            "number_cards_clubs": [2, 3, 4, 5, 6, 7, 8, 9, 10],
            "number_cards_diamonds": [2, 3, 4, 5, 6, 7, 8, 9, 10],
            "number_cards_hearts": [2, 3, 4, 5, 6, 7, 8, 9, 10],
            "number_cards_spades": [2, 3, 4, 5, 6, 7, 8, 9, 10],
            "picture_cards_clubs": [2, 3, 4, 5, 6, 7, 8, 9, 10],
            "picture_cards_diamonds": [10, 10, 10],
            "picture_cards_hearts": [10, 10, 10],
            "picture_cards_spades": [10, 10, 10],
            "ace_clubs": [1, 11],
            "ace_diamonds": [1, 11],
            "ace_hearts": [1, 11],
            "ace_spades": [1, 11],
        }

        mixed_deck = {}

        for mii in deck.keys():
            if "ace_" not in mii:
                print(mii)



        self.__deck = deck

    # def pick_a_card(self, number_of_cards):

    #     get_keys = self

        

    # def get_deck(self):
    #     pass

    # def pick_card(self):
    #     self.__set_deck()

        # self.
    


mii = Cards()
mii.set_deck()
# mii.get_deck()