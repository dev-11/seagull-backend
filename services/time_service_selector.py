from typing import List
from .adjust_time_service import AdjustTimeService


class TimeServiceSelector:
    def __init__(self, strategies: List[AdjustTimeService]):
        self._strategies = strategies

    def select(self, service_name: str):
        return list(filter(lambda s: s.get_service_name() == service_name, self._strategies))[0]
