# Task 1: List Comprehensions

squared_numbers = [n * n for n in range(1, 11)]
print(squared_numbers)

# Task 2: Functions


def e_squares(start, end):
    result = [n * n for n in range(start, end)]
    return result


print(e_squares(1, 11))
