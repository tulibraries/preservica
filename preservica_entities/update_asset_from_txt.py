# This script updates metadata for assets in Preservica based on input from a tab-delimited text file
# To use this script, create a tab-delmited text file called "update_asset.txt" and save it in the same directory from which you are running this script
# The text file should have 3 columns, with the following headers: asset_reference, new_description, and new_identifier
# - folder_reference should contain the Preservica xip.reference of the asset to be updated
# - new_description should contain the desired value of the xip.description field
# - new_identifier should contain the desired value of the identifier (type=code) field (generally this will be the same value as xip.description)
# You will also need the XML metadata file "LegacyXIP_accessionRef_catalog.xml" in the same directory from which you are running this script


from pyPreservica import *
client = EntityAPI()
import csv

# Read a tab-delimited text file
with open('update_asset.txt', 'r') as file:
    reader = csv.DictReader(file, delimiter='\t')

    # Iterate through each row in the file
    for row in reader:
        # Extract values from the row
        asset_reference = row['asset_reference']
        new_description = row['new_description']
        new_identifier = row['new_identifier']

        # Update each asset: delete existing identifiers and Legacy XIP, replace description & identifier, add new Legacy XIP fragment
        asset = client.asset(asset_reference)
        client.delete_identifiers(asset)
        client.delete_metadata(asset, "http://preservica.com/LegacyXIP")
        asset.description = new_description
        asset = client.save(asset)
        client.add_identifier(asset, "code", new_identifier)
        with open("LegacyXIP_accessionRef_catalog.xml", 'r', encoding="UTF-8") as md:
        	asset = client.add_metadata(asset, "http://preservica.com/LegacyXIP", md)