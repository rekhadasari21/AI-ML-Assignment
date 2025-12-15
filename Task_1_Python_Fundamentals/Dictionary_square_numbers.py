# Dictionary with number and its square
def square_dictionary(numbers):
    squares={}
    for num in numbers:
        squares[num] = num*num
    return squares
