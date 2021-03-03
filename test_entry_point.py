# import unittest
# from entry_point import app
# from services.external_services.admiralty_service import AdmiraltyService as TidalService
# import settings as s
#
#
# class TestEntryPoint(unittest.TestCase):
#     def test_01(self):
#         result = app.lambda_handler(None, None)
#         self.assertEqual({'statusCode': 200, 'body': 'Hello from Lambda!'}, result)
#
#     def test_02(self):
#         api_reader = TidalService(s.ADMIRALTY_STATIONS_ENDPOINT, s.ADMIRALTY_API_KEY)
#         print(api_reader.get_tidal_events(s.HAMMERSMITH_BRIDGE_STATION_ID))
#         self.assertTrue(True)
