import sys


# > function should be declared before usage in a file
def build_decades(decades):
    d = ''
    if decades != 0:
        d = f'{decades} decades'
    return d


def build_years(decades, residual):
    if residual == 0:
        y = ''
    elif decades == 0:
        y = f' {residual} years'
    else:
        y = f' and {residual} years'
    return y


# How many decades
loop = 0
while loop < 3:
    age_str = input('your age ?\n')
    try:
        age = int(age_str)
    except ValueError:
        print("! Age should be an integer")
        sys.exit("Error")

    dec = age // 10
    d = build_decades(dec)
    y = build_years(dec, age % 10)

    print(f'your age is {age}, that goes to {d} {y} ')
    loop += 1

print("end of program")
