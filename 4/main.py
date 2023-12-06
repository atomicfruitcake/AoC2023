def main():
    with open("input.txt", "r") as f:
        inputs = f.readlines()
    total_points = 0
    scratchcards = [1] * len(inputs)

    for idx, input in enumerate(inputs):
        winning_nums, card_nums = input.split(":")[1].split("|")
        winning_nums = [int(i) for i in winning_nums.replace("  ", " ").replace("\n", "").split(" ") if i]
        card_nums = [int(i) for i in card_nums.replace("  ", " ").replace("\n", "").split(" ") if i]
        intsct = list(set(card_nums).intersection(winning_nums))

        num_matches = len(intsct)

        for i in range(num_matches):
            scratchcards[idx + i + 1] = scratchcards[idx + i + 1] + scratchcards[idx]

        # score = matches_to_score(matches=len(intsct))
        # total_points = total_points + score
    print(total_points)
    total_cards = sum(scratchcards)
    print(total_cards)


def matches_to_score(matches: int) -> int:
    if matches in [0, 1]:
        return matches
    return 1 * (2 ** (matches - 1))


if __name__ == "__main__":
    main()

