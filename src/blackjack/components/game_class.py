from blackjack.components.hand import Hand
from blackjack.components.cards import Cards
from blackjack.components.pool import Pool

import sys
import os
from subprocess import call

class Game():
    def __init__(self):
        self.__dealer_hand: object = Hand()
        self.__player_hand: object = Hand()

        self.__dealer_deck: object = Cards()
        self.__player_deck: object = Cards()

        self.__pool: object = Pool()

        self.__run_game: bool = False

    def start_game(self) -> None:
        self.__run_game = True

    def __prep_cards(self) -> None:
        self.__dealer_hand.set_max_total_value(17)
        self.__player_hand.set_max_total_value(21)

        self.__dealer_deck.set_deck()
        self.__dealer_deck.shuffle_cards()
        self.__dealer_hand.add_card(self.__dealer_deck.pick_card())
        self.__dealer_hand.add_card(self.__dealer_deck.pick_card())

        # Show dealer's hand
        dealer_hand = self.__dealer_hand.get_cards_on_hand()[0]
        print(f"Dealer's hand: ({dealer_hand})")

        print("\n\n")

        self.__player_deck.set_deck()
        self.__player_deck.shuffle_cards()
        self.__player_hand.add_card(self.__player_deck.pick_card())
        self.__player_hand.add_card(self.__player_deck.pick_card())

        # Show player's hand
        player_hand = self.__player_hand.get_cards_on_hand()
        print(f"Players's hand: {player_hand}")
        print(f"Players's hand value: {self.__player_hand.get_hand_value()}")

    def actions(self) -> None:

        demand_action = True

        while demand_action:

            possible_actions = ["hit", "stand", "exit"]
            player_input = input("hit, stand or exit: ").lower()

            if not player_input in possible_actions:
                print("\n\nYou must select between: hit, stand or exit")
            else:
                demand_action = False
                return player_input

    def __ace_handler(self, person: str) -> tuple[str, int]:

        if person == "player":
            picked_card = self.__player_deck.pick_card()
            currenct_value = self.__player_hand.get_hand_value()
        elif person == "dealer":
            picked_card = self.__dealer_deck.pick_card()
            currenct_value = self.__dealer_hand.get_hand_value()
        else:
            print("something went wrong")
            sys.exit(1)

        if 11 == picked_card[1] and picked_card[1] + currenct_value > 21:
            card = [picked_card[0], 1]
        else:
            card = picked_card

        return card
        

    def __show_hands(self) -> None:
        print(f"Dealer's hand: {self.__dealer_hand.get_cards_on_hand()}")
        print(f"Dealer's hand value: {self.__dealer_hand.get_hand_value()}")

        print("\n\n")

        print(f"Players's hand: {self.__player_hand.get_cards_on_hand()}")
        print(f"Players's hand value: {self.__player_hand.get_hand_value()}")


    def round(self) -> None:

        self.__prep_cards()

        while self.__run_game == True:

            if self.__dealer_hand.get_hand_value() > 201:
                print("Dealer lost, the value of the hand exeeded 21!")
                self.__run_game = False
                return

            if self.__player_hand.get_hand_value() > 201:
                print("Player lost, the value of the hand exeeded 21!")
                self.__run_game = False
                return

            action = self.actions()

            if action == "exit":
                self.__run_game = False
            elif action == "stand":
                call('cls' if os.name == 'nt' else 'clear')

                if self.__player_hand.get_hand_value() >= self.__dealer_hand.get_hand_value():
                    self.__show_hands()
                    print("Player wins")
                else:
                    self.__show_hands()
                    print("Dealer wins")

                self.__run_game = False
                return
            elif action == "hit":
                if self.__dealer_hand.get_hand_value() > self.__dealer_hand.get_max_total_value():
                    self.__player_hand.add_card(self.__ace_handler("player"))
                    self.__dealer_hand.add_card(self.__ace_handler("dealer"))
                else:
                    self.__player_hand.add_card(self.__ace_handler("player"))

                self.__show_hands()

            else:
                print("Something went wrong, closing the app")
                sys.exit(1)
    
