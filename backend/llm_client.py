import requests
import os

API_KEY = os.getenv("OPENROUTER_API_KEY") or "your_openrouter_api_key_here"
LLAMA_API_URL = "https://openrouter.ai/api/v1/chat/completions"


def query_llama(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(LLAMA_API_URL, json=data, headers=headers)
        response.raise_for_status()
        res_json = response.json()

        # Ensure response has the expected format
        if "choices" in res_json and len(res_json["choices"]) > 0:
            return res_json["choices"][0]["message"]["content"]
        else:
            return "❌ LLM did not return a valid response."
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return "❌ Request to LLM API failed."
    except ValueError as ve:
        print(f"Response parsing error: {ve}")
        print("Raw response text:", response.text)
        return "❌ Failed to parse LLM response."
