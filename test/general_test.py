import os
import glob
import unittest
import filecmp

from main import elephant


class GeneralTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        elephant('test/inputs/input.txt', 'test/outputs/actual/output.txt')
        elephant('test/inputs/input2.txt', 'test/outputs/actual/output2.txt')
        elephant('test/inputs/input3.txt', 'test/outputs/actual/output3.txt')

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     outputs = glob.glob('test/outputs/actual/*.txt')
    #     for output in outputs:
    #         os.remove(output)

    def test_app(self):
        self.assertTrue(
            filecmp.cmp(
                'test/outputs/actual/output.txt',
                'test/outputs/expected/expected.txt'
            )
        )

    def test_app_2(self):
        self.assertTrue(
            filecmp.cmp(
                'test/outputs/actual/output2.txt',
                'test/outputs/expected/expected2.txt'
            )
        )

    def test_app_3(self):
        self.assertTrue(
            filecmp.cmp(
                'test/outputs/actual/output3.txt',
                'test/outputs/expected/expected3.txt'
            )
        )
