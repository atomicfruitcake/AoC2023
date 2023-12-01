
num_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def sum_digits_in_inputs():
    with open("input.txt", "r") as f:
        inputs = f.readlines()
    print(sum([extract_digits(i) for i in inputs]))


def extract_digits(string: str) -> int:
    return int(f"{main(string=string)}{main(string=string[::-1])}")


def main(string: str) -> int:
    first_char = ""
    last_char = ""
    low_char = ""
    high_char = ""
    for idx, char in enumerate(string):
        try:
            int(char)
            lowest_num_idx = idx
            for num_str in num_map.keys():
                str_index = string.find(num_str)
                if -1 < str_index < lowest_num_idx:
                    lowest_num_idx = str_index
                    low_char = f"{num_map[num_str]}"
            first_char = low_char if low_char else char
        except ValueError:
            continue

    rev_str = string[::-1]
    for idx, char in enumerate(rev_str):
        try:
            int(char)
            highest_num_idx = len(string) - idx - 1
            for num_str in num_map.keys():
                str_index = string.find(num_str)
                if str_index > highest_num_idx:
                    highest_num_idx = str_index
                    high_char = f"{num_map[num_str]}"

            last_char = high_char if high_char else char
        except ValueError:
            continue
    return int(f"{first_char}{last_char}")


def sum_number_strings_in_inputs():
    with open("input.txt", "r") as f:
        inputs = f.readlines()
    print(sum([main(i) for i in inputs]))


if __name__ == "__main__":
    sum_number_strings_in_inputs()