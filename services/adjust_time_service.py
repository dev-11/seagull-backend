from abc import ABC, abstractmethod
from datetime import timedelta

from dom.data_objects import TideType


class AdjustTimeService(ABC):

    def get_service_name(self):
        service_name = self.__class__.__name__.replace("Service", "")

        return "".join(
            ["_" + i.lower() if i.isupper() else i for i in service_name]
        ).lstrip("_")

    @abstractmethod
    def get_adjusted_time(self, tide_type: TideType) -> timedelta:
        pass


class ChiswickEyotTimeService(AdjustTimeService):
    def get_adjusted_time(self, tide_type: TideType) -> timedelta:
        if tide_type == TideType.Low:
            return timedelta(minutes=8)
        if tide_type == TideType.High:
            return timedelta(minutes=3)

        raise TypeError(tide_type)
