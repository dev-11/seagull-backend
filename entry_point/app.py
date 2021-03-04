from dom import AdmiraltyDataMapper, AdmiraltyEventTypeMapper
from services import service_factory
import settings as s
from services.station_id_service import StationIdService


def lambda_handler(event, context):

    headers = event["params"]["header"]
    location = (
        headers[s.LOCATION_HEADER_KEY]
        if s.LOCATION_HEADER_KEY in headers
        else None
    )

    station_id = StationIdService().get_station_id(location)

    admiralty = service_factory.admiralty_service_instance()
    admiralty_data = admiralty.get_tidal_events(station_id)

    mapper = AdmiraltyDataMapper(AdmiraltyEventTypeMapper())

    tide_times = [mapper.to_dom(_) for _ in admiralty_data]
    tidal_service = service_factory.tidal_service_instance()
    tide_events = tidal_service.get_tidal_data(tide_times)

    return {'statusCode': 200, 'body': [_.to_dict() for _ in tide_events]}
