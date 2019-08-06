from instructions import Instruction
from config import BUCKET_FILL_DEFAULT_CHARACTER


class BucketFill(Instruction):
    def __init__(self, x, y, filling_character=BUCKET_FILL_DEFAULT_CHARACTER):
        Instruction.__init__(self, filling_character)
        self.x = x
        self.y = y

    @staticmethod
    def validate(args):
        if len(args) < 3:
            raise ValueError
        numbers = []
        for i in range(0, 2):
            numbers.append(int(args[i]))
        return BucketFill(numbers[0], numbers[1], args[2])

    def __str__(self):
        return "BucketFill({}, {}, {})".format(self.x, self.y, self.filling_character)
