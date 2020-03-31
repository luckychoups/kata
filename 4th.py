def sum_of_minimums(numbers: list):
    summ = 0
    for row in numbers:
        item = row[0]
        for thing in row:
            if thing < item:
                item = thing
        summ = summ + item
    return summ


assert sum_of_minimums([
    [3, 8, 15, 1],
    [4, 7, 9, 2],
    [7, 8, 9, 6, 5],
]) == 8
print(sum_of_minimums([
    [3, 8, 15, 1],
    [4, 7, 9, 2],
    [7, 8, 9, 6, 5],
]))
print ('done')
