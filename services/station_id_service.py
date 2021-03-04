class StationIdService:
    def get_station_id(self, location):
        return station_ids[location]


station_ids = {
    'ChiswickEyot': '0115'
}