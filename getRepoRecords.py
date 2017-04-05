from sickle import Sickle
import sys
date=sys.argv[1]

newFile=open('ETD_'+date+'.xml','w')
def main():
    sickle = Sickle('http://arizona.openrepository.com/arizona/oai/request?')
    sets = sickle.ListSets()

    recs = sickle.ListRecords(**{'metadataPrefix':'oai_dc','set':'com_10150_129649','from':date})
    newFile.write('<OAI-PMH xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:ns0="http://www.openarchives.org/OAI/2.0/" xmlns:ns2="http://www.openarchives.org/OAI/2.0/oai_dc/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">')
    for r in recs:
        newFile.write(str(r))
    newFile.write('</OAI-PMH>')

if __name__ == '__main__':
    main()
