import os
import openai
import AccessKeys

#openai.organization = "org-UyKsO5lj2gVRNP6YefxZPkTs"
openai.api_key = os.getenv("OPENAI_API_KEY")

#prompt = input("Enter your promt: ")

promt = """
"""

#code-davinci-002 - free because in beta
#text - costs money
response = openai.Completion.create(
model="code-davinci-002",
prompt=promt,
temperature=0,
max_tokens=200,
top_p=1,
frequency_penalty=0,
presence_penalty=0
)

print(response["choices"][0]["text"])