import datetime
import calendar

def Easter(y):
    """
    >>> print(Easter(2017))
    2017-04-16
    >>> print(Easter(823))
    0823-04-09
    """

    a = y % 19
    b = y // 100
    c = y % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32

    return [y,n,p]

def format_short(date):
    string = str(date[2])+"/"+str(date[1])+"/"+str(date[0])
    return string

def format_full(date):
    if str(date[2])[-1] == "1":
        superscript = "st"
    elif str(date[2])[-1] == "2":
        superscript = "nd"
    elif str(date[2])[-1] == "3":
        superscript = "rd"
    else:
        superscript = "th"

    superscript = "<sup>"+superscript+"</sup>"
    day = str(date[2])+superscript
    month = calendar.month_name[date[1]]

    return "The "+day+" of "+month+", "+str(date[0])
