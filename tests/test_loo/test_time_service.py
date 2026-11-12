import unittest

from src.loo.time_service import TimeService


class TestTimeService(unittest.TestCase):

    def test_current_time_looks_good(self):
        self.assertGreater(TimeService.current_time_in("Europe/Berlin"), -1)
