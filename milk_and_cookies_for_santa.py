import datetime

def time_for_milk_and_cookies(dt):
    if dt.month == 12 and dt.day == 24:
        return True
    else:
        return False

ll = input('what\'s data?\n').split('.')
ll.reverse()
print(time_for_milk_and_cookies(datetime.date(int(ll[0]), int(ll[1]), int(ll[2]))))