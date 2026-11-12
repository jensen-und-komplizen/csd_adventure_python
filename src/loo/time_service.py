import re

import requests


class TimeService:

    def __init__(self):
        self.tz = "Europe/Berlin"

    def current_time(self):
        return TimeService.current_time_in(self.tz)

    @staticmethod
    def current_time_in(tz):
        try:
            response = requests.get("https://csd-timeservice.idiot.games/")
            if response.status_code != 200:
                raise Exception(f"Wrong status: {response.status_code}")

            match = re.search(r"(-?\d+)", response.text)
            if match:
                return int(match.group(1))
        except Exception as e:
            print(e)

        return -1
