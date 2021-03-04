from .service_factory import get_all_time_services


class TimeServiceSelector:
    def __init__(self):
        self._strategies = get_all_time_services()

    def select(self, service_name: str):
        return list(filter(lambda s: s.get_service_name() == service_name, self._strategies))[0]
