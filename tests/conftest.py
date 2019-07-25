import pytest


@pytest.fixture()
def timeout():
    return 5


@pytest.fixture()
def true_url():
    return "http://files.smashingmagazine.com/wallpapers/apr-19/inspiring-blossom/cal/apr-19-inspiring-blossom-cal" \
           "-1680x1200.jpg"


@pytest.fixture()
def not_found_url():
    return "http://files.smashingmagazine.com/wallpapers/apr-19/inspiring-blossom/cal/apr-19-insping-blossom-cal" \
           "-1680x1200.jpg"


@pytest.fixture()
def timeout_url():
    return "https://httpstat.us/200?sleep=500000"


@pytest.fixture()
def incorrect_url():
    return "https://gooooooogllll.com/"
