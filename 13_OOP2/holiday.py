import holidays

def academic_day(day):
    pl_holiday = holidays.POL()

    return day not in pl_holiday


print(academic_day(2022-12-24))