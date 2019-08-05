class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @staticmethod
    def validate(args):
        if len(args) < 2:
            raise ValueError
        numbers = []
        for i in range(0, 2):
            numbers.append(int(args[i]))
        return Canvas(numbers[0], numbers[1])