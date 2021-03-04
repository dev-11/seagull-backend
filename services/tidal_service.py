from typing import List

from dom import TideEvent

from .adjust_time_service import AdjustTimeService


class TidalService:
    def __init__(self, adjust_time_service: AdjustTimeService):
        self._adjust_time_service = adjust_time_service

    def get_tidal_data(self, tide_times: List[TideEvent]):
        for _ in tide_times:
            _.time += self._adjust_time_service.get_adjusted_time(_.type)

        return tide_times


"""
    WillyWeather interpolates its tide times for many locations by converting the tide forecasts provided by the 
    United Kingdom Hydrographic Office</em> for standard ports.
    
    The tide times for River Thames - Chiswick Eyot have been adjusted by 8 min for low tide and 3 min for high tide to
    the official tide times for Hammersmith Bridge.
    
    Tide height data is gathered from Hammersmith Bridge, adjustments made where applicable.</p>
"""
