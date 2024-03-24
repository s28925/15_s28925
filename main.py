import math

# Task 1: List Comprehensions

squared_numbers = [n * n for n in range(1, 11)]
print(squared_numbers)

# Task 2: Functions


def e_squares(start, end):
    result = [n * n for n in range(start, end)]
    return result


print(e_squares(1, 11))

# Task 3: Classes


class SquareGenerator:
    def generate_squares(self, start, end):
        result = [n * n for n in range(start, end)]
        return result


square_generator_result = SquareGenerator().generate_squares(1, 11)
print(square_generator_result)

# Task 4: Libraries

sqrt_list = [math.sqrt(n) for n in square_generator_result]
print(sqrt_list)
