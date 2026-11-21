import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from prompt import SYSTEM_PROMPT

load_dotenv()

def get_ai_response(user_prompt: str, conversation=None) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is missing. Add it to your .env file."
        )

    model = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
    client = genai.Client(api_key=api_key)

    history_text = ""
    if conversation:
        recent = conversation[-8:]
        history_text = "\n".join(
            f'{item["role"].upper()}: {item["content"]}' for item in recent
        )

    full_prompt = (
        f"{SYSTEM_PROMPT}\n\n"
        f"Recent conversation (for context only):\n{history_text}\n\n"
        f"USER QUESTION:\n{user_prompt}"
    )

    response = client.models.generate_content(
        model=model,
        contents=full_prompt,
        config=types.GenerateContentConfig(
            temperature=0.2,
            max_output_tokens=700,
        ),
    )
    if not response.text:
        return (
            "I couldn't produce a response. Please rephrase your question "
            "or consult a qualified healthcare professional."
        )
    return response.text
