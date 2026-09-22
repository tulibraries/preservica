# This script deletes metadata object(s) from Preservica folders in batch
# To use this script, create a tab-delimited text file called "delete_metadata_folder.txt" and save it in the same directory from which you are running this script
# The text file should have 2 columns, with the following headers: folder_reference, metadata_schema
# - folder_reference should contain the Preservica xip.reference of the folder from which you would like to delete metadata
# - metadata_schema should contain the schema of the metadata object you would like to delete
# -- example schemas:
# --- http://www.preservica.com/archives_space/v1
# --- http://preservica.com/LegacyXIP
# --- http://www.openarchives.org/OAI/2.0/oai_dc/

from pyPreservica import *
client = EntityAPI()
import csv

# Read a tab-delimited text file
with open('delete_metadata_folder.txt', 'r') as file:
    reader = csv.DictReader(file, delimiter='\t')

    # Iterate through each row in the file
    for row in reader:
        # Extract values from the row
        folder_reference = row['folder_reference']
        metadata_schema = row['metadata_schema']

        # Delete metadata object using the Preservica API
        folder = client.folder(folder_reference)
        client.delete_metadata(folder, metadata_schema)
