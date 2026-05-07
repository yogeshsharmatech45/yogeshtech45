
import ollama

client = ollama.Client()

model = "llama3"

prompt = "What is the capital of France?"

response = client.generate(model=model, prompt=prompt)

print(response.response)