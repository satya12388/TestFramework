import pytest
from selenium import webdriver

@pytest.fixture
def driver_setup(request):

    browser = request.config.getoption("--browser")

    if browser == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()

    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.close()

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action = "store",
        default = "edge"
    )


def pytest_metadata(metadata):
   metadata.clear()
   metadata["Project_Name"] = "Ecommerce Login"
   metadata["Tester_Name"] = "Satya Kota"
   metadata["Functionality"] = "Login"

def pytest_html_report_title(report):
    report.title = "Ecommerce Testing Stats"
