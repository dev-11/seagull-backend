from typing import List
from .adjust_time_service import AdjustTimeService, ChiswickEyotTimeService


class TimeServiceSelector:
    def __init__(self, strategies: List[AdjustTimeService]):
        self._strategies = strategies

    def select(self, service_name: str):
        return list(filter(lambda s: s.get_service_name() == service_name, self._strategies))[0]


def get_all_time_services() -> List[AdjustTimeService]:
    return [
        ChiswickEyotTimeService(),
    ]


def map_location_to_time_service(location: str):
    return "".join(
        ["_" + i.lower() if i.isupper() else i for i in location]
    ).lstrip("_") + '_time'

