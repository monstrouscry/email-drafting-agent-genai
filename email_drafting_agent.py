import asyncio
from typing import Annotated
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext
from openai import OpenAI
import os

# ✅ Set your OpenAI API Key as an environment variable before running
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Your Agent Token
AGENT_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMWE0OTE5Zi0zZmU3LTQyN2EtYTU1OS0xY2ZiZDBmNjRiMWMiLCJleHAiOjI1MzQwMjMwMDc5OSwidXNlcl9pZCI6IjFmMjVkYWY0LWNmMTEtNDUxMC1hNGE4LTI3NzU5MTQ4NjBiNyJ9.DHAKRYqpnRNC2X9Td4xAzh69o3hrT8zxcNRs5ERx-jI"
session = GenAISession(jwt_token=AGENT_JWT)

# 📄 Email Generation Prompt Template
EMAIL_PROMPT = (
    "You are a professional email drafting assistant. Based on the bullet points below, generate a complete email.\n\n"
    "Bullet Points:\n{bullet_points}\n\n"
    "The email should include:\n"
    "- A relevant subject line\n"
    "- A professional greeting\n"
    "- A concise and informative body\n"
    "- A polite closing\n\n"
    "Return the complete email."
)


@session.bind(
    name="email_drafting_agent",
    description="Creates emails from bullet-style input"
)
async def email_drafting_agent(
    agent_context: GenAIContext,
    bullet_points: Annotated[
        str,
        "Provide bullet-point style notes: recipient, purpose, details."
    ],
):
    """Creates emails from bullet-style input"""

    try:
        prompt = EMAIL_PROMPT.format(bullet_points=bullet_points)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful email assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=400
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Email generation failed: {str(e)}"


async def main():
    print(f"✅ Email Drafting Agent started with token: {AGENT_JWT[:10]}...")
    await session.process_events()

if __name__ == "__main__":
    asyncio.run(main())
