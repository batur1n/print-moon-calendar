import yattag
from yattag import Doc
import calendar
from moon import MoonPhase
from datetime import datetime, timedelta
from math import ceil
import os
from translations import Russian

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
        # prints moon calendar as HTML table 
        doc, tag, text = Doc().tagtext()
        date = datetime.now() + timedelta(days=7)
        
        r = Russian()  # used for Russian translation, remove translate() calls if not needed
        
        cal = [['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']]
        cal.extend(calendar.monthcalendar(date.year,date.month))

        doc.asis('<!DOCTYPE html>')
        doc.asis('<link rel="stylesheet" href="src/styles.css">')

        with tag('html'):   #  style="height:210mm;width:297mm;"  # fit to A4 paper size ?
            with tag('body'):     
                with tag('h2'):
                    text(r.traslate(calendar.month_name[date.month]) + ' ' + str(date.year))
                # create a calendar table
                with tag("table", border="1"):
                    for list_one in cal:
                        with tag("tr"):
                            for elem in list_one:
                                with tag("td"):
                                    with tag("th", style="padding:5px;"):
                                        # inside a single table cell, i.e. a calendar day
                                        if elem != 0 and isinstance(elem, int):
                                            # get moon data for current day    
                                            m = MoonPhase(datetime.strptime(str(date.year) + '-' + str(date.month) 
                                            + '-' + str(elem) + '-00:00', '%Y-%m-%d-%H:%M'))

                                            # set background for new and full moon
                                            if m.zodiac_sign['moon_phase'] in ['new', 'full'] and m.zodiac_sign['phase_time'] != '':
                                                doc.attr(style="background-color: #e3e3e3;")

                                            # information about current day in text form
                                            with tag("p", style="font-size:50px;text-align:center;"):
                                                text(str(elem))
                                            with tag("p", style="text-align:center;"):
                                                text(str(ceil(m.age)) + ' ' + r.traslate('moon day') + ', ' + r.traslate(m.zodiac_sign['zodiac_sign']))

                                            # images for zodiac and moon phase for current day
                                            pic_size = "75"

                                            doc.stag('img', src=self.get_picture_path(m.phase_text, ceil(m.illuminated*100)), 
                                            height=pic_size, width=pic_size, align='left')                                   
                                            doc.stag('img', src=self.get_picture_path(m.zodiac_sign['zodiac_sign'], None), 
                                            height=pic_size, width=pic_size, align='right')

                                            # captions for zodiac and moon phase transitions
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

                                        # days of the week                        
                                        elif isinstance(elem, str):
                                            text(r.traslate(elem))
                                        elif elem == 0:
                                            pass

        # write HTML                                        
        f = open('moon_calendar_{}_{}.html'.format(date.month, date.year), 'w')
        f.write(yattag.indent(doc.getvalue(), indent_text=True)) 
        print('Successfully generated calendar: {}'.format(f.name))
        f.close()

if __name__ == '__main__':
    m = Moon_HTML_Printer()
    m.print_html()