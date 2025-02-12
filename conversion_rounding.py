def round_ans(val):
    """
    rounds temperatures to nearest degree
    :param val: Number to be rounded
    :return: Number rounded to nearest degree
    """
    var_rounded = (val *2 +1) // 2
    return "{:.0f}".format(var_rounded)


def to_celsius(to_convert):
    """
    Converts from °F to °C
    :param to_convert: Temperature TO BE converted IN °F
    :return:
    """

def to_fahrenheit(to_convert):



    # main routine / testing starts here

to_c_test = [0, 100, -459]
to_f_test = [0, 100, 40, -273]

for item in to_f_test:
    ans = to_fahrenheit(item)
    print(f"{item} C is {ans} F")

print()

for item in to_c_test:
    ans = to_celsius(item)
    print(f"{item} F is {ans} C")