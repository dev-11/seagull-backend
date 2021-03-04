from services import service_factory


def lambda_handler(event, context):

    instance = service_factory.tidal_service_instance()

    return {'statusCode': 200, 'body': [_.to_dict() for _ in instance.get_tidal_data()]}
