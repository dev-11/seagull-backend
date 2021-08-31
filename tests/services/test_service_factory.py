import unittest

from services.external_services.admiralty_service import AdmiraltyService
from services.service_factory import admiralty_service_instance


class AdmiraltyServiceInstanceTest(unittest.TestCase):
    def test_factory_method_returns_correct_instance(self):
        instance = admiralty_service_instance()
        self.assertIsInstance(AdmiraltyService, instance)
