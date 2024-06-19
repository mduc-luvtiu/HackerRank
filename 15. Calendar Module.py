import calendar

if __name__ == "__main__":
    date = [int(i) for i in input().split()]
    day = calendar.weekday(date[2], date[0], date[1])
    days_week = list(calendar.day_name)
    print(days_week[day].upper())