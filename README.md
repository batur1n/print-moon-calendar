Works with Python 3.8

Dependencies:
pip install datetime yattag dateutil

For tests:
pip install pytest selenium

Usage:
python generate_html.py

Generates an HTML document in the same folder - a moon calendar for current month (data comes from moon.py which I modified slightly)

Calendar contains moon (lunar) days, moon phases and zodiac signs as well as times of their transitions for each day of the month. Timezone is hardcoded to UTC +02:00, language is English.

moon.py by [@keturn]( https://keturn.net/ ) (modified)

Icons by:
https://www.flaticon.com/authors/bqlqn
https://www.flaticon.com/authors/freepik
