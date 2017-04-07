from sickle import Sickle
import sys, json
from argparse import ArgumentParser
import logging
import requests




# date=sys.argv[1]

log = logging.getLogger(__name__)
logging.basicConfig(level="DEBUG")


newFile=open('ETD_'+'2'+'.xml','w')
def main():

    sickle = Sickle('http://arizona.openrepository.com/arizona/oai/request?')
    # sets = sickle.ListSets()

    recs = sickle.ListRecords(**{'metadataPrefix':'oai_dc','set':'com_10150_129649','from':'2017-04-05'})
    log.debug("Making request to {}".format(recs))
    try:
        response = recs
    except Exception as e:
        log.exception("An error occured in issuing the request!")
        raise
    log.debug("Request completed")
    # log.debug("Response Code: {}".format(response.status_code))
    # log.debug("Response text: {}".format(response.text))
    log.debug("Trying to convert response to JSON...")
    try:
        response = response
        log.debug("Response successfully converted to JSON: {}".format(response))
    except Exception as e:
        log.exception("An error occured!")
        raise


    # print(recs.url)
    newFile.write('<OAI-PMH xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:oai_dc="http://www.openarchives.org/OAI/2.0/" xmlns:oai_dc="http://www.openarchives.org/OAI/2.0/oai_dc/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">')
    for r in recs:
        newR = str(r).encode('utf8')
        newFile.write(str(newR))
        newFile.write('</OAI-PMH>')


if __name__ == '__main__':
    main()
