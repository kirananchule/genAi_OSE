from google import genai

client = genai.Client(api_key="AIzaSyA7JYtN2KUGpOzlNfFoS1tle9VRETJ9S1Y")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)