
import uuid
from orchestrator import Orchestrator
import logging
from dotenv import load_dotenv
import os
import aiohttp

import time
from pprint import pprint
logging.basicConfig(filename="test.log", filemode="w", level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')


start = time.time()

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')
TENANT_NAME = os.getenv('TENANT_NAME')
PRE_FOLDER_ID = os.getenv('PRE_FOLDER_ID')
MACHINE_IDENTIFIER = os.getenv('MACHINE_IDENTIFIER')

client = Orchestrator(client_id=CLIENT_ID, refresh_token=REFRESH_TOKEN, tenant_name=TENANT_NAME)

folder = client.get_folder_by_id(int(PRE_FOLDER_ID))

queue = folder.get_queue_by_id(116803)


res = queue.check_duplicate(endpoint="Comments", value="This is a comment")
print(res)
item_content = {
    "Name": "Yo",
    "Apellido": "Test"
}

batch_id = str(uuid.uuid4())
print("Empezando la transaccion")
res = queue.start(machine_identifier=MACHINE_IDENTIFIER, specific_content=item_content, reference="Name", fields={"doc_type": "updated contract"})
# pprint(res)
# time.sleep(2)
item_id = res["Id"]
print(item_id)
print("Obteniendo el item")
item = queue.get_item_by_id(item_id)
# time.sleep(2)
item.make_comment(text="This is a comment")
print("Actualizando el status")
item.set_transaction_status(success=False, reason="Some reason", details="Some details", exception_type="Retried")
# pprint(res2)

end = time.time()
