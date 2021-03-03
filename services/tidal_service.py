from .external_services.admiralty_service import AdmiraltyService
from dom.mappers import AdmiraltyDataMapper

from settings import HAMMERSMITH_BRIDGE_STATION_ID


class TidalService:
    def __init__(self, admiralty_service: AdmiraltyService, mapper: AdmiraltyDataMapper):
        self._admiralty_service = admiralty_service
        self._mapper = mapper

    def get_tidal_events(self, station_id):
        return self._admiralty_service.get_tidal_events(station_id)

    def get_tidal_data(self):
        raw_data = self.get_tidal_events(HAMMERSMITH_BRIDGE_STATION_ID)
        return [self._mapper.to_dom(_) for _ in raw_data]


"""
    WillyWeather interpolates its tide times for many locations by converting the tide forecasts provided by the 
    United Kingdom Hydrographic Office</em> for standard ports.
    
    The tide times for River Thames - Chiswick Eyot have been adjusted by 8 min for low tide and 3 min for high tide to
    the official tide times for Hammersmith Bridge.
    
    Tide height data is gathered from Hammersmith Bridge, adjustments made where applicable.</p>
"""