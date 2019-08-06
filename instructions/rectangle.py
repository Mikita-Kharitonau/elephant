from instructions import Instruction
from config import RECTANGLE_DEFAULT_CHARACTER


class Rectangle(Instruction):
    def __init__(self, x1, y1, x2, y2, filling_character=RECTANGLE_DEFAULT_CHARACTER):
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
        if not numbers[0] < numbers[2] or not numbers[1] < numbers[3]:
            raise ValueError
        return Rectangle(numbers[0], numbers[1], numbers[2], numbers[3])

    def __str__(self):
        return "Rectangle({}, {}, {}, {})".format(self.x1, self.y1, self.x2, self.y2)
