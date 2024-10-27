from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_email(prompt, model_id):
    response = client.chat.completions.create(
        model=model_id,  # Placeholder for your fine-tuned model ID
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )
    return response.choices[0].message.content  # Fixed syntax error here

# Example usage
prompt = "Write a cold email for a software developer role, showing genuine interest in the company and including a specific call to action."
email_content = generate_email(prompt, "YOUR_MODEL_ID")  # Placeholder for model ID
with open("generated_email.txt", "w") as file:
    file.write(email_content)
