import os
import dotenv
from openai import AzureOpenAI

dotenv.load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_APIM_ENDPOINT"),
    api_key=os.getenv("AZURE_APIM_API_KEY"),
    api_version="2023-12-01-preview",
    default_headers={
    "Application-Name": "app one",  
    "Application-Number": "1",
    "Business-Unit": "Data Science",
    }
)

response = client.chat.completions.create(
    model="gpt-35-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant for Data Science employees."},
        {"role": "user", "content": "What do data scientist do?"}
    ],


)
print(response)
