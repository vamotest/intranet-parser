from fixtures.browser import Browser
import os
import pytest
import yaml


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
    conf = yaml.safe_load(open('configuration.yml'))
    url = conf['base_url']
    browser = request.config.getoption("--browser")
    fixture = Browser(url=url, browser=browser)
    yield fixture
    fixture.quit()


def _pytest_configure_(config):
    config.metadata['os'] = os.name
    config.metadata['PATH'] = os.environ['PATH']
    config.metadata['pwd'] = os.getcwd()
