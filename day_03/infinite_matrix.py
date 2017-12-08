import math


def getMaximumMatrixSize(number):
    square = math.sqrt(number)
    if not square.is_integer():
        square = math.trunc(square)
        if square % 2 == 0:
            square += 1
        else:
            square += 2
    return square


def resolveInfiniteMatrix(number):
    square = getMaximumMatrixSize(number)
    middleNumber = (square - 1) / 2
    maxSpiralNumber = square * square
    steps = middleNumber
    interval = []
    if number >= maxSpiralNumber - (square - 1):
        for num in range(int(maxSpiralNumber - square + 1), int(maxSpiralNumber + 1)):
            interval.append(num)
        position = interval.index(number)
        steps += abs(middleNumber - position)
    elif number >= maxSpiralNumber - (square - 1) * 2:
        for num in range(int(maxSpiralNumber - square * 2 + 2), int(maxSpiralNumber + 1 - square)):
            interval.append(num)
        position = interval.index(number)
        steps += abs(middleNumber - position)
    elif number >= maxSpiralNumber - (square - 1) * 3:
        for num in range(int(maxSpiralNumber - square * 3 + 3), int(maxSpiralNumber + 1 - square * 2)):
            interval.append(num)
        position = interval.index(number)
        steps += abs(middleNumber - position)
    elif number >= maxSpiralNumber - (square - 1) * 4:
        for num in range(int(maxSpiralNumber - square * 4 + 4), int(maxSpiralNumber + 1 - square * 2)):
            interval.append(num)
        position = interval.index(number)
        steps += abs(middleNumber - position)

    return steps
