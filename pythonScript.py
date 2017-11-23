#!/usr/bin/python3
import cgi, cgitb
import ImportantDates
cgitb.enable()
form = cgi.FieldStorage()
year = form.getvalue('Year')
formatting = form.getvalue('format')
date = ImportantDates.Easter(int(year))


print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<html>')
print('<head> <title> The date of Easter in {} </title>  </head>'.format(year))
print('<body>')

print('<p>')
print('In the year {}, Easter starts on the date;'.format(year))
print('</p>')

if formatting == "short" or formatting == "both":
    print('<p>')
    print("{}".format(ImportantDates.format_short(date)))
    print('</p>')

if formatting == "full" or formatting == "both":
    print('<p>')
    print("{}".format(ImportantDates.format_full(date)))
    print('</p>')

print('</body>')
print('</html>')
