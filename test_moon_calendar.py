import pytest
import moon, generate_html
import os
from datetime import datetime
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    """test for December 2019"""
    date = datetime.strptime('2019-12-12', '%Y-%m-%d')
    m_test = generate_html.Moon_HTML_Printer()
    m_test.print_html()
    request.cls.filename = os.getcwd() + '\\' + 'moon_calendar_{}_{}.html'.format(date.month, date.year)
    request.cls.driver = webdriver.Firefox()
    request.cls.driver.get('file:///{}'.format(request.cls.filename))
    request.cls.table = request.cls.driver.find_element_by_xpath('/html/body/table')
    yield
    request.cls.driver.close()
    os.remove(request.cls.filename)

@pytest.mark.usefixtures("setup")
class Test_suite:

    def test_01_check_if_file_exists(self):
        """check if generated HTML file exists"""     
        assert os.path.isfile(self.filename)

    def test_02_check_table_rows(self, setup):
        """check that there are 7 rows in the calendar"""
        assert 7 == len(list(x for x in self.table.find_elements_by_tag_name("tr")))

    def test_03_check_table_columns(self, setup):
        """check that there are 7 rows in the calendar"""
        assert 7 == len(list(x for x in self.table.find_elements_by_tag_name("td")))//7

    def test_04_check_images_in_table(self, setup):
        """check that there are 31*2 images in a table (for each day of the month)"""
        assert 62 == len(list(x for x in self.table.find_elements_by_tag_name("img")))