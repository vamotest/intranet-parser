import os
import pytest

from fixtures.browser import Browser
from configuration import get_intranet_configuration


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="This is request browser",
        required=False
    )


@pytest.fixture(scope="session")
def browser(request):
    intranet_url = get_intranet_configuration()[2]
    browser = request.config.getoption("--browser")
    fixture = Browser(url=intranet_url, browser=browser)
    yield fixture
    fixture.quit()


def _pytest_configure_(config):
    config.metadata['os'] = os.name
    config.metadata['PATH'] = os.environ['PATH']
    config.metadata['pwd'] = os.getcwd()
