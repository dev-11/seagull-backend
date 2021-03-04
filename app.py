from entry_point.app import lambda_handler


def main():
    event = {
      "params": {
        "header": {
          "X-seagull-location": "ChiswickEyot"
        }
      }
    }

    print(lambda_handler(event, None))


if __name__ == "__main__":
    main()
