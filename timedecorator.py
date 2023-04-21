



def timeDecorator(time_date):

    if time_date < 60:
        return time_date

    seconds = time_date % 60
    temp_time = time_date - seconds
    temp_time = temp_time / 60

    minutes = temp_time % 60
    temp_time = temp_time - minutes
    temp_time = temp_time / 60

    hours = temp_time % 24
    temp_time = temp_time - hours
    days = temp_time / 24

    return (days, hours, minutes, seconds)

time_date = 1727700

print(timeDecorator(time_date))
