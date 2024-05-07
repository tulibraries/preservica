# This script prints each entity.reference and entity.title contained in Preservica's "pending" folder to a .tsv file

from pyPreservica import *
client = EntityAPI()
import csv

with open("pending_output.tsv", "a", newline='') as f:
    tsv_writer = csv.writer(f, delimiter='\t')
    tsv_writer.writerow(['entity_reference', 'entity_title'])
    for entity in client.descendants("92b47238-23d7-43fd-aac3-cdf34d5562f9"):
        tsv_writer.writerow([entity.reference, entity.title])