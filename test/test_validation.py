import unittest

from instructions import (
    Canvas,
    Line,
    Rectangle,
    BucketFill
)


class ValidationTest(unittest.TestCase):

    def test_line_instruction_validation(self):
        self.assertRaises(ValueError, Line.validate, ['a1', '1', '2', '3'])
        self.assertRaises(ValueError, Line.validate, ['1', '2', '3'])
        self.assertRaises(ValueError, Line.validate, ['01', '1fw', '2', '3'])
        self.assertRaises(ValueError, Line.validate, ['1', '1', '2', '3--'])
        self.assertRaises(ValueError, Line.validate, [])
        line = Line.validate(['1', '2', '3', '4', '5'])
        self.assertEqual(line.x1, 1)
        self.assertEqual(line.y1, 2)
        self.assertEqual(line.x2, 3)
        self.assertEqual(line.y2, 4)

    def test_rectangle_instruction_validation(self):
        self.assertRaises(ValueError, Rectangle.validate, ['a1', '1', '2', '3'])
        self.assertRaises(ValueError, Rectangle.validate, ['1', '2', '3'])
        self.assertRaises(ValueError, Rectangle.validate, ['01', '1fw', '2', '3'])
        self.assertRaises(ValueError, Rectangle.validate, ['1', '1', '2', '3--'])
        self.assertRaises(ValueError, Rectangle.validate, [])
        self.assertRaises(ValueError, Rectangle.validate, ['1', '5', '6', '4'])
        self.assertRaises(ValueError, Rectangle.validate, ['5', '5', '5', '5'])
        rectangle = Rectangle.validate(['1', '2', '3', '4', '5'])
        self.assertEqual(rectangle.x1, 1)
        self.assertEqual(rectangle.y1, 2)
        self.assertEqual(rectangle.x2, 3)
        self.assertEqual(rectangle.y2, 4)

    def test_bucket_fill_instruction_validation(self):
        self.assertRaises(ValueError, BucketFill.validate, ['*1', '2', '*'])
        self.assertRaises(ValueError, BucketFill.validate, ['1', '2dw', '3'])
        self.assertRaises(ValueError, BucketFill.validate, ['1', '1'])
        self.assertRaises(ValueError, Line.validate, [])
        bucket_fill = BucketFill.validate(['1', '2', '*'])
        self.assertEqual(bucket_fill.x, 1)
        self.assertEqual(bucket_fill.y, 2)
        self.assertEqual(bucket_fill.filling_character, '*')

    def test_canvas_instruction_validation(self):
        self.assertRaises(ValueError, Canvas.validate, ['*1', '2'])
        self.assertRaises(ValueError, Canvas.validate, ['1', '2dw'])
        self.assertRaises(ValueError, Canvas.validate, ['1'])
        self.assertRaises(ValueError, Canvas.validate, ['3', '0'])
        self.assertRaises(ValueError, Canvas.validate, [])
        canvas = Canvas.validate(['1', '2'])
        self.assertEqual(canvas.width, 1)
        self.assertEqual(canvas.height, 2)
