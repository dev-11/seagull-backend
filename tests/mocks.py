from unittest.mock import Mock
from dom.mappers import AdmiraltyEventTypeMapper
from dom.mappers import TideType


def get_mocked_AdmiraltyEventTypeMapper():
    mocked_mapper = AdmiraltyEventTypeMapper()
    mocked_mapper.to_dom = Mock(name="to_dom")
    mocked_mapper.to_dom.return_value = TideType.High
    return mocked_mapper
