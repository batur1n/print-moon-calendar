import yattag
from yattag import Doc
import calendar
from moon import MoonPhase
from datetime import datetime, timedelta
from math import ceil
import os

class Moon_HTML_Printer():

    def get_picture_path(self, input_string, illum):
        # get icons of moon phases
        if input_string == 'new':
            return os.getcwd() + '\\src\\' + 'new.png'
        elif input_string == 'full':
            return os.getcwd() + '\\src\\' + 'full.png'
        elif input_string == 'first quarter':
            return os.getcwd() + '\\src\\' + 'first_quarter.png'
        elif input_string == 'last quarter':
            return os.getcwd() + '\\src\\' + 'last_quarter.png'
        elif input_string and illum:
            # find closest value of current moon illumination in picture representation
            approx = min([x*5 for x in range(1,20)] , key=lambda y:abs(y-illum)) 
            prefix = input_string.replace(' ', '_').lower()
            return os.getcwd() + '\\src\\{}\\'.format(prefix) + str(approx) + '.png'
        # get icons of zodiac signs
        elif input_string and not illum: 
            return os.getcwd() + '\\src\\' + input_string.lower() + '.png'

    def print_html(self):

        doc, tag, text = Doc().tagtext()
        date = datetime.now() + timedelta(days=120)
        
        cal = [['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']]
        cal.extend(calendar.monthcalendar(date.year,date.month))

        doc.asis('<!DOCTYPE html>')
        doc.asis('<link rel="stylesheet" href="src/styles.css">')

        with tag('html'):
            with tag('body'):
                with tag('h2'):
                    text(calendar.month_name[date.month] + ' 2019')
                with tag("table", border="1"):
                    for list_one in cal:
                        with tag("tr"):
                            for elem in list_one:
                                with tag("td"):
                                    with tag("th"):
                                        if elem != 0 and isinstance(elem, int):
                                            m = MoonPhase(datetime.strptime(str(date.year) + '-' + str(date.month) 
                                            + '-' + str(elem) + '-00:00', '%Y-%m-%d-%H:%M'))

                                            with tag("p", style="font-size:50px;text-align:center;"):
                                                text(str(elem))
                                            with tag("p", style="text-align:center;"):
                                                text(str(ceil(m.age)) + ' moon day, ' + m.zodiac_sign['zodiac_sign'])

                                            doc.stag('img', src=self.get_picture_path(m.phase_text, ceil(m.illuminated*100)), 
                                            height="75", width="75", align='left')                                   
                                            doc.stag('img', src=self.get_picture_path(m.zodiac_sign['zodiac_sign'], None), 
                                            height="75", width="75", align='right')

                                            with tag('div'):
                                                if m.zodiac_sign['moon_phase'] in ['new', 'full'] and m.zodiac_sign['phase_time'] != '':
                                                    with tag('p', style="float:left;margin-left:20px;"):   
                                                        text(m.zodiac_sign['phase_time'][11:-3])
                                                if m.zodiac_sign['zodiac_time'][11:-3] not in ['10:00', '00:00']:
                                                    with tag('p', style="float:right;margin-right:20px;"):
                                                        text(m.zodiac_sign['zodiac_time'][11:-3])
                                                if m.zodiac_sign['phase_time'] == '' and m.zodiac_sign['zodiac_time'][11:-3] in ['10:00', '00:00']:
                                                    with tag('div', style="height:100px;"):
                                                        pass

                                        elif isinstance(elem, str):
                                            text(elem)
                                        elif elem == 0:
                                            pass

        f = open('moon_calendar_{}_{}.html'.format(date.month, date.year), 'w')
        f.write(yattag.indent(doc.getvalue(), indent_text=True)) 
        print('Successfully generated calendar: {}'.format(f.name))
        f.close()

if __name__ == '__main__':
    m = Moon_HTML_Printer()
    m.print_html()