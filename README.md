# Windows instructions:

0. Install latest Google Chrome (or any browser with HTML5/CSS3 support)
1. Download generate_html.zip
2. Unzip generate_html.zip
3. Run generate_html.exe
4. Open generated .html file in the same folder (starts with 'moon_calendar..') with browser

# CLI/advanced user's instructions:

0. Install Python 3.8 and latest Google Chrome (or any browser with HTML5/CSS3 support)
1. Install dependencies: pip install datetime yattag dateutil
2. (Optional) Install test dependencies: pip install pytest selenium
3. (Optional) Run tests: pytest -v test_moon_calendar.py
4. Run: python generate_html.py
5. Open generated .html file in the same folder (starts with 'moon_calendar..') with browser

# Description:

Generates an HTML document in the same folder - a moon calendar for current month (data comes from moon.py which I modified slightly)

Calendar contains moon (lunar) days, moon phases and zodiac signs as well as times of their transitions for each day of the month. Timezone is hardcoded to UTC +02:00, language is __Russian__ (can be changed back to English in generate_html.py code).

# Acknowledgements

moon.py by [@keturn]( https://keturn.net/ ) (modified)

Icons by:

https://www.flaticon.com/authors/bqlqn

https://www.flaticon.com/authors/freepik
