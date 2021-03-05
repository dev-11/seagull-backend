import unittest
from services.station_id_service import StationIdService


class StationIdServiceTest(unittest.TestCase):
    def test_get_station_id_returns_correct_value(self):
        sis = StationIdService()
        location = 'ChiswickEyot'
        station_id = sis.get_station_id(location)
        self.assertEqual('0115', station_id)

    def test_get_station_id_returns_None_for_empty_location(self):
        sis = StationIdService()
        location = ''
        station_id = sis.get_station_id(location)
        self.assertEqual(None, station_id)

    def test_get_station_id_returns_None_for_None_location(self):
        sis = StationIdService()
        location = None
        station_id = sis.get_station_id(location)
        self.assertEqual(None, station_id)

    def test_get_station_id_returns_None_for_unknown_location(self):
        sis = StationIdService()
        location = 'asdfasdf'
        station_id = sis.get_station_id(location)
        self.assertEqual(None, station_id)
