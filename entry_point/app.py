from dom import AdmiraltyDataMapper, AdmiraltyEventTypeMapper
from services import service_factory
import settings as s
from services.station_id_service import StationIdService
from services.tidal_service import TidalService
from services.time_service_selector import TimeServiceSelector, get_all_time_services, map_location_to_time_service


def lambda_handler(event, context):
    querystring = event["params"]["querystring"]
    location = (
        querystring[s.QUERYSTRING_LOCATION_KEY]
        if s.QUERYSTRING_LOCATION_KEY in querystring
        else None
    )

    station_id = StationIdService().get_station_id(location)

    if station_id is None:
        return {'statusCode': 400, 'body': f'unknown location {location}'}

    admiralty = service_factory.admiralty_service_instance()
    admiralty_data = admiralty.get_tidal_events(station_id)

    mapper = AdmiraltyDataMapper(AdmiraltyEventTypeMapper())

    tide_times = [mapper.to_dom(_) for _ in admiralty_data]

    tss = TimeServiceSelector(get_all_time_services())
    time_service = tss.select(map_location_to_time_service(location))

    tidal_service = TidalService(time_service)
    tide_events = tidal_service.get_tidal_data(tide_times)

    return {'statusCode': 200, 'body': [_.to_dict() for _ in tide_events]}
