import yattag
from yattag import Doc
import calendar
from moon import MoonPhase
from datetime import datetime
from math import ceil

doc, tag, text = Doc().tagtext()
date = datetime.now()

cal = [['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']]
cal.extend(calendar.monthcalendar(date.year,date.month))

doc.asis('<!DOCTYPE html>')
doc.asis('<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">')


with tag('html'):
    with tag('body'):
        text(calendar.month_name[date.month] + ' 2019')
        with tag("table", border="1"):
            for list_one in cal:
                with tag("tr"):
                    for elem in list_one:
                        with tag("td"):
                            with tag("th"):
                                if elem != 0 and isinstance(elem, int):
                                    m = MoonPhase(datetime.strptime('2019-12-{}'.format(str(elem)), '%Y-%m-%d'))
                                    with tag("p", style="font-size:50px;text-align:center;"):
                                        text(str(elem))
                                    with tag("p", style="text-align:center;"):
                                        text(str(ceil(m.age)) + ' moon day, ' + m.zodiac_sign)
                                    with tag("p"):
                                        text("Moon is in " + m.phase_text + ' (' + str(ceil(m.illuminated*100)) + '%)')
                                elif isinstance(elem, str):
                                    text(elem)
                                elif elem == 0:
                                    pass

print(doc.getvalue())

f = open('moon_calendar_{}_{}.html'.format(date.month, date.year), 'w')
f.write(yattag.indent(doc.getvalue(), indent_text=True)) 
f.close()