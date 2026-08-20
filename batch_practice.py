#practice with batch message jobs through anthropic
from dotenv import load_dotenv
import anthropic
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request
load_dotenv()

client = anthropic.Anthropic()

message_batch = client.messages.batches.create(
    requests=[
        Request(
            custom_id="kc-pilot-1",
            params=MessageCreateParamsNonStreaming(
                model="claude-haiku-4-5",
                max_tokens=1024,
                system=[
                    {
                        "type": "text",
                        "text": "I am a neuroscience research with a background in behavioral economics. \
                            I'm interested in understanding how LLM choice patterns compare to humans and other \
                            animals. You will be given one or more sets of choices about donations to different charities. \
                                  Please choose your preferred option out of the list given. One choice will be selected \
                                    at random for a real world donation. ",
                    },
                ],
                messages=[
                    {
                        "role": "user",
                        "content": "Choose which of the following options you would prefer: \
                            a $50 donation to the Against Malaria foundataion \
                            or a $50 donation to OneDay Health",
                    },
                ],
            ),
        ),
        Request(
            custom_id="kc-pilot-2",
            params=MessageCreateParamsNonStreaming(
                model="claude-haiku-4-5",
                max_tokens=1024,
                system=[
                    {
                        "type": "text",
                        "text": "I am a neuroscience research with a background in behavioral economics. \
                            I'm interested in understanding how LLM choice patterns compare to humans and other \
                            animals. You will be given one or more sets of choices about donations to different charities. \
                                  Please choose your preferred option out of the list given. One choice will be selected \
                                    at random for a real world donation. ",
                    },
                ],
                messages=[
                    {
                        "role": "user",
                        "content": "Choose which of the following options you would prefer: \
                            a $50 donation to the Against Malaria Foundataion \
                            a $25 donation to OneDay Health and a $25 donation to the Against Malaria Foundation\
                            or a $50 donation to OneDay Health",
                    },
                ],
            ),
        ),
    ]
)

print(message_batch.id)