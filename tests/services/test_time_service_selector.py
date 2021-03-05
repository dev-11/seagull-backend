import unittest

from services.adjust_time_service import ChiswickEyotTimeService
from services.time_service_selector import TimeServiceSelector


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
