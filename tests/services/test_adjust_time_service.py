import unittest
from datetime import timedelta

from parameterized import parameterized

from dom import TideType
from services.adjust_time_service import ChiswickEyotTimeService


class ChiswickEyotTimeServiceTest(unittest.TestCase):
    def test_01(self):
        cets = ChiswickEyotTimeService()
        result = cets.get_adjusted_time(TideType.High)
        self.assertEqual(timedelta(minutes=3), result)

    def test_02(self):
        cets = ChiswickEyotTimeService()
        result = cets.get_adjusted_time(TideType.Low)
        self.assertEqual(timedelta(minutes=8), result)

    @parameterized.expand(
        [
            ['Undefined_tide_type', TideType.Undefined],
            ['Falling_tide_type', TideType.Falling],
            ['Raising_tide_type', TideType.Raising],
            ['None_tide_type', None],
        ]
    )
    def test_get_adjusted_time_raises_TypeError_for_unsupported_tide_types(self, name, tide_type):
        cets = ChiswickEyotTimeService()
        self.assertRaises(TypeError, cets.get_adjusted_time, tide_type)

    def test_get_service_name_returns_correct_service_name(self):
        cets = ChiswickEyotTimeService()
        service_name = cets.get_service_name()
        self.assertEqual('chiswick_eyot_time', service_name)
