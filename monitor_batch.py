import time
import anthropic
from dotenv import load_dotenv
load_dotenv()

client = anthropic.Anthropic()

MESSAGE_BATCH_ID = "msgbatch_01QJyuavFwbPj39J88rR3GZb"

message_batch = None
while True:
    message_batch = client.messages.batches.retrieve(MESSAGE_BATCH_ID)
    if message_batch.processing_status == "ended":
        break

    print(f"Batch {MESSAGE_BATCH_ID} is still processing...")
    time.sleep(60)
print(message_batch)