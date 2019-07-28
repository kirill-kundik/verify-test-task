from datetime import date

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


@pytest.fixture()
def start_time():
    return date.fromisoformat('2019-01-01')


@pytest.fixture()
def end_time():
    return date.fromisoformat('2019-07-01')


@pytest.fixture()
def bad_start_time():
    return date.fromisoformat('2020-01-01')


@pytest.fixture()
def bad_end_time():
    return date.fromisoformat('2020-02-01')


@pytest.fixture()
def bad_resolution():
    return '2561x1222'


@pytest.fixture()
def resolution():
    return '2560x1440'


@pytest.fixture()
def start_url():
    return 'https://www.smashingmagazine.com/category/wallpapers/'


@pytest.fixture()
def path():
    return '/Users/kyrylo_kundik/PycharmProjects/verify-test-task/images'


@pytest.fixture()
def correct_res():
    return [
        'http://files.smashingmagazine.com/wallpapers/june-19/summer-is-coming/cal/june-19-summer-is-coming-cal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/june-19/summer-is-coming/nocal/june-19-summer-is-coming-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/june-19/melting-away/cal/june-19-melting-away-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/june-19/melting-away/nocal/june-19-melting-away-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/june-19/its-bauhaus-year/cal/june-19-its-bauhaus-year-cal-2560x1440.jpeg',
        'http://files.smashingmagazine.com/wallpapers/june-19/its-bauhaus-year/nocal/june-19-its-bauhaus-year-nocal-2560x1440.jpeg',
        'http://files.smashingmagazine.com/wallpapers/june-19/midsummer-junes-dream/cal/june-19-midsummer-junes-dream-cal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/june-19/midsummer-junes-dream/nocal/june-19-midsummer-junes-dream-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/june-19/sunset-with-crabs/cal/june-19-sunset-with-crabs-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/june-19/sunset-with-crabs/nocal/june-19-sunset-with-crabs-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/june-19/its-monsoon-season/cal/june-19-its-monsoon-season-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/june-19/its-monsoon-season/nocal/june-19-its-monsoon-season-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/june-17/deep-dive/nocal/june-17-deep-dive-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/june-16/pineapple-summer-pop/nocal/june-16-pineapple-summer-pop-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/june-18/travel-time/nocal/june-18-travel-time-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/june-15/shine-your-light/nocal/june-15-shine-your-light-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/june-18/tropical-vibes/nocal/june-18-tropical-vibes-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/june-17/window-of-opportunity/nocal/june-17-window-of-opportunity-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/june-14/start-your-day/nocal/june-14-start-your-day-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/june-14/doughnuts-galore/nocal/june-14-doughnuts-galore-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/june-17/nine-lives/nocal/june-17-nine-lives-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/june-17/getting-better-everyday/nocal/june-17-getting-better-everyday-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/june-16/expand-your-horizons/nocal/june-16-expand-your-horizons-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/june-14/hand-made-pony-gone-wild/nocal/june-14-hand-made-pony-gone-wild-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/june-14/the-kids-looking-outside/nocal/june-14-the-kids-looking-outside-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/june-14/good-design-is-a-tough-knitted-job/nocal/june-14-good-design-is-a-tough-knitted-job-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/june-13/viking-meat-war/jun-13-meatwar-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/june-12/june-12-sunset__71-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/june-17/hello-winter/nocal/june-17-hello-winter-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/july-19/hello-strawberry-sundae/cal/july-19-hello-strawberry-sundae-cal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/july-19/hello-strawberry-sundae/nocal/july-19-hello-strawberry-sundae-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/july-19/riding-in-the-drizzle/cal/july-19-riding-in-the-drizzle-cal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/july-19/riding-in-the-drizzle/nocal/july-19-riding-in-the-drizzle-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/july-19/we-all-scream-for-ice-cream/cal/july-19-we-all-scream-for-ice-cream-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/july-19/we-all-scream-for-ice-cream/nocal/july-19-we-all-scream-for-ice-cream-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/july-19/my-july/cal/july-19-my-july-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/july-19/my-july/nocal/july-19-my-july-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/july-19/frogs-in-the-night/cal/july-19-frogs-in-the-night-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/july-19/frogs-in-the-night/nocal/july-19-frogs-in-the-night-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/july-19/plastic-bag-free-day/cal/july-19-plastic-bag-free-day-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/july-19/plastic-bag-free-day/nocal/july-19-plastic-bag-free-day-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/july-19/save-the-tigers/cal/july-19-save-the-tigers-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/july-19/save-the-tigers/nocal/july-19-save-the-tigers-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/july-19/friendship-day/cal/july-19-friendship-day-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/july-19/friendship-day/nocal/july-19-friendship-day-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/july-19/yellow-lemon-tree/cal/july-19-yellow-lemon-tree-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/july-19/yellow-lemon-tree/nocal/july-19-yellow-lemon-tree-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/july-19/summer-energy/cal/july-19-summer-energy-cal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/july-19/summer-energy/nocal/july-19-summer-energy-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/july-19/heat-wave/cal/july-19-heat-wave-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/july-19/heat-wave/nocal/july-19-heat-wave-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/july-19/season-of-wind/cal/july-19-season-of-wind-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/july-19/season-of-wind/nocal/july-19-season-of-wind-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/july-17/fire-camp/nocal/july-17-fire-camp-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/july-18/heated-mountains/nocal/july-18-heated-mountains-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/july-17/tutti-frutti/nocal/july-17-tutti-frutti-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/july-17/memories-in-july/nocal/july-17-memories-in-july-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/july-17/cactus-hug/nocal/july-17-cactus-hug-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/july-17/keep-moving-forward/nocal/july-17-keep-moving-forward-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/july-16/sand-and-waves/nocal/july-16-sand-and-waves-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/july-16/island-river/nocal/july-16-island-river-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/july-16/ice-cream-vs-hot-dog/nocal/july-16-ice-cream-vs-hot-dog-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/july-15/summer-heat/nocal/july-15-summer-heat-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/july-15/peaceful-memories/nocal/july-15-peaceful-memories-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/july-12/july-12-floral_thing__86-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/july-15/an-intrusion-of-cockroaches/nocal/july-15-an-intrusion-of-cockroaches-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/jul-13/hot-air-balloon/jul-13-hot_air_baloon-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/jul-13/only-one/jul-13-Only_one-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/july-12/july-12-cool_summer__28-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/july-12/july-12-birdie_nam_nam__67-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/may-19/april-showers-bring-magnolia-flowers/cal/may-19-april-showers-bring-magnolia-flowers-cal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/may-19/april-showers-bring-magnolia-flowers/nocal/may-19-april-showers-bring-magnolia-flowers-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/may-19/the-wriggling-glory-of-river-uvac/cal/may-19-the-wriggling-glory-of-river-uvac-cal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/may-19/the-wriggling-glory-of-river-uvac/nocal/may-19-the-wriggling-glory-of-river-uvac-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/may-19/floral-impression/cal/may-19-floral-impression-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/may-19/floral-impression/nocal/may-19-floral-impression-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/may-19/lookout-at-sea/cal/may-19-lookout-at-sea-cal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/may-19/lookout-at-sea/nocal/may-19-lookout-at-sea-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/may-19/happy-birthday-to-pap/cal/may-19-happy-birthday-to-pap-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/may-19/happy-birthday-to-pap/nocal/may-19-happy-birthday-to-pap-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/may-19/may-mountains/cal/may-19-may-mountains-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/may-19/may-mountains/nocal/may-19-may-mountains-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/may-19/cool-as-an-octopus/cal/may-19-cool-as-an-octopus-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/may-19/cool-as-an-octopus/nocal/may-19-cool-as-an-octopus-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/may-19/stranded/cal/may-19-stranded-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/may-19/stranded/nocal/may-19-stranded-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/may-19/suns-out-tongues-out/cal/may-19-suns-out-tongues-out-cal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/may-19/suns-out-tongues-out/nocal/may-19-suns-out-tongues-out-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/may-19/hello-spring/cal/may-19-hello-spring-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/may-19/hello-spring/nocal/may-19-hello-spring-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/may-18/lake-deck/nocal/may-18-lake-deck-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/may-18/its-finally-may-my-deer/nocal/may-18-its-finally-may-my-deer-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/may-17/all-is-possible-in-may/nocal/may-17-all-is-possible-in-may-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/may-17/spring-gracefulness/nocal/may-17-spring-gracefulness-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/may-15/cruel-life/nocal/may-15-cruel-life-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/may-16/stone-dahlias/nocal/may-16-stone-dahlias-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/may-15/field-wild-flowers/nocal/may-15-field-wild-flowers-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/may-15/enjoy-may/nocal/may-15-enjoy-may-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/may-14/bird-day/nocal/may-14-bird-day-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/may-16/always-seek-knowledge/nocal/may-16-always-seek-knowledge-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/may-18/magical-sunset/nocal/may-18-magical-sunset-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/feb-19/savannah-stroll/cal/feb-19-savannah-stroll-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/feb-19/savannah-stroll/nocal/feb-19-savannah-stroll-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/feb-19/love-is-worth-fighting-for/cal/feb-19-love-is-worth-fighting-for-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/feb-19/love-is-worth-fighting-for/nocal/feb-19-love-is-worth-fighting-for-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/feb-19/dark-temptation/cal/feb-19-dark-temptation-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/feb-19/dark-temptation/nocal/feb-19-dark-temptation-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/feb-19/feel-the-love/cal/feb-19-feel-the-love-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/feb-19/feel-the-love/nocal/feb-19-feel-the-love-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/feb-19/cold-and-frost/cal/feb-19-cold-and-frost-cal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/feb-19/cold-and-frost/nocal/feb-19-cold-and-frost-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/feb-19/what-is-love/cal/feb-19-what-is-love-cal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/feb-19/what-is-love/nocal/feb-19-what-is-love-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/feb-19/polar-cold/cal/feb-19-polar-cold-cal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/feb-19/polar-cold/nocal/feb-19-polar-cold-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/feb-19/lovely-day/cal/feb-19-lovely-day-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/feb-19/lovely-day/nocal/feb-19-lovely-day-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/feb-19/let-love-speak/cal/feb-19-let-love-speak-cal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/feb-19/let-love-speak/nocal/feb-19-let-love-speak-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/feb-19/umbrella-day/cal/feb-19-umbrella-day-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/feb-19/umbrella-day/nocal/feb-19-umbrella-day-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/feb-19/sunset/cal/feb-19-sunset-cal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/feb-19/sunset/nocal/feb-19-sunset-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/feb-18/dog-year-ahead/nocal/feb-18-dog-year-ahead-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/feb-17/balloons/nocal/feb-17-balloons-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/feb-17/febpurrary/nocal/feb-17-febpurrary-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/feb-17/minimalistic-love/nocal/feb-17-minimalistic-love-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/feb-17/greben-icebreaker/nocal/feb-17-greben-icebreaker-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/feb-17/winter-wonderland/nocal/feb-17-winter-wonderland-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/feb-15/love-angel-vader/nocal/feb-15-love-angel-vader-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/feb-16/farewell-winter/nocal/feb-16-farewell-winter-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/february-14/principles-of-good-design--dieter-rams/nocal/feb-14-principles-of-good-design--dieter-rams-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/feb-16/out-there-theres-someone-like-you/nocal/feb-16-out-there-theres-someone-like-you-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/mar-18/the-great-beyond/nocal/mar-18-the-great-beyond-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/apr-19/dreaming/cal/apr-19-dreaming-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/apr-19/dreaming/nocal/apr-19-dreaming-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/apr-19/inspiring-blossom/cal/apr-19-inspiring-blossom-cal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/apr-19/inspiring-blossom/nocal/apr-19-inspiring-blossom-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/apr-19/april-showers/cal/apr-19-april-showers-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/apr-19/april-showers/nocal/apr-19-april-showers-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/apr-19/gentle-blooming/cal/apr-19-gentle-blooming-cal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/apr-19/gentle-blooming/nocal/apr-19-gentle-blooming-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/apr-19/egg-hunt-in-wonderland/cal/apr-19-egg-hunt-in-wonderland-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/apr-19/egg-hunt-in-wonderland/nocal/apr-19-egg-hunt-in-wonderland-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/apr-19/in-the-river/cal/apr-19-in-the-river-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/apr-19/in-the-river/nocal/apr-19-in-the-river-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/apr-19/signs/cal/apr-19-signs-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/apr-19/signs/nocal/apr-19-signs-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/apr-19/aphrodite/cal/apr-19-aphrodite-cal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/apr-19/aphrodite/nocal/apr-19-aphrodite-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/apr-17/april-is-the-nicest-month/nocal/apr-17-april-is-the-nicest-month-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/apr-18/wildest-dreams/nocal/apr-18-wildest-dreams-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/apr-18/no-winter-lasts-forever/nocal/apr-18-no-winter-lasts-forever-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/apr-17/april-insignia/nocal/apr-17-april-insignia-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/apr-17/once-upon-a-time/nocal/apr-17-once-upon-a-time-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/apr-18/nikes-on-my-feet/nocal/apr-18-nikes-on-my-feet-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/apr-17/colors-of-april/nocal/apr-17-colors-of-april-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/apr-17/bad-bunny/nocal/apr-17-bad-bunny-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/april-16/springing/nocal/apr-16-springing-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/april-16/rainy-day/nocal/apr-16-rainy-day-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/april-15/citrus-passion/nocal/apr-15-citrus-passion-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/april-14/sweet-april-showers-do-bring-may-flowers/nocal/apr-14-sweet-april-showers-do-bring-may-flowers-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/april-15/umbrella-season/nocal/apr-15-umbrella-season-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/mar-19/time-to-wake-up/cal/mar-19-time-to-wake-up-cal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/mar-19/time-to-wake-up/nocal/mar-19-time-to-wake-up-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/mar-19/queen-bee/cal/mar-19-queen-bee-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/mar-19/queen-bee/nocal/mar-19-queen-bee-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/mar-19/bunny-ohare/cal/mar-19-bunny-ohare-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/mar-19/bunny-ohare/nocal/mar-19-bunny-ohare-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/mar-19/a-bite-of-spring/cal/mar-19-a-bite-of-spring-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/mar-19/a-bite-of-spring/nocal/mar-19-a-bite-of-spring-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/mar-19/balance/cal/mar-19-balance-cal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/mar-19/balance/nocal/mar-19-balance-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/mar-19/stunning-beauty/cal/mar-19-stunning-beauty-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/mar-19/stunning-beauty/nocal/mar-19-stunning-beauty-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/mar-19/spring-time/cal/mar-19-spring-time-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/mar-19/spring-time/nocal/mar-19-spring-time-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/mar-19/banished/cal/mar-19-banished-cal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/mar-19/banished/nocal/mar-19-banished-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/mar-18/lets-get-outside/nocal/mar-18-lets-get-outside-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/mar-18/the-unknown/nocal/mar-18-the-unknown-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/mar-18/imagine/nocal/mar-18-imagine-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/mar-17/spring-bird/nocal/mar-17-spring-bird-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/mar-17/ballet/nocal/mar-17-ballet-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/mar-17/wake-up/nocal/mar-17-wake-up-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/mar-16/spring-is-coming/nocal/mar-16-spring-is-coming-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/mar-16/spring-is-inevitable/nocal/mar-16-spring-is-inevitable-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/march-15/tune-in-to-spring/nocal/mar-15-tune-in-to-spring-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/march-15/wake-up/nocal/mar-15-wake-up-nocal-2560x1440.jpg',
        'http://files.smashingmagazine.com/wallpapers/march-15/lets-spring/nocal/march-15-lets-spring-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/march-14/marching-forward/nocal/mar-14-marching-forward-nocal-2560x1440.png',
        'http://files.smashingmagazine.com/wallpapers/march-12/march-12-march_fusion__77-nocal-2560x1440.jpg',
        'https://cloud.netlifyusercontent.com/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/75537c7c-9551-493a-a8f5-0e8b219c439f/march-11-daydream-69-nocal-2560x1440.jpg']


@pytest.fixture()
def correct_hash():
    return {'7a597df7848963af62631d3034604696e161d5121339e0624bc83bd69016e9bd',
            'b04a8dbb6704a6f6c03834d1e98d85f4125474b54078728d45344574b4ff543f',
            '1d58c67cfcb998af1133099084d0814c6a791aa8c4b3a10c692abd5ff8674f6f',
            '3655e5338488566893adc89ca92167c353409ac41a62adff8ca74a893f1eac8a',
            '2e9c42fd66888d2f5fb3c39624a2af094da1d6ff85f5d50d59227a6383749f7d',
            '6b8698f90ea5ada90a0b44227b5983036edb2aa687efa166207fa79f806b8f69',
            'be3c53745715f18f8cd344f56ff508f226faffb26673df260c2e9a112d24eefe',
            '724698a6c79bf872ac9630a540a5c0d2cb316c7ea805439f478ff3997205f4d4',
            '9676d3bd2c7af99ed1dd9e0b980537be1f7a2edf5f9392edc43e28df3eacb1fc',
            '4847e4cd540098e987bb1ac2ae8bb670d0061a4c0187043dd6ee68cf5e7892fb',
            '3c55643d19f14fdfbfc1173ec823afd8bcdd23e50edb9eb77d0390290b94d99e',
            '4aa144f9bc0a5c8fa188ca64222cf4ca03bc9dc928b3ccd8a79a5aec75190645',
            '807336f6e0101c4289e828090bf2861902ca00eb33d4cf519f0fc56e014c3229',
            '174c6d295e4d27664d9a926040a095a19f1d8dcf86545f0845e6b3bc0a98deb2',
            '224d65f96204ee4b12db44f51af9fd0d74efb14a333339401266334895031607',
            '1142b2835fa98d31e56cdc6f200145ee6c9c5667d34c7082b2360c17e3f86892',
            '11219b6faa9d4ee6544b6203d544f41cac200ff3a54ecea6befbbbee5b95e24f',
            '7bc636d2f729c6d39ab5e89ae3f2abc6fef5a6f771308ab912516608064bd3ef',
            '0cefd2862ef08556c2a8fe4f5ca5b2f8263dfc715a2267e49a404cc2803c7b84',
            '778021e4a3756f8aaa37c80305b7ced034308dd898187c9113e61eecd10561a3',
            '4d25fdb07fb9820183c68a88eb4c84f54480c0a8f5176c191c653a71d0969929',
            'ddefd2ac511f4a51201b7346097fca1216b5e281495a15451228abf56f896966',
            '4c6e01a741684d530af2eedce8c6ac996b1bdb1e55f1bd6090b2c9e9959c2506',
            'db5a58c6971eb2cf17c34877249a13669d25f21565a074d36238fdfd35e30ecc',
            '8c6f6887d825811ca8b8b9f76ffe9a173fbbb862d97d05cf19bf006c2e60ed4f',
            'e29e8058cdb6a320e6e83948f249870d4fb42b9fd26cc9586519990dc16b19a9',
            '51a84190bd7c06f2614e468841c10f8ee0b33ddfdf34e386027fbc374cfcd9cb',
            '8181b8bf6bc5ae9e44b3681d2e9eaa32cdf840663b689f53641b5ae0f422238e',
            '20853652a60b535da8c71884c6a28c63069a9b99923bd124e79ebcb67a048798',
            '57a478bfa238ea3021923191ee3ba6f3393a20236b573ac0184f95dd4c1c20e0',
            'b777d75279636b8e039f7359895a8c72900091c27a676de43e5c1a5e63073cfa',
            '7b3260ffd791a2ebd84efdd999e90914a0218cee83f4f99f916bd2cc049e3f5f',
            '74870fe77fde486b3c9a6f46c53affe83ab77267f7eddad5c7c4e32bd295d1e8',
            '793c2c51e885f7e805891a575647c6d2567acaf10abc8734ab81b5c798cb18dc',
            '6902272de1c30d7d7cbecbaeae93bea48aa7a9286f9a725ac45248a900785e41',
            'd082190ae0a69cddb638a3b0d56cc7664087b9b6e455ea943eb60537d8ae158f',
            'e8de6ff8f56ce63df2c745986b63d451e0879f16f9725d1aa5b21f33aac930f8',
            '5b1c7c6ecd9d7126110000741fd2ea80197c5682671b6b2793a7e8874decfd15',
            '685a945485f3b545912958fcc17f5ac4403fb03deeaf1391552d83bb2df2607e',
            '4359c8dc4ac65246d3503a2f4dbce975f9f533dbba1d7c8c4e8de2958fee7a10',
            '82fce5d6b4598c103a8172421ff032f1aa3fb0446876942266165f0d99edc78d',
            '40f2d0808c4da3582150e00440cf3ec3e8d046e65ea9c8477547571236df0855',
            'b1b91c01c728b1668ebf711fbf3db0fe1d8dedd21ec78b6b414d7e84b068dc7f',
            'e2235d29bd73a48fdbc6640e7cc8ca4f5930c969b9a3e22ba78b6e9a7e1ce707',
            '687480b2e82d71c8310fd9bb76fd01d0db5a3fbe6fcf04f7ab62263902f32c03',
            'f080d3dbbcff28f0ec4ab4c80ec28769ae6b36b43c05934efac9ed6fb0def7ad',
            'b62a9e79f0f5e50f03953ff2531b33087b23cc16f311baf36c27b88ae0b41a0b',
            'd756761b7fe22817b7f4ee2f73f70368e118131323afbb30567a32a09c49b51f',
            'bd93d1d373253c0c3f9b116336d1515fc9a6f0c56b8e4a53429412a75585032f',
            '9ca615e4f6e2d7e1dcf605be356b64544a52443b0bbe28447c0e2a234b83123b',
            'e8a44f5d352eda382ff88ac9f12c980da199afb1b50fce4b52803fbb7d594969',
            'ab0b4b682258ce4eb16781e679e0a67e563ca001697156628b9cbedb47072c93',
            'fcabf0edeb8d19e524c534bafa7e6c9abe32233b9a32cc462644aa4a2d2d3c86',
            '3122f9f7ef96df2df7191d323eef11df525c4cd01288b2a8f6a78da5887f57c8',
            'fb0fb68360af0156ff2834f861229bbb5bf00664d5d34026379c881a087f4353',
            'd5069c0dbe6bb1d68c0c1d77caf8f751228e3f45ef6cfe3511c95bf750c4a43e',
            'db8daf0a232acb28e93c8ed0d44d20ee465cc6c8c287b7168ebec4ac446e6b73',
            '598e5d415f48547eeeb40dd136d1b0de7bcf39884da29e9a6dd29a145b9521b1',
            '54fe654019166cab841f87fdc622484b2fb42f121da7b4bc240a1ec3276676a7',
            '2e88dc05412eb94beb668b377483933c8b076515e9500d3f55a18eb2d44d30e5',
            'f5a4d6a2707e5d848d3469d915aa3994b005aa9c307aac4f81dec1072d4b0272',
            '57c7d7b29ae27e585aa0e7bae9e6060ba9cb37a15b0113c5550e11a2fb4618a2',
            '94d1a69c29ac184d6505bcaff2c2dc6614aa91224bca4de9148828c2d726738f',
            '76851795d8c7caf3cf4e9edd1ffe6a5497c9f83d3006790c80a8544dbceecb94',
            'dcdee2b9d4caa82abbb7de324939b68d452fe30a1df217267b37f1b461a94a5f',
            'ef2cf5783a89b94886edc80eced5f903042d7a4e088dfe6b267f93c06ad49520',
            '8b5d56d4c35a0708e13086d82478736f615907a97090a55e184727686210389d',
            'b64b13017278bf6db0bba69d0c8fa3c25aa8a6285f9105a0308f5f19cc8088bc',
            '5bff103c1c97362ff747fb6fd28482a74f9c9febb73743a08615ac6f5ff375a7',
            '70d178a6a03094df2833891756796099cdd38cfa3513d7b98956d8b76dba6db9',
            'ba45e24db5ef4b3445f7362d7df48928044ee3ac73567f5784f7081613b15d72',
            'd73ba894cf2067ccd99347db6f9395f7912487f841b7907a46c4b48044c1a135',
            'af85927720838e6ac4bbbd3881d7e36f1a14575df98ef85d3bdd51c2d7695dfb',
            '4ddb8771b46563eadeeeb1c3692d9833a0fcf3dd927bff094e3605b690d50e47',
            'ee96b9dcfc3404c4fe7bdcc10c06b37606eab0cae55e7eac8caa480c61a71ea8',
            'd8db00996addb416bf392bb38b3756916e2b6bc9642996576e63d3a73df7c8eb',
            '7e09e9daa9414a367345e93555be4b376722dc706400cf6b88e0fcf74cf57deb',
            '95ed6a8dc94243affbe8de66a3553e745ccde371953a54899a86d62d72a25107',
            '601e5db67445dedcd580a4c68b3a426b66f0d32a93901cf8c75272c1ee2bdfaa',
            'ee464f96cec8db309116f9a2750b1f72f9f8c194e912b3e79dc70e11bffe9b94',
            '1fc2a1df2ce65e9228e9796309ea3959b49dde9fbbc9409adadbb73e99458532',
            '87ef0ac5550e004caead9c0929b445655b69ce5c48348e2e89296796e91a077e',
            '72672eb354cbe122b53c78c4bda6d6bbe8ce8cb5216db65e810583b55c59c3a8',
            '2a3e20f8b62d84e2b83100136581c5d5fb82ce4d9e9c3520e0617b8a692d1ae9',
            'c743ac360d26e26046306c68dd59f789f5ba6147d016026c2b95b2769134803d',
            '20097d22144d9db8dc1840f29dc8d1a7ca464f6fcddf7bf95ded9323fb42f673',
            '2c15ebdc5a862eec57cb5a2aedbf22f99b4b9f2dcaf91d5d689923ec9c85ec88',
            'e64cc78bd70a89671cf9fd93ee11e55df8e1b226fae801187b72ae69c5d1695d',
            '5f7791b544ac4891ac868aac90506e540162ff8d9f2cae18d0dd01ef54ea04f1',
            'dc91baf236638b153881ab1bf624ebdae5458963dcd40c18ea8fa89d101037c5',
            'f820cbdcd4ce735f77157fda4dbb20c767a6d29c42086231d6f8f49f6d66ebb4'}
