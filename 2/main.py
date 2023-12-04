def main():
    with open("input.txt", "r") as f:
        inputs = f.readlines()
    print(sum([get_game_power(i) for i in inputs]))


def get_game_power(input: str) -> int:
    num_red = 0
    num_green = 0
    num_blue = 0
    game_possible = True
    game, rounds = input.split(":")
    game_id = int(game.replace("Game ", ""))
    rounds = rounds.split(";")
    for _round in rounds:
        balls = _round.split(",")
        for ball in balls:
            if "red" in ball:
                num_reds = int(ball.replace(" red", ""))
                if num_reds > num_red:
                    num_red = num_reds
            if "green" in ball:
                num_greens = int(ball.replace(" green", ""))
                if num_greens > num_green:
                    num_green = num_greens
            if "blue" in ball:
                num_blues = int(ball.replace(" blue", ""))
                if num_blues > num_blue:
                    num_blue = num_blues

    return num_red * num_blue * num_green


if __name__ == "__main__":
    main()
