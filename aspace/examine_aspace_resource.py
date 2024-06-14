##To use this script, create separate config.py file with ASpace API authentication credentials:
##
##ASpace_baseURL=''
##ASpace_user = ''
##ASpace_pw = ''
##
##Comment out or uncomment the sections of this script that you need
##Populate the ASPACE Resource variables as needed

import config
import requests
import json
import csv

#ASPACE Resource variables
ASpace_repository =''    # ASpace_repository: 3 (test) or 4 (main) repositories
ASpace_res_id =  '' # refer to resource uri assigned by ASpace (ex. https://scrcarchivesspace.temple.edu/staff/resources/644#tree::resource_644)
archival_object_id = '' # leave blank unless restricting data to a particular series or subseries. again, refer to Aspace uri (ex. https://scrcarchivesspace.temple.edu/staff/resources/644#tree::archival_object_237685)

digital_object_id = '' # leave blank unless looking for the Digital Object JSON model. again, gather the id from the DO's uri.

auth = requests.post(f'{config.ASpace_baseURL}/users/{config.ASpace_user}/login?password={config.ASpace_pw}').json()
session = auth['session']
headers = {'X-ArchivesSpace-Session': session, 'Content_Type': 'application/json'}

ao = None
do = None
output_ao_children = None


##NEED THE RESOURCE JSON MODEL?
#ao = requests.get(config.ASpace_baseURL + '/repositories/' + ASpace_repository + '/resources/' + ASpace_res_id, headers=headers).json()


##NEED A LIST OF THE CHILDREN ARCHIVAL OBJECTS FROM A RESOURCE?
#ao=requests.get(config.ASpace_baseURL + '/repositories/' + ASpace_repository + '/resources/' + ASpace_res_id + '/ordered_records', headers = headers).json()


##NEED AN ARCHIVAL OBJECT'S JSON MODEL 
##ao = requests.get(config.ASpace_baseURL+ '/repositories/' + ASpace_repository +'/archival_objects/'+archival_object_id, headers=headers, params={'resolve[]': ['top_container']}).json()

if ao:
    print(json.dumps(ao, indent=2))


#NEED A DIGITAL OBJECT?
##do = requests.get(config.ASpace_baseURL + '/repositories/' + ASpace_repository + '/digital_objects/' +digital_object_id, headers=headers).json()
if do:
    print(json.dumps(do, indent=2))

##NEED A LIST OF THE CHILDREN ARCHIVAL OBJECTS FROM A SPECIFIC SUB/SERIES?
output_ao_children = requests.get(config.ASpace_baseURL + '/repositories/' + ASpace_repository + '/archival_objects/'+ archival_object_id +'/children', headers=headers).json() 

if output_ao_children:
    with open('output_ao_children.tsv', 'w', newline='') as f:
        tsv_writer = csv.writer(f, delimiter='\t')
        tsv_writer.writerow(['ref_id', 'title', 'uri']) #header
        for child in output_ao_children:
            tsv_writer.writerow([child['ref_id'], child['title'], child['uri']])

    #print(json.dumps(output_ao_children[0], indent=2))
    
    #for child in output_ao_children:
    #    print(child['ref_id'], child['title'], child['uri'])