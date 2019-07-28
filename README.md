# Wallpaper crawler

Required environment:
* [Python3.7+](https://www.python.org/downloads/) 
* [pip](https://pip.pypa.io/en/stable/installing/)

Basic setup:
`pip install -r requirements.txt && pip install -e .`

Start using:
`python app/main.py`

Usage: 

```
main.py [-h] --path PATH --start-time START_TIME --end-time END_TIME
             --resolution RESOLUTION [--log-file LOG_FILE]
             [--timeout TIMEOUT] [--verbose]

CLI program for auto downloading wallpapers.

optional arguments:
  -h, --help            show this help message and exit
  --path PATH, --P PATH
                        Path to the folder where to store images and where
                        previous images exist (preferably).
  --start-time START_TIME, --S START_TIME
                        Start time for period in which wallpapers published.
                        In yyyy-mm-dd format
  --end-time END_TIME, --E END_TIME
                        End time for period in which wallpapers published. In
                        yyyy-mm-dd format
  --resolution RESOLUTION, --R RESOLUTION
                        Resolution in which wallpapers needs to be downloaded.
                        eg.: 1280x720, 320x480, 2560x1440
  --log-file LOG_FILE, --L LOG_FILE
                        Path where to store log file, default: output.log
  --timeout TIMEOUT, --T TIMEOUT
                        Timeout for each request out of the program in
                        seconds, default 10s
  --verbose, --V        Printing whole program log to the console.
```

Testing: `pytest`

Testing with cli records: `pytest -o log_cli=true`