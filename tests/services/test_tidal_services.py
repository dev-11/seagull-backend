import unittest
from datetime import datetime

from dom import TideEvent, TideType
from services.tidal_service import TidalService
from tests.mocks import get_mocked_adjust_time_service


class TestTidalService(unittest.TestCase):
    def test_get_tidal_data_raises_TypeError_for_None_data(self):
        service = TidalService(get_mocked_adjust_time_service())
        self.assertRaises(TypeError, service.get_tidal_data, None)

    def test_get_tidal_data_returns_empty_array_for_empty_array(self):
        service = TidalService(get_mocked_adjust_time_service())
        result = service.get_tidal_data([])
        self.assertEqual([], result)

    def test_get_tidal_data_returns_correct_data(self):
        service = TidalService(get_mocked_adjust_time_service())
        result = service.get_tidal_data([TideEvent(type=TideType.High, time=datetime(1, 1, 1), height=1)])
        self.assertEqual(1, len(result))
        self.assertEqual(TideType.High, result[0].type)
        self.assertEqual(datetime(1, 1, 1), result[0].time)
        self.assertEqual(1, result[0].height)

