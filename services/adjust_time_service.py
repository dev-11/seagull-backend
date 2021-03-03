from datetime import timedelta

from dom.data_objects import TideType


class AdjustTimeService:
    @staticmethod
    def get_adjusted_time(tide_type: TideType) -> timedelta:
        if tide_type == TideType.Low:
            return timedelta(minutes=8)
        if tide_type == TideType.High:
            return timedelta(minutes=3)
