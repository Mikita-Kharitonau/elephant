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
            number = int(args[i])
            if not number > 0:
                raise ValueError
            numbers.append(number)
        return Canvas(numbers[0], numbers[1])

    def __str__(self):
        return "CanvasInstruction({}, {})".format(self.width, self.height)
