import requests
import os
from dotenv import load_dotenv

load_dotenv()

SCALEDOWN_API_KEY = os.getenv("SCALEDOWN_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

SCALEDOWN_URL = "https://api.scaledown.xyz/compress/raw/"
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"


def get_visa_guidance(country, visa_type, profile):

    # -------- SCALE DOWN --------
    context = f"""
You are an expert immigration assistant.

Country: {country}
Visa Type: {visa_type}
Applicant: {profile}
STRICT RULES:
- Do NOT use ** or markdown
- Do NOT use bullet symbols like *
- Use only plain text


Return:
Eligibility
Documents
Steps
Processing Time
Tips
"""

    prompt = f"{visa_type} visa process for {country}"

    scaledown_payload = {
        "context": context,
        "prompt": prompt,
        "model": "gpt-4o",
        "scaledown": {"rate": "auto"}
    }

    scaledown_headers = {
        "x-api-key": SCALEDOWN_API_KEY,
        "Content-Type": "application/json"
    }

    try:
        sd_res = requests.post(
            SCALEDOWN_URL,
            headers=scaledown_headers,
            json=scaledown_payload
        )

        sd_data = sd_res.json()
        compressed_prompt = sd_data["results"]["compressed_prompt"]

    except Exception as e:
        return f"ScaleDown error: {str(e)}"

    # -------- GROQ --------
    groq_headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    groq_payload = {
        "model": "llama-3.1-8b-instant",   # ✅ FIXED MODEL
        "messages": [
            {"role": "user", "content": compressed_prompt}
        ],
        "temperature": 0.7
    }

    try:
        g_res = requests.post(GROQ_URL, headers=groq_headers, json=groq_payload)
        g_data = g_res.json()

        if "choices" not in g_data:
            return f"Groq API error: {g_data}"

        final_answer = g_data["choices"][0]["message"]["content"]
        return final_answer

    except Exception as e:
        return f"Groq request failed: {str(e)}"
