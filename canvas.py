from config import (
    HORIZONTAL_BORDER,
    VERTICAL_BORDER
)


class Canvas:

    AVAILABLE_INSTRUCTIONS = {
        'Line': 1,
        'Rectangle': 2,

    }

    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

        line = [] * (width + 2)
        self.field = line * (heigth + 2)

        self.initialize_borders()

    def initialize_borders(self):
        for i in range(0, self.width + 2):
            self.field[0][i] = HORIZONTAL_BORDER
            self.field[self.heigth + 1][i] = HORIZONTAL_BORDER

        for i in range(0, self.heigth + 2):
            self.field[i][0] = VERTICAL_BORDER
            self.field[i[self.width + 1]] = VERTICAL_BORDER

    def print(self):
        for line in self.field:
            for ch in line:
                print(ch, end=' ')
            print()

    def apply_instruction(self, instruction):
        self.AVAILABLE_INSTRUCTIONS.get(instruction, lambda : 1)()
