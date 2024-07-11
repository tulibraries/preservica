# This script moves Preservica assets to new folders based on input from a tab-delimited text file
# To use this script, create a tab-delimited text file called "move_asset.txt" and save it in the same directory from which you are running this script
# The text file should have 2 columns: asset_to_move and destination_folder
# - asset_to_move should contain the xip.reference of the asset you would like to move
# - destination_folder should contain the xip.reference of the desired parent folder


from pyPreservica import *
client = EntityAPI()
import csv

# Read a tab-delimited text file
with open('move_asset.txt', 'r') as file:
    reader = csv.DictReader(file, delimiter='\t')

    # Iterate through each row in the file
    for row in reader:
        # Extract values from the row
        asset_to_move = row['asset_to_move']
        destination_folder = row['destination_folder']

        # Move folder using the Preservica API
        asset = client.asset(asset_to_move)
        dest_folder = client.folder(destination_folder)
        client.move(asset, dest_folder)