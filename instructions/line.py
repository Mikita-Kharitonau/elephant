from instructions import Instruction
from config import LINE_DEFAULT_CHARACTER


class Line(Instruction):
    def __init__(self, x1, y1, x2, y2, filling_character=LINE_DEFAULT_CHARACTER):
        Instruction.__init__(self, filling_character)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @staticmethod
    def validate(args):
        if len(args) < 4:
            raise ValueError
        numbers = []
        for i in range(0, 4):
            numbers.append(int(args[i]))
        return Line(numbers[0], numbers[1], numbers[2], numbers[3])

