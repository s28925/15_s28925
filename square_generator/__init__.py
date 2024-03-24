# Task 6: Modules
# Task 7: Packages

class SquareGenerator:
    def generate_squares(self, start, end):

        # Task 5: Exceptions
        if start > end:
            print("The start of the range cannot be higher than the end of the range")
            return None

        result = [n * n for n in range(start, end)]
        return result

# Task 8: Inheritance


class CubicGenerator(SquareGenerator):
    def generate_cubes(self, start, end):
        if start > end:
            print("The start of the range cannot be higher than the end of the range")
            return None

        result = [n ** 3 for n in range(start, end)]
        return result
