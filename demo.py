import openai

response = openai.images.generate(
    prompt="Tom Cruise",
    n=1,
    size="256x256"
)

print(response.data[0].url)