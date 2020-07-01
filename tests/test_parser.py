import os
import yaml
import requests

from selenium.common.exceptions import NoSuchElementException

from main import authorization, parse_info, write_results
from configuration import get_intranet_configuration

try:
    from collections.abc import Callable
except ImportError:
    from collections import Callable


def test_parse_info(browser):

    try:

        email, password, url = get_intranet_configuration()

        response = requests.get(url)
        response.raise_for_status()

        authorization(browser, email, password)

        names_list, jobs_list, emails_list = parse_info(browser)
        assert len(names_list) == len(jobs_list) == len(emails_list)

        try:
            os.stat('results')
        except FileNotFoundError:
            os.mkdir('results')

        write_results(names_list, jobs_list, emails_list)

    except yaml.YAMLError as err:
        assert False, print(err)

    except NoSuchElementException as err:
        assert False, print(err)

    except requests.exceptions.ConnectionError:
        assert False, print(f'\nConnectionError occured')

    except requests.exceptions.HTTPError as err:
        response = f'\nHTTP Error occured.' \
                   f'\nResponse is: {err.response.content}.' \
                   f'\nStatus code: {err.response.status_code}.'
        assert False, print(response)

    finally:
        browser.quit()
