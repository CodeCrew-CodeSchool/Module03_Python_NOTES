def is_leap(year):
    leap = False

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        leap = True
    else:
        leap = False
    # if year % 4 == 0:
    #     leap = True
    #     if year % 100 == 0:
    #         leap = False
    #         if year % 400 == 0:
    #             leap = True

    return leap

year = 2020
print(is_leap(year))