from datetime import datetime
from loo.items.Timeservice import TimeService


class Clock:
    def __init__(self):
        self.time_service = TimeService()

    def tell_hh_mm(self):
        try:
            current_time_seconds = self.time_service.current_time()
            date_time = datetime.fromtimestamp(current_time_seconds)
            ret = date_time.strftime("%I:%M")
            hour = date_time.hour

            if hour < 6:
                ret += " ... waaaaaay too early!"
            elif hour < 12:
                ret += " ... yawn!"
            elif hour < 18:
                ret += " ... lunch? food?"
            elif hour < 24:
                ret += " ... pizza?"
            else:
                ret += " ... I see ghosts!"

            return ret
        except Exception as e:
            return "dunno"