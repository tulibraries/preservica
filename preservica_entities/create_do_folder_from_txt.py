# This script creates digital object folders in Preservica based on input from a tab-delimited text file
# To use this script, create a tab-delimited text file called "create_do_folder.txt" and save it in the same directory from which you are running this script
# The text file should have 4 columns, with the following headers: title, description, security_tag, and folder_reference
# - title should contain the desired xip.title of the new folder
# - description should contain the desired xip.description of the new folder
# - security_tag should contain one of the Preservica security options: open, onsite, public, or restricted
# - folder_reference should contain the Preservica xip.reference of the desired parent folder for the new folder
# You will also need the XML metadata file "LegacyXIP_accessionRef_catalog.xml" in the same directory from which you are running this script


from pyPreservica import *
client = EntityAPI()
import csv

# Read a tab-delimited text file
with open('create_do_folder.txt', 'r') as file:
    reader = csv.DictReader(file, delimiter='\t')

    # Iterate through each row in the file
    for row in reader:
        # Extract values from the row
        title = row['title']
        description = row['description']
        security_tag = row['security_tag']
        folder_reference = row['folder_reference']

        # Create a new folder using the Preservica API
        folder = client.folder(folder_reference)
        new_folder = client.create_folder(title, description, security_tag, folder_reference)
        # add identifier type=code with the same value as the description field
        client.add_identifier(new_folder, "code", description)
        # add Legacy XIP metadata fragment based on external XML file
        with open("LegacyXIP_accessionRef_catalog.xml", 'r', encoding="UTF-8") as md:
            folder = client.add_metadata(folder, "http://preservica.com/LegacyXIP", md)
        print(new_folder.reference)
        
        # Assert parent folder reference
        assert new_folder.parent == folder.reference
