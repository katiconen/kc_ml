# practice with LLM API calls
# practice with LLM API calls
from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

message = client.messages.create(
    model = "claude-haiku-4-5",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What tasks are used to study phenomena like range dependence, loss aversion, \
                framing effects, IIA violations, and discounting in behavioral economics",
        }
    ],
)

for block in message.content:
    if block.type == "text":
        print(block.text)


