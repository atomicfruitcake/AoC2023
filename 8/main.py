from dataclasses import dataclass
from functools import cached_property
from typing import List, Dict
from itertools import cycle


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

    def main(self):
        elem = "AAA"
        node = self.map[elem]
        steps = 0
        for instruction in cycle(self.instructions):
            steps += 1
            print(instruction)
            elem = node[instruction]
            if elem == "ZZZ":
                break
            node = self.map[elem]
            print(node)
        print(steps)

def main():
    ms = MapSolver()
    ms.main()


if __name__ == "__main__":
    main()