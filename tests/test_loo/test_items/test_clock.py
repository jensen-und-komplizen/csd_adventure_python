import unittest
from src.loo.items.Timeservice import TimeService

class TestTimeService(unittest.TestCase):
    def test_current_time_looks_good(self):
        timestamp = TimeService.current_time()
        self.assertGreater(timestamp, -1, "timestamp should be greater than -1")

