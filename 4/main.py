def main():
    with open("input.txt", "r") as f:
        inputs = f.readlines()
    total_points = 0
    for input in inputs:
        winning_nums, card_nums = input.split(":")[1].split("|")
        winning_nums = [int(i) for i in winning_nums.replace("  ", " ").replace("\n", "").split(" ") if i]
        card_nums = [int(i) for i in card_nums.replace("  ", " ").replace("\n", "").split(" ") if i]
        intsct = list(set(card_nums).intersection(winning_nums))
        score = matches_to_score(matches=len(intsct))
        total_points = total_points + score
    print(total_points)


def matches_to_score(matches: int) -> int:
    if matches in [0, 1]:
        return matches
    return 1 * (2 ** (matches - 1))


if __name__ == "__main__":
    main()

