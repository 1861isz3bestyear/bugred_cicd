import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    options.binary_location = '/usr/bin/chromium-browser'  # Alpine-specific path
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Alpine-specific fixes
    options.add_argument('--disable-software-rasterizer')
    options.add_argument('--disable-dev-shm-usage')


    service = Service(executable_path='/usr/bin/chromedriver')

    driver = webdriver.Chrome(service=service, options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()
