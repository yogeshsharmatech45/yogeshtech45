from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

system_prompt = """You are a sentiment analysis expert.
Analyse the sentiment of the given text and reply in this format:
Sentiment: Positive / Neutral / Negative
Confidence: <0-100>%
Reason: <one short sentence>"""

while True:
    text = input("\nEnter text (or 'quit' to exit): ")
    if text.lower() == "quit":
        break

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        max_tokens=100,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ]
    )

    print(response.choices[0].message.content)