import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Chrome\\chromedriver_win32\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Chrome(executable_path="C:\\Drivers\\geckodriver-v0.30.0-win64\\geckodriver.exe")
    elif browser_name == "IE":
        driver = webdriver.Chrome(executable_path="C:\\Drivers\\IEDriverServer_x64_4.0.0\\IEDriverServer.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()