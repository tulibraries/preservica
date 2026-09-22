# This script deletes metadata object(s) from Preservica assets in batch
# To use this script, create a tab-delimited text file called "delete_metadata_asset.txt" and save it in the same directory from which you are running this script
# The text file should have 2 columns, with the following headers: asset_reference, metadata_schema
# - asset_reference should contain the Preservica xip.reference of the asset from which you would like to delete metadata
# - metadata_schema should contain the schema of the metadata object you would like to delete
# -- example schemas:
# --- http://www.preservica.com/archives_space/v1
# --- http://preservica.com/LegacyXIP
# --- http://www.openarchives.org/OAI/2.0/oai_dc/

from pyPreservica import *
client = EntityAPI()
import csv

# Read a tab-delimited text file
with open('delete_metadata_asset.txt', 'r') as file:
    reader = csv.DictReader(file, delimiter='\t')

    # Iterate through each row in the file
    for row in reader:
        # Extract values from the row
        asset_reference = row['asset_reference']
        metadata_schema = row['metadata_schema']

        # Delete metadata object using the Preservica API
        asset = client.asset(asset_reference)
        client.delete_metadata(asset, metadata_schema)
