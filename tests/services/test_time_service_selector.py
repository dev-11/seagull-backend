import unittest

from services.adjust_time_service import ChiswickEyotTimeService
from services.time_service_selector import TimeServiceSelector, map_location_to_time_service, get_all_time_services


class TimeServiceSelectorTest(unittest.TestCase):
    def test_selector_raisesError_on_None_strategies(self):
        tss = TimeServiceSelector(None)
        service_name = 'test_service_name'
        self.assertRaises(TypeError, tss.select, service_name)

    def test_selector_raisesError_on_empy_strategies(self):
        tss = TimeServiceSelector([])
        service_name = 'test_service_name'
        self.assertRaises(IndexError, tss.select, service_name)

    def test_selector_raisesError_on_None_strategy(self):
        tss = TimeServiceSelector([None])
        service_name = 'test_service_name'
        self.assertRaises(AttributeError, tss.select, service_name)

    def test_selector_returns_correct_strategy(self):
        tss = TimeServiceSelector([ChiswickEyotTimeService()])
        service_name = 'chiswick_eyot_time'
        result = tss.select(service_name)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, ChiswickEyotTimeService)

    def test_map_location_to_time_service_returns_correct_value_for_simple_location(self):
        location = 'asdf'
        service_name = map_location_to_time_service(location)
        self.assertEqual('asdf_time', service_name)

    def test_map_location_to_time_service_returns_correct_value_for_complex_location(self):
        location = 'TestLocation'
        service_name = map_location_to_time_service(location)
        self.assertEqual('test_location_time', service_name)

    def test_map_location_to_time_service_returns_correct_value_for_empty_location(self):
        location = ''
        service_name = map_location_to_time_service(location)
        self.assertEqual('_time', service_name)

    def test_map_location_to_time_service_rasises_error_for_None_location(self):
        location = None
        self.assertRaises(TypeError, map_location_to_time_service, location)

    def test_get_all_time_services(self):
        all_services = get_all_time_services()
        self.assertEqual(1, len(all_services))
        self.assertIsInstance(all_services[0], ChiswickEyotTimeService)
