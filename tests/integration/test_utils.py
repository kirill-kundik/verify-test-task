import pathlib
from unittest.mock import mock_open, patch

import requests

import app.utils


def test_download_file(timeout, true_url, not_found_url, timeout_url, incorrect_url):
    url = incorrect_url  # url is not exists
    resp = app.utils.download_file(url, timeout)
    assert resp is None

    url = timeout_url  # url timeout
    resp = app.utils.download_file(url, timeout)
    assert resp is None

    url = not_found_url  # not found
    resp = app.utils.download_file(url, timeout)
    assert resp is None

    url = true_url

    r = requests.get(url, timeout=timeout)

    resp = app.utils.download_file(url, timeout)
    assert resp == r.content


def test_store_file(timeout, true_url):
    url = true_url

    r = requests.get(url, timeout=timeout)

    open_mock = mock_open()
    with patch("app.utils.open", open_mock, create=True):
        app.utils.store_file(r.content, pathlib.Path('output.img'))

    open_mock.assert_called_with("output.img", "wb")
    open_mock.return_value.write.assert_called_once_with(r.content)
