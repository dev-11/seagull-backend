from .external_services.admiralty_service import AdmiraltyService
from .tidal_service import TidalService
from dom.mappers import AdmiraltyDataMapper, AdmiraltyEventTypeMapper
import settings


def admiralty_service_instance():
    return AdmiraltyService(settings.ADMIRALTY_STATIONS_ENDPOINT, settings.ADMIRALTY_API_KEY)


def tidal_service_instance():
    return TidalService(admiralty_service_instance(), AdmiraltyDataMapper(AdmiraltyEventTypeMapper()))
