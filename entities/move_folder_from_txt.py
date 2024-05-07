# This script moves Preservica folders to new folders based on input from a tab-delimited text file
# To use this script, create a tab-delimited text file called "move_folder.txt" and save it in the same directory from which you are running this script
# The text file should have 2 columns: folder_to_move and destination_folder
# - folder_to_move should contain the xip.reference of the folder you would like to move
# - destination_folder should contain the xip.reference of the desired parent folder


from pyPreservica import *
client = EntityAPI()
import csv

# Read a tab-delimited text file
with open('move_folder.txt', 'r') as file:
    reader = csv.DictReader(file, delimiter='\t')

    # Iterate through each row in the file
    for row in reader:
        # Extract values from the row
        folder_to_move = row['folder_to_move']
        destination_folder = row['destination_folder']

        # Move folder using the Preservica API
        folder = client.folder(folder_to_move)
        dest_folder = client.folder(destination_folder)
        client.move(folder, dest_folder)