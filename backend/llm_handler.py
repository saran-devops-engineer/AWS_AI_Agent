# === File: backend/llm_handler.py ===
import requests
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
LLAMA_MODEL = "meta-llama/llama-3-8b-instruct"

def get_llm_response(message: str) -> str:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": LLAMA_MODEL,
        "messages": [
            {"role": "user", "content": message}
        ]
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=payload, headers=headers)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print("❌ LLM Error:", str(e))
        return None

def extract_aws_task(text: str) -> str:
    if "unused eip" in text.lower():
        return "list_unused_eips"
    return None
