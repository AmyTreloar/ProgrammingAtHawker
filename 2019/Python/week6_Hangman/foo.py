from datetime import date

def dodgy_days_alive(dob):
    day = int(dob[0])
    month = int(dob[1])
    year = int(dob[2])

    years_alive = curr_year - year
    max_days_alive = years_alive * days_in_year
    days_not_alive = days_in_year / 12 * month + day
    return max_days_alive - days_not_alive

def days_alive(dob):
    d = int(dob[0])
    m = int(dob[1])
    y = int(dob[2])
    today = date.today()
    dob = date(year=y, month=m, day=d)
    return today - dob


curr_year = 2019
days_in_year = 365
dob = "16/06/2001"
dob = dob.split('/')
print(dodgy_days_alive(dob))
print(days_alive(dob))

