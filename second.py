## tratata = 'mi vezem with us kota'


def two_oldest_ages(ages: list):
    first = 0
    for age in ages: # для каждого возраста в возрастах мы делаем:
        if first < age:
            first = age

    ages.remove(first)

    second = 0
    for age in ages:
        if second < age:
            second = age

    return [second, first]


assert two_oldest_ages([4, 23, 5, 56,2]) == [23, 56]
print(two_oldest_ages([4, 23, 5, 56,2]))
print('done')