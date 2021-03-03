from .external_services.admiralty_service import AdmiraltyService
from .tidal_service import TidalService
from dom.mappers import AdmiraltyDataMapper, AdmiraltyEventTypeMapper
from .secret_manager_service import SecretManagerService

import repositories.environment_repository as er


import settings


def admiralty_service_instance():
    env_repo = er.EnvironmentRepository()
    secret_manager = SecretManagerService(env_repo)
    key = secret_manager.get_secret("ADMIRALTY_API_KEY")

    return AdmiraltyService(settings.ADMIRALTY_STATIONS_ENDPOINT, key)


def tidal_service_instance():
    return TidalService(admiralty_service_instance(), AdmiraltyDataMapper(AdmiraltyEventTypeMapper()))
