from unittest.mock import Mock

from dom.mappers import AdmiraltyEventTypeMapper, TideType
from repositories import EnvironmentRepository


def get_mocked_AdmiraltyEventTypeMapper():
    mocked_mapper = AdmiraltyEventTypeMapper()
    mocked_mapper.to_dom = Mock(name='to_dom')
    mocked_mapper.to_dom.return_value = TideType.High
    return mocked_mapper


def get_env_repo():
    er = EnvironmentRepository()
    er.get_parameter = Mock(name='get_parameter')
    er.get_parameter.return_value = 'test_value'
    return er
