import unittest

from parameterized import parameterized

from dom.mappers import AdmiraltyEventTypeMapper, AdmiraltyDataMapper
from dom.mappers import TideType
from datetime import datetime

from tests.mocks import get_mocked_AdmiraltyEventTypeMapper
from dom.exceptions import InvalidDataToMapException


class AdmiraltyEventTypeMapperTests(unittest.TestCase):
    def test_to_dom_returns_Low_on_LowWater(self):
        event_type = 'LowWater'

        aetm = AdmiraltyEventTypeMapper()
        result = aetm.to_dom(event_type)

        self.assertEqual(TideType.Low, result)

    def test_to_dom_returns_High_on_HighWater(self):
        event_type = 'HighWater'

        aetm = AdmiraltyEventTypeMapper()
        result = aetm.to_dom(event_type)

        self.assertEqual(TideType.High, result)

    def test_to_dom_returns_Undefined_on_empty_string(self):
        event_type = ''

        aetm = AdmiraltyEventTypeMapper()
        result = aetm.to_dom(event_type)

        self.assertEqual(TideType.Undefined, result)

    def test_to_dom_returns_Undefined_on_None(self):
        event_type = None

        aetm = AdmiraltyEventTypeMapper()
        result = aetm.to_dom(event_type)

        self.assertEqual(TideType.Undefined, result)

    def test_to_dom_returns_Undefined_on_unknown_type(self):
        event_type = 'asdf'

        aetm = AdmiraltyEventTypeMapper()
        result = aetm.to_dom(event_type)

        self.assertEqual(TideType.Undefined, result)


class AdmiraltyDataMapperTests(unittest.TestCase):
    def test_01(self):
        json = {
            'EventType': 'LowWater',
            'DateTime': '2021-03-02T00:13:59.5',
            'Height': 0.04281385004939631,
        }

        adm = AdmiraltyDataMapper(AdmiraltyEventTypeMapper())
        dom = adm.to_dom(json)

        self.assertIsNotNone(dom)
        self.assertEqual(datetime(2021, 3, 2, 0, 13, 59, 500000), dom.time)
        self.assertEqual(TideType.Low, dom.type)
        self.assertEqual(0.04281385004939631, dom.height)

    @parameterized.expand([
        ["missing_event_type", {'DateTime': '2021-03-02T00:13:59.5', 'Height': 0.04281385004939631}],
        ["missing_datetime", {'EventType': 'LowWater', 'Height': 0.04281385004939631}],
        ["missing_height", {'EventType': 'LowWater', 'DateTime': '2021-03-02T00:13:59.5'}],
        ["empty_json", {}],
        ["None_json", None]])
    def test_to_dom_raises_exception_for_incorrect_parameters(self, name, json):
        adm = AdmiraltyDataMapper(get_mocked_AdmiraltyEventTypeMapper())
        self.assertRaises(InvalidDataToMapException, adm.to_dom, json)
