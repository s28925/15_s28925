# Task 6: Modules
# Task 7: Packages

from typing import override
from abc import ABC, abstractmethod

# Task 10: Abstract Elements


class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, start, end):
        return


# Task 8: Inheritance


class CubicGenerator(SquareGenerator):

    # Task 9: Function Overriding
    @override
    def generate_squares(self, start, end):
        if start < end:
            result = [n * n for n in range(start, end)]
            return result
        else:
            raise ValueError("The start of the range cannot be higher than the end")

    def generate_cubes(self, start, end):
        if start > end:
            print("The start of the range cannot be higher than the end of the range")
            return None

        result = [n ** 3 for n in range(start, end)]
        return result
