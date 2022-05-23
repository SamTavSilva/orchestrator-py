from pyrsistent import v
from orchestrator.orchestrator import Orchestrator
import logging
from dotenv import load_dotenv
import os
from pprint import pprint
import json
import logging

logging.basicConfig(filename="test.log", filemode="w", level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')
TENANT_NAME = os.getenv('TENANT_NAME')
FOLDER_ID = os.getenv('FOLDER_ID')
QUEUE_ID = os.getenv('QUEUE_ID')
ITEM_ID = os.getenv('ITEM_ID')
PRE_FOLDER_ID = os.getenv('PRE_FOLDER_ID')
PROD_FOLDER_ID = os.getenv('PROD_FOLDER_ID')
print(PROD_FOLDER_ID)

client = Orchestrator(client_id=CLIENT_ID, refresh_token=REFRESH_TOKEN, tenant_name=TENANT_NAME)
# print(client)
# pprint(client.get_folder_ids())
folder = client.get_folder_by_id(int(PRE_FOLDER_ID))
queue = folder.get_queue_by_id(116803)
items = queue.get_queue_items_by_status(status="Successful")
# pprint(items)
print(len(items))
res = queue.check_duplicate(reference="127101069#6a224d58-eb4b-4fcc-98c9-c644ca4a8302")
# need to pass part of the reference as key
filt = queue.get_queue_items(options={"$filter": "contains(Reference,'127101069')"})
print(filt[0].specific_content)
