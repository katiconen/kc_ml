import anthropic
from dotenv import load_dotenv
load_dotenv()

client = anthropic.Anthropic()

MESSAGE_BATCH_ID = "msgbatch_01QJyuavFwbPj39J88rR3GZb"

# Stream results file in memory-efficient chunks, processing one at a time
for result in client.messages.batches.results(
    MESSAGE_BATCH_ID,
):
    match result.result.type:
        case "succeeded":
            print(f"Success! {result.custom_id} {result.result}")
        case "errored":
            if result.result.error.error.type == "invalid_request_error":
                # Request body must be fixed before re-sending request
                print(f"Validation error {result.custom_id}")
            else:
                # Request can be retried directly
                print(f"Server error {result.custom_id}")
        case "expired":
            print(f"Request expired {result.custom_id}")