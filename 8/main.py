from functools import cached_property
from typing import List, Dict
from itertools import cycle
from math import lcm


class MapSolver:

    @cached_property
    def inputs(self) -> List:
        with open("input.txt", "r") as f:
            inputs = f.readlines()
        return inputs

    @cached_property
    def instructions(self):
        _i = [i for i in self.inputs[0]]
        del _i[-1]
        return _i

    @cached_property
    def map(self) -> Dict:
        out_dict = {}
        raw_input = self.inputs[2:]
        for row in raw_input:
            start, out = row.split(" = (")
            left_el, right_el = out.replace(")\n", "").split(", ")
            out_dict[start] = {
                "L": left_el,
                "R": right_el
            }
        return out_dict

    @cached_property
    def start_elems(self):
        return [k for k in self.map.keys() if k[-1] == "A"]

    def part1(self):
        elem = "AAA"
        node = self.map[elem]
        steps = 0
        for instruction in cycle(self.instructions):
            steps += 1
            elem = node[instruction]
            if elem == "ZZZ":
                break
            node = self.map[elem]
        return steps

    def part2_get_steps(self, start_elem: str) -> int:
        node = self.map[start_elem]
        steps = 0
        for instruction in cycle(self.instructions):
            steps += 1
            elem = node[instruction]
            if elem[-1] == "Z":
                break
            node = self.map[elem]
        return steps

    def part2(self):
        low_com_mul = 1
        for el in self.start_elems:
            low_com_mul = lcm(low_com_mul, self.part2_get_steps(start_elem=el))
        return low_com_mul


def main():
    ms = MapSolver()
    print(ms.part1())
    print(ms.part2())


if __name__ == "__main__":
    main()
