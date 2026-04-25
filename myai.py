from openai import OpenAI 
client = OpenAI( api_key="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", base_url="https://openrouter.ai/api/v1" ) 
# System prompt = gives AI a role/personality 
system_prompt = """You are a helpful Python tutor for beginners. Explain everything in simple words. Always give a short code example with your answer. Never use difficult jargon.""" 
user_question = input("Ask your Python question: ") 
response = client.chat.completions.create( model="openai/gpt-oss-120b:free", messages=[ {"role": "system", "content": system_prompt}, {"role": "user", "content": user_question} ] , max_tokens=10  )
print(response.choices[0].message.content)