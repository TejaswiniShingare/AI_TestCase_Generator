import os
import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

client = OpenAI(
base_url="https://models.inference.ai.azure.com",
api_key=GITHUB_TOKEN
)

def call_ai(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content


def call_ai_json(prompt):
    response_text = call_ai(prompt)

    try:
        return json.loads(response_text)

    except Exception as e:
        print("\nUnable to parse JSON response")
        print(e)

        print("\nRaw Response:")
        print(response_text)

        return []
