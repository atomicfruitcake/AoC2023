from dataclasses import dataclass
from typing import List


@dataclass
class Match:
    number: int
    min_index: int
    max_index: int
    line_no: int


symbols = [
    "£", "@", "*", "/", "$", "+", "-", "+", "&", "#", "%"
]

with open("input.txt", "r") as f:
    inputs: List = f.readlines()


def main():
    total = 0
    for line_no, line in enumerate(inputs):
        line_matches = find_number_matches_in_line(line=line, line_no=line_no)
        res = [match.number for match in line_matches if match_has_adjacent_symbol(match=match)]
        print(res)
        total = total + sum(res)
        print(sum(res))
    # 479290
    print(f"Total: {total}")


def match_has_adjacent_symbol(match: Match) -> bool:
    match_line = inputs[match.line_no]
    if match.number == 539:
        pass

    try:
        leading_char = match_line[match.min_index]
        if leading_char in symbols:
            return True
    except IndexError:
        pass
    try:
        trailing_char = match_line[match.max_index]
        if trailing_char in symbols:
            return True
    except IndexError:
        pass

    if match.line_no != 0:
        adjacent_str_above = inputs[match.line_no - 1][match.min_index: match.max_index + 1]
        print(adjacent_str_above)
        if len([e for e in symbols if e in adjacent_str_above]):
            return True

    if match.line_no != len(inputs) - 1:
        adjacent_str_below = inputs[match.line_no + 1][match.min_index: match.max_index + 1]
        print(adjacent_str_below)
        if len([e for e in symbols if e in adjacent_str_below]):
            return True
    return False

def find_number_matches_in_line(line: str, line_no: int) -> List[Match]:
    cur_num = ""
    matches = []
    for idx, char in enumerate(line):
        try:
            int(char)
            cur_num = cur_num + char
        except ValueError:
            if cur_num:
                matches.append(
                    Match(
                        number=int(cur_num),
                        min_index=idx - (len(cur_num) + 1),
                        max_index=idx,
                        line_no=line_no
                    )
                )
            cur_num = ""
            continue
    return matches


if __name__ == "__main__":
    # matchesfoo[3])
    main()