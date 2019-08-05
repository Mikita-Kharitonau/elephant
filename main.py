from config import (
    INSTRUCTION_VALIDATION_ERROR
)
from instructions import (
    Canvas as CanvasInstruction,
    Line,
    Rectangle,
    BucketFill
)

AVAILABLE_INSTRUCTIONS = {
    'C': lambda args: CanvasInstruction.validate(args),
    'L': lambda args: Line.validate(args),
    'R': lambda args: Rectangle.validate(args),
    'B': lambda args: BucketFill.validate(args)
}


def read_instructions_from_file(path):
    instructions = []
    with open(path, 'r') as f:
        for line in f:
            instructions.append(line.split())
    validated_instructions = validate_instructions(instructions)
    return validated_instructions


def validate_instructions(instructions):
    validated_instructions = []
    for instruction in instructions:
        try:
            if len(instruction) == 0:
                raise ValueError
            validated_instructions.append(
                AVAILABLE_INSTRUCTIONS.get(
                    instruction[0],
                    raise_(ValueError)
                )(instruction[1:])
            )
        except ValueError:
            print(INSTRUCTION_VALIDATION_ERROR.format(instruction))
    return validated_instructions


def raise_(e):
    def r():
        raise e
    return r


def main():
    instructions = read_instructions_from_file('input.txt')
    print(instructions)


if __name__ == '__main__':
    main()
