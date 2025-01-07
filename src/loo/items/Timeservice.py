import re
import requests


class TimeService:
    tz = ""
    def __init__(self):
        self.tz = "Europe/Berlin"


    def current_time():
        pattern = re.compile(r"(\d+)", re.MULTILINE)

        try:
            response = requests.get("https://csd-timeservice.idiot.games/")
            if response.status_code != 200:
                raise Exception(f"Wrong status: {response.status_code}")

            matcher = pattern.search(response.text)
            if matcher:
                return int(matcher.group(1))
        except Exception as e:
            print(str(e))

        return -1
