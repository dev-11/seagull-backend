import repositories.environment_repository as er
import settings
from dom.mappers import AdmiraltyDataMapper, AdmiraltyEventTypeMapper
from typing import List

from .adjust_time_service import ChiswickEyotTimeService, AdjustTimeService
from .external_services.admiralty_service import AdmiraltyService
from .secret_manager_service import SecretManagerService
from .tidal_service import TidalService


def admiralty_service_instance():
    env_repo = er.EnvironmentRepository()
    secret_manager = SecretManagerService(env_repo)
    key = secret_manager.get_secret('ADMIRALTY_API_KEY')

    return AdmiraltyService(settings.ADMIRALTY_STATIONS_ENDPOINT, key)


def tidal_service_instance():
    return TidalService(ChiswickEyotTimeService())


def get_all_time_services() -> List[AdjustTimeService]:
    return [
        ChiswickEyotTimeService(),
    ]
