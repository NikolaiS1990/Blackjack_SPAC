"""Module for managing the betting pool amount.

This module provides the Pool class to handle the state of the betting pool,
including updating the amount based on win/loss outcomes and retrieving
the current balance.

Classes:
    Pool: Manages a betting pool's amount.

Author:
    Nikolai Sandbeck
"""


class Pool:
    """A class to manage a betting pool's amount.

    Attributes:
        __amount (int): The private integer representing the current pool balance.

    usage examples:
        pool = Pool()
        pool.get_amount()
        pool.amount_manager(50, True)
    """

    def __init__(self):
        self.__amount: int = 200


    def amount_manager(self, points: int, win: bool) -> None:
        """Updates the pool amount based on a bet outcome.

        Args:
            points (int): The number of points to add or subtract.
            win (bool): If True, adds points to the pool. If False, subtracts points.
        """

        if not win:
            self.__amount -= points
        else:
            self.__amount += points


    def get_amount(self) -> int:
        """Returns the current amount in the pool.

        Returns:
            int: The current balance of the pool.
        """

        return self.__amount
