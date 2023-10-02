import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Ie()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


####### Pytest HTML Report ##########

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata = {
        "Tester": "Uyah",
        "Project Name": "non commerce practice",
    }


# It is hook for delete/Modify Environment info to HTML Report
# Use the pytest.hookimpl decorator to define the pytest_metadata hook
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)



