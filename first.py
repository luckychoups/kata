f = ''

print('ajaja')


def divide(weight: int):
    assert isinstance(weight, int)
    return weight >= 4 and weight % 2 == 0


assert divide(5) == False