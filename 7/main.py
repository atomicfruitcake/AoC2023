from dataclasses import dataclass
from typing import Dict

@dataclass
class Hand:
    cards: str
    bid: int
    hand_type = ""
    card_count: Dict = None


full_houses = []
four_of_a_kind = []
three_of_a_kind = []
two_pair = []
one_pair = []
high_card = []

letters = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


def get_hands_data() -> list:
    with open("input.txt", "r") as f:
        inputs = f.readlines()
    out = []
    for i in inputs:
        cards, bid = i.split(" ")
        out.append(Hand(cards=cards, bid=int(bid.replace("\n", ""))))
    return out


def sort_hands_by_type(hands_data):
    for hand in hands_data:
        card_count = {}
        for card in hand.cards:
            try:
                card_count[card] += 1
            except:
                card_count[card] = 1
        hand.card_count = card_count
        print(f"count: {len(card_count)}")
        if len(card_count) == 1:
            full_houses.append(hand)
        if len(card_count) == 2:
            if max(card_count.values()) == 4:
                four_of_a_kind.append(hand)
            else:
                three_of_a_kind.append(hand)
        if len(card_count) == 3:
            if max(card_count.values()) == 2:
                two_pair.append(hand)
            else:
                three_of_a_kind.append(hand)
        if len(card_count) == 4:
            one_pair.append(hand)
        if len(card_count) == 5:
            high_card.append(hand)


def main():
    hands_data = get_hands_data()
    sort_hands_by_type(hands_data=hands_data)
    # sort_hands_by_score()
    print(full_houses)
    print(four_of_a_kind)
    print(three_of_a_kind)

    pass


if __name__ == "__main__":
    main()
