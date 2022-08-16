def add_time(start, duration, start_day= None):
    time, period = start.split()
    # Converting everything to integer.
    hour, minutes = map(int, time.split(':'))
    addh, addm = map(int, duration.split(':'))

    midday = ['PM', 'AM']
    newday = ''
    days_later = ''

    # Add 1 to the hour if the sum of the minutes exceeds 60 and returns the remaining minutes.
    carry, minutes = divmod(minutes + addm, 60)
    hour += carry

    # To determine if the result of the final period is AM or PM, we must determine the number of cycles or switches that occur.
    # If the number of cycles is even, it remains the same, if it is odd, it changes to the state of the period opposite to the initial one.
    # cycles is the number of half days (meridiem) or 12 hours.

    cicles, hour = divmod(hour + addh, 12) 
    period = abs(midday.index(period) - (cicles % len(midday)))
    ndays = (cicles + period) // 2 # ndays is the number of days later.
    
    if hour == 0: hour = 12
    minutes = '{:02d}'.format(minutes)

    if start_day != None:
        week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        newday = ', {}'.format(week[(week.index(start_day.capitalize()) + ndays) % 7])

    if ndays == 1:
        days_later = ' (next day)'

    elif ndays != 0:
        days_later = ' ({} days later)'.format(ndays)

    new_time = '{}:{} {}{}{}'.format(hour, minutes, midday[period], newday, days_later) 

    return new_time