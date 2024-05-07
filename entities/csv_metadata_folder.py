#This script adds Dublin Core metadata to already ingested folders in Preservica, via a csv file
#To use this script, create a csv file called "dublincore.csv"
#The first column should have a header of "folderID"
#Additional columns should have headers for metadata elements prefixed by dc:
#The folderID column should contain Preservica xip.references for the folders to be updated

import xml
import csv
from pyPreservica import *

OAI_DC = "http://www.openarchives.org/OAI/2.0/oai_dc/"
DC = "http://purl.org/dc/elements/1.1/"
XSI = "http://www.w3.org/2001/XMLSchema-instance"

entity = EntityAPI()

headers = list()
with open('dublincore-folders.csv', encoding='utf-8-sig', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        for header in row:
            headers.append(header)
        break
    if 'folderId' in headers:
        for row in reader:
            folderID = None
            xml_object = xml.etree.ElementTree.Element('oai_dc:dc', {"xmlns:oai_dc": OAI_DC, "xmlns:dc": DC, "xmlns:xsi": XSI})
            for value, header in zip(row, headers):
                if header.startswith('dc:'):
                    xml.etree.ElementTree.SubElement(xml_object, header).text = value
                elif header.startswith('folderId'):
                    folderID = value
            xml_request = xml.etree.ElementTree.tostring(xml_object, encoding='utf-8', xml_declaration=True).decode('utf-8')
            folder = entity.folder(folderID)
            entity.add_metadata(folder, OAI_DC, xml_request)
    else:
        print("The CSV file should contain a folderId column containing the Preservica identifier for the folder to be updated")