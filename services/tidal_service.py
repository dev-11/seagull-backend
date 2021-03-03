from dom.mappers import AdmiraltyDataMapper
from settings import HAMMERSMITH_BRIDGE_STATION_ID

from .adjust_time_service import AdjustTimeService
from .external_services.admiralty_service import AdmiraltyService


class TidalService:
    def __init__(
        self,
        admiralty_service: AdmiraltyService,
        mapper: AdmiraltyDataMapper,
        adjust_time_service: AdjustTimeService,
    ):
        self._admiralty_service = admiralty_service
        self._mapper = mapper
        self._adjust_time_service = adjust_time_service

    def get_tidal_events(self, station_id):
        return self._admiralty_service.get_tidal_events(station_id)

    def get_tidal_data(self):
        raw_data = self.get_tidal_events(HAMMERSMITH_BRIDGE_STATION_ID)

        mapped_data = []
        for _ in raw_data:
            dto = self._mapper.to_dom(_)
            dto.time += self._adjust_time_service.get_adjusted_time(dto.type)
            mapped_data.append(dto)

        return mapped_data


"""
    WillyWeather interpolates its tide times for many locations by converting the tide forecasts provided by the 
    United Kingdom Hydrographic Office</em> for standard ports.
    
    The tide times for River Thames - Chiswick Eyot have been adjusted by 8 min for low tide and 3 min for high tide to
    the official tide times for Hammersmith Bridge.
    
    Tide height data is gathered from Hammersmith Bridge, adjustments made where applicable.</p>
"""
