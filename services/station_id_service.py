class StationIdService:
    def get_station_id(self, location):
        return station_ids[location] if location in station_ids.keys() else None


station_ids = {
    'ChiswickEyot': '0115'
}