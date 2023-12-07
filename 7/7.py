from __future__ import annotations
from collections import Counter
from dataclasses import dataclass
from functools import cmp_to_key

card_order = [
    'A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'
]
card_order.reverse()


@dataclass
class Hand(object):
    _cards_original: str
    _cards: list[str]
    _votes: str
    _score: int
    _cards_sorted: str

    def __init__(self, cards: str, votes: str):
        self._cards_original = cards
        self._cards = list(cards)
        self._votes = votes
        self._cards_sorted = self._sort_hand()
        self._score = self.get_score_for_hand()

    def _sort_hand(self):
        sorted_symbols = sorted(self._cards, key=lambda x: card_order.index(x), reverse=True)
        return ''.join(sorted_symbols)

    def __lt__(self, other: Hand):
        return self.compare(self, other) == -1

    def __le__(self, other: Hand):
        return self.compare(self, other) in [-1, 0]

    def __eq__(self, other: Hand):
        return self.compare(self, other) == 0

    def __gt__(self, other: Hand):
        return self.compare(self, other) == 1

    def __ge__(self, other: Hand):
        return self.compare(self, other) in [1, 0]

    def __repr__(self):
        return f"Hand:{self._cards_sorted} {self._votes} ({self._cards_original})/{self._score}"
    def __str__(self):
        return f"Hand: {self._cards_sorted} {self._votes} ({self._cards_original})"
    @staticmethod
    def compare(self: Hand, other: Hand):
        """
>>> Hand.compare(Hand("AAAAA",""),Hand("AAAAA",""))
0
>>> Hand.compare(Hand("AAAAA",""),Hand("AAAAK",""))
-1

>>> Hand.compare(Hand("33332",""),Hand("2AAAA",""))
-1
>>> Hand.compare(Hand("2AAAA",""),Hand("33332",""))
1
>>> Hand.compare(Hand("77888",""),Hand("77788",""))
-1
>>> Hand.compare(Hand("TTTT3",""),Hand("TTATT",""))
1

        """
        score1 = self._score
        score2 = other._score

        if score1 != score2:
            if score1 > score2:
                return -1  # left hand is better
            else:
                return 1  # right hand is better

        # scores are equal, we compare the highest card
        pointer = 0
        """If two hands have the same type, a second ordering rule takes effect. 
        Start by comparing the first card in each hand. If these cards are different, 
        the hand with the stronger first card is considered stronger. If the first card 
        in each hand have the same label, however, then move on to considering 
        the second card in each hand. If they differ, the hand with the higher second card wins; 
        otherwise, continue with the third card in each hand, then the fourth, then the fifth.

        So, 33332 and 2AAAA are both four of a kind hands, 
        but 33332 is stronger because its first card is stronger. 
        Similarly, 77888 and 77788 are both a full house, but 77888 is stronger 
        because its third card is stronger (and both hands have the same first and second card).
        """
        # we compare by highest card, and if equal look at next card
        h1 = list(self._cards_original)
        h2 = list(other._cards_original)
        while True:
            if pointer == len(h1):
                return 0  # draw, no more cards to compare
            L = h1[pointer]
            R = h2[pointer]
            Ls = card_order.index(L)
            Rs = card_order.index(R)
            if Ls > Rs:
                return -1  # left card is better
            elif Ls < Rs:
                return 1  # right card is better
            else:
                pointer += 1

    # to get card, A is highest and biggest number
    # card_order.index()

    # 6 Five of a kind, where all five cards have the same label: AAAAA
    # 5 Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    # 4 Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    # 3 Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    # 2 Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    # 1 One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    # 0 High card, where all cards' labels are distinct: 23456
    def get_score_for_hand(self) -> int:
        """
        >>> Hand.get_score_for_hand(Hand("AAAAA",""))
        6
        >>> Hand.get_score_for_hand(Hand("AAAAK",""))
        5
        >>> Hand.get_score_for_hand(Hand("AAAKK",""))
        4
        >>> Hand.get_score_for_hand(Hand("AAAKQ",""))
        3
        >>> Hand.get_score_for_hand(Hand("AAKKQ",""))
        2
        >>> Hand.get_score_for_hand(Hand("AAKQJ",""))
        1
        >>> Hand.get_score_for_hand(Hand("AKQJT",""))
        0

        """
        counts = list(Counter(self._cards).values())
        counts.sort(reverse=True)
        if len(set(self._cards)) == 1:  # five of a kind
            return 6
        if len(set(self._cards)) == 2 and counts[0]==4:  # four of a kind
            return 5
        if counts[0] == 3 and counts[1] == 2:  # full house
            return 4
        if counts[0] == 3 and counts[1] == 1:  # three of a kind
            return 3
        if counts[0] == counts[1] == 2:  # two pairs
            return 2
        if counts[0] == 2 and counts[1] == 1:  # one pair
            return 1
        if counts[0] == 1:
            return 0
        return -1


# f = "input.txt"
f = "sample.txt"

def main(inputname):
    """
    >>> main("sample.txt")
    6440
    """
    with open(inputname, 'r') as input_file:
        game = [
            Hand(hand, votes)
            for hand, votes
            in [
                line.strip().split(" ")
                for line
                in input_file.readlines()
            ]
        ]

        total = 0

        game_sorted = sorted(game.copy(), key=cmp_to_key(Hand.compare), reverse=True)

        for num, hand in enumerate(game_sorted, start=1):
            total += int(hand._votes) * num
    return total

if __name__ == "__main__":
    total = main("input.txt")
    print(total)


# 250425418 IS NOT ANSWER, too high
# 250925918 IS NOT ANSWER, too high
# 249268714 IS NOT ANSWER, too low
# 251576580 IS NOT ANSWER
# 251362095 NOT
# 249638405
