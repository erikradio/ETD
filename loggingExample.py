import logging
import requests
from argparse import ArgumentParser
from json import dumps

log = logging.getLogger(__name__)
logging.basicConfig(level="DEBUG")

def main():
    log.debug("Parsing arguments")
    parser = ArgumentParser()
    parser.add_argument("target")
    args = parser.parse_args()
    log.debug("Arguments parsed: {}".format(str(args)))

    log.debug("Making request to {}".format(args.target))
    try:
        response = requests.get(args.target)
    except Exception as e:
        log.exception("An error occured in issuing the request!")
        raise
    log.debug("Request completed")
    log.debug("Response Code: {}".format(response.status_code))
    log.debug("Response text: {}".format(response.text))
    log.debug("Trying to convert response to JSON...")
    try:
        response_json = response.json()
        log.debug("Response successfully converted to JSON: {}".format(dumps(response_json)))
    except Exception as e:
        log.exception("An error occured!")
        raise


if __name__ == "__main__":
    main()
