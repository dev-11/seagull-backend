import requests

from settings import ADMIRALTY_HEADER_KEY


class AdmiraltyService:
    def __init__(self, endpoint, api_key):
        self._endpoint = endpoint
        self._api_key = api_key

    def get_tidal_events(self, station_id):
        headers = self._get_headers()
        url = f'{self._endpoint}{station_id}/TidalEvents'
        api_get = requests.get(url=url, headers=headers)
        return api_get.json()

    def _get_headers(self):
        return {ADMIRALTY_HEADER_KEY: self._api_key}
