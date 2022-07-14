# > function should be declared before usage in a file
def build_decades(decades):
    if decades == 0:
        d = ''
    else:
        d = f'{decades} decades'
    return d


def build_years(decades, residual):
    if residual == 0:
        y = ''
    else:
        if decades == 0:
            y = f' {residual} years'
            print(f'debug when less than 10 years, y = {y}')
        else:
            y = f' and {residual} years'
    return y


# How many decades
while True:
    ageS = input('your age ?\n')
    age = int(ageS)

    dec = age // 10
    d = build_decades(dec)
    y = build_years(dec, age % 10)

    print(f'your age is {age}, that goes to {d} {y} ')
