import os
import dotenv
from openai import AzureOpenAI

dotenv.load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_APIM_ENDPOINT"),
    api_key=os.getenv("AZURE_APIM_API_KEY"),
    api_version="2023-12-01-preview",
    default_headers={
    "Application-Name": "app two",  # Add "app two" to the default headers
    "Application-Number": "2",
    "Business-Unit": "Marketing",
    }
)

response = client.chat.completions.create(
    model="gpt-35-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant for Marketing employees."},
        {"role": "user", "content": "Where did Marketing within businesses originate from?"}
    ],


)
print(response)
