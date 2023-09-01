
# Lab07_01
"""
def corner_frame(n):
    lines = map(lambda i: ' '.join(map(lambda j: str(j) if j == i else str(i), range(1, n+1))), range(1, n+1))
    return '\n'.join(lines)

# Example usage
n = 4
output = corner_frame(n)
print(output)
"""

# Lab07_02
# 3 = 1 2 3 
#     8 _ 4
#     7 6 5

# 4 = 01 02 03 04
#     12       05
#     11       06
#     10 09 08 07

# def square_frame(n, sep=' '):
#     # Create the initial square list
#     square = [list(range(1, n + 1))]
#     for i in range(1, n - 1):
#         square.append([0] * n)
#     square.append(list(range(2*n - 1, n, -1)))

#     # Convert the numbers to strings
#     square = list(map(lambda row: list(map(str, row)), square))

#     # Find the maximum number of digits in the square
#     max_digits = len(str(2*n - 1))

#     # Format each number with zero-padding
#     square = list(map(lambda row: list(map(lambda num: num.zfill(max_digits), row)), square))

#     # Join the numbers with the separator (sep)
#     square = list(map(lambda row: sep.join(row), square))

#     # Print the square
#     for row in square:
#         print(row)

# # Example call:
# square_frame(3)

def square_frame(n, sep=' '):
    if n < 1:
        raise ValueError("Size 'n' must be greater than or equal to 1.")

    frame = [[0] * n for _ in range(n)]

    # Define the directions for each movement (right, down, left, up)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    num = 1
    x, y = 0, 0
    direction_index = 0

    while num <= n * n:
        frame[x][y] = num
        num += 1

        next_x, next_y = x + directions[direction_index][0], y + directions[direction_index][1]

        # Check if the next position is outside the frame or already filled
        if not (0 <= next_x < n and 0 <= next_y < n) or frame[next_x][next_y] != 0:
            direction_index = (direction_index + 1) % 4

        x, y = x + directions[direction_index][0], y + directions[direction_index][1]

    row_strings = map(lambda row: sep.join(f"{num:02}" for num in row), frame)
    frame_str = '\n'.join(row_strings)
    return frame_str

# Example: Using the custom separator '.'
result = square_frame(4, '.')
print(result)
