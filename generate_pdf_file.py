from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.graphics.shapes import Drawing
from reportlab.lib.styles import ParagraphStyle

import calendar

doc = SimpleDocTemplate('calendar.pdf', pagesize=landscape(A4))

cal = [['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']]
cal.extend(calendar.monthcalendar(2011,9))

print(cal)


table = Table(cal, 7*[inch], len(cal) * [inch])

table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'Helvetica'),
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.green),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))

style = ParagraphStyle(
        name='Normal',
        fontName='Helvetica',
        fontSize=8,
    )

title = """Title goes here"""
p = Paragraph(title, style)

#create the pdf with this
doc.build([table])