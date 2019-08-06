import argparse

from canvas import Canvas
from config import (
    INSTRUCTION_VALIDATION_ERROR,
    CANVAS_HAS_NOT_BEEN_CREATED,
    FILE_NOT_EXISTS
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
    try:
        with open(path, 'r') as f:
            for line in f:
                instructions.append(line.split())
    except FileNotFoundError:
        print(FILE_NOT_EXISTS.format(path))
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
    def r(arg):
        raise e
    return r


def elephant(input_path, output_path):
    instructions = read_instructions_from_file(input_path)
    canvas = None
    for instruction in instructions:
        if type(instruction) == CanvasInstruction and canvas is None:
            canvas = Canvas(instruction.width, instruction.height)
            canvas.write_to_file(output_path)
            continue
        if canvas is None:
            print(CANVAS_HAS_NOT_BEEN_CREATED.format(instruction))
            continue
        try:
            canvas.apply_instruction(instruction)
        except Exception as e:
            print(str(e))
            continue
        canvas.write_to_file(output_path)


def main():
    parser = argparse.ArgumentParser(description='Elephant application.')
    parser.add_argument('input', help='Path to input file.')
    parser.add_argument('output', help='Path to output file.')
    args = parser.parse_args()
    elephant(args.input, args.output)


if __name__ == '__main__':
    main()
