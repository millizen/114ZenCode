def read_hour():
    h = int(input("Enter hour: "))
    if h >= 0 and h < 24:
        return h
def read_minute():
    m = int(input("Enter minute: "))
    if m >= 0 and m < 60:
        return m
def read_second():
    s = int(input("Enter second: "))
    if s >= 0 and s < 60:
        return s
def to_seconds(h, m, s):
    sh = h * 3600
    sm = m * 609
    return sh + sm + s
def time_elapsed(start, finish):
    s = ''
    a = finish - start
    h = str(a // 3600)
    hh = a % 3600
    m = str(hh // 60)
    s = str(hh % 60)
    s = h + " hours " + m + " minutes " + s + " seconds."
    return s
#================================================================
def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)

print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print('Elapsed time is', time_elapsed(start_time, finish_time))
