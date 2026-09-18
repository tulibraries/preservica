##To use this script, create separate config.py file with ASpace API authentication credentials:
##
##ASpace_baseURL=''
##ASpace_user = ''
##ASpace_pw = ''
##

import config
import requests
import csv

# ASpace Resource variables
ASpace_repository = '' #populate with repository ID: 3 (test) or 4 (main)
archival_object_id = '' #populate with archival object ID (e.g., '237685' for archival_object_237685)

# Authenticate with the ASpace API
auth = requests.post(
    f'{config.ASpace_baseURL}/users/{config.ASpace_user}/login?password={config.ASpace_pw}'
).json()
session = auth['session']
headers = {'X-ArchivesSpace-Session': session, 'Content-Type': 'application/json'}

# Get archival object children
output_ao_children = requests.get(
    f"{config.ASpace_baseURL}/repositories/{ASpace_repository}/archival_objects/{archival_object_id}/children",
    headers=headers
).json()

if output_ao_children:
    with open('output_ao_children.tsv', 'w', newline='', encoding="utf-8") as f:
        tsv_writer = csv.writer(f, delimiter='\t')
        tsv_writer.writerow(['ref_id', 'title', 'uri', 'top_container', 'folder_type', 'folder_number'])  # header

        for child in output_ao_children:
            ref_id = child.get('ref_id', '')
            title = child.get('title', '')
            uri = child.get('uri', '')
            top_container_display = ''
            type_2 = ''
            indicator_2 = ''

            # Look for top_container reference in instances
            instances = child.get('instances', [])
            for inst in instances:
                sub_container = inst.get('sub_container')
                if sub_container and 'top_container' in sub_container:
                    # sub_container fields (folder type and number)
                    type_2 = sub_container.get('type_2', '')
                    indicator_2 = sub_container.get('indicator_2', '')
                    top_container_ref = sub_container['top_container']['ref']
                    top_container = requests.get(
                        f"{config.ASpace_baseURL}{top_container_ref}",
                        headers=headers
                    ).json()

                    top_container_display = top_container.get('display_string', '')
                    break  # Use the first container found

            tsv_writer.writerow([ref_id, title, uri, top_container_display, type_2, indicator_2])