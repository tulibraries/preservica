# This script retrieves Preservica xip.reference identifiers for the children of a given Preservica folder and prints them to a .tsv file
# Replace PRESERVICA_REF with the xip.reference of the parent folder
# Change the filename of the output file if desired

from pyPreservica import *
client = EntityAPI()
import csv

with open("output.tsv", "a", newline='') as f:
    tsv_writer = csv.writer(f, delimiter='\t')
    for entity in client.descendants("PRESERVICA_REF"):
        tsv_writer.writerow([entity.reference, entity.title])