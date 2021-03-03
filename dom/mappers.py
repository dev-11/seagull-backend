from abc import ABC, abstractmethod

from .data_objects import TideEvent, TideType
from .exceptions import InvalidDataToMapException
from datetime import datetime
from settings import DATE_FORMAT_WITH_MILLISECONDS, DATE_FORMAT_WITHOUT_MILLISECONDS


class Mapper(ABC):
    @abstractmethod
    def to_dom(self, source):
        pass


class AdmiraltyEventTypeMapper(Mapper):
    def to_dom(self, source):
        if source == 'LowWater':
            return TideType.Low
        if source == 'HighWater':
            return TideType.High

        return TideType.Undefined


class AdmiraltyDataMapper(Mapper):

    def __init__(self, event_type_mapper: AdmiraltyEventTypeMapper):
        self._event_type_mapper = event_type_mapper

    @staticmethod
    def get_correct_date_format(date: str):
        return DATE_FORMAT_WITH_MILLISECONDS if '.' in date else DATE_FORMAT_WITHOUT_MILLISECONDS

    def to_dom(self, source):
        if source is None:
            raise InvalidDataToMapException(source)

        if 'EventType' not in source:
            raise InvalidDataToMapException('EventType')

        if 'DateTime' not in source:
            raise InvalidDataToMapException('DateTime')

        if 'Height' not in source:
            raise InvalidDataToMapException('Height')

        return TideEvent(
            type=self._event_type_mapper.to_dom(source['EventType']),
            time=datetime.strptime(source['DateTime'], self.get_correct_date_format(source['DateTime'])),
            height=source['Height']
        )
