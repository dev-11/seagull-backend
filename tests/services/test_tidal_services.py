import unittest
from services.tidal_service import TidalService


class TestTidalService(unittest.TestCase):
    def test_01(self):
        service = TidalService('endpoint', 'api_key')
        events = service.get_tidal_events('1234')
        self.assertN