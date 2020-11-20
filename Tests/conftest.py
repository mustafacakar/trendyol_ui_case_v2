import pytest
from selenium import webdriver


#@pytest.fixture(params=["chrome","firefox"],scope='class') -> chromedriver error.
@pytest.fixture(params=["firefox"],scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.close()


    ## run commands.

    ## pytest Tests/test_HomePage.py -v --html=./trendyol.html
    ## pytest Tests/test_HomePage.py -v -n 3 --html=./trendyol.html -> paralel execution