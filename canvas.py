from config import (
    HORIZONTAL_BORDER,
    VERTICAL_BORDER,
    CANT_PRINT_LINE,
    CANVAS_DEFAULT_CHARACTER
)
from instructions import (
    Line,
    Rectangle,
    BucketFill
)


class Canvas:

    def __init__(self, width, height):

        self.AVAILABLE_INSTRUCTIONS = {
            Line: lambda l: self.print_line(l),
            Rectangle: lambda r: self.print_rectangle(r),
            BucketFill: lambda b: self.print_bucket_fill(b),
        }

        self.width = width
        self.height = height

        self.field = [[CANVAS_DEFAULT_CHARACTER] * (width + 2)
                      for i in range(0, height + 2)]

        self.initialize_borders()

    def initialize_borders(self):
        for i in range(0, self.height + 2):
            self.field[i][0] = VERTICAL_BORDER
            self.field[i][self.width + 1] = VERTICAL_BORDER

        for i in range(0, self.width + 2):
            self.field[0][i] = HORIZONTAL_BORDER
            self.field[self.height + 1][i] = HORIZONTAL_BORDER

    def print(self):
        for line in self.field:
            for ch in line:
                print(ch, end='')
            print()

    def write_to_file(self, path):
        with open(path, 'a') as file:
            for line in self.field:
                for ch in line:
                    file.write(ch)
                file.write('\n')

    def apply_instruction(self, instruction):
        self.AVAILABLE_INSTRUCTIONS[type(instruction)](instruction)

    def print_line(self, line):
        if (line.x1 != line.x2 and line.y1 != line.y2) or \
                self.check_for_out_of_range(line.x1, line.y1) or \
                self.check_for_out_of_range(line.x2, line.y2):
            raise Exception(CANT_PRINT_LINE.format(line))
        if line.x1 == line.x2:
            for i in range(line.y1, line.y2 + 1):
                self.field[i][line.x1] = line.filling_character
        if line.y1 == line.y2:
            for i in range(line.x1, line.x2 + 1):
                self.field[line.y1][i] = line.filling_character

    def print_rectangle(self, rectangle):
        self.print_line(Line(rectangle.x1, rectangle.y1, rectangle.x2, rectangle.y1))
        self.print_line(Line(rectangle.x1, rectangle.y2, rectangle.x2, rectangle.y2))
        self.print_line(Line(rectangle.x1, rectangle.y1, rectangle.x1, rectangle.y2))
        self.print_line(Line(rectangle.x2, rectangle.y1, rectangle.x2, rectangle.y2))

    def print_bucket_fill(self, bucket_fill):
        if self.field[bucket_fill.y][bucket_fill.x] != CANVAS_DEFAULT_CHARACTER:
            return

        # Fill current point
        self.field[bucket_fill.y][bucket_fill.x] = bucket_fill.filling_character

        # left
        self.print_bucket_fill(
            BucketFill(
                bucket_fill.x - 1,
                bucket_fill.y,
                bucket_fill.filling_character
            )
        )
        # right
        self.print_bucket_fill(
            BucketFill(
                bucket_fill.x + 1,
                bucket_fill.y,
                bucket_fill.filling_character
            )
        )
        # up
        self.print_bucket_fill(
            BucketFill(
                bucket_fill.x,
                bucket_fill.y - 1,
                bucket_fill.filling_character
            )
        )
        # down
        self.print_bucket_fill(
            BucketFill(
                bucket_fill.x,
                bucket_fill.y + 1,
                bucket_fill.filling_character
            )
        )

    def check_for_out_of_range(self, x, y):
        if x < 1 or x > self.width + 1 or y < 1 or y > self.height + 1:
            return True
        return False
