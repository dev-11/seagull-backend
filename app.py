from services import service_factory


def main():
    instance = service_factory.tidal_service_instance()
    print(instance.get_tidal_data())


if __name__ == "__main__":
    main()
