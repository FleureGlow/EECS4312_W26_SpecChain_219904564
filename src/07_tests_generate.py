import json
import os
from groq import Groq

MODEL_NAME = "meta-llama/llama-4-scout-17b-16e-instruct"

SPEC_FILE = "spec/spec_auto.md"
OUTPUT_FILE = "tests/tests_auto.json"


def load_spec(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def call_groq(prompt):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable is not set.")

    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "Return only valid JSON. Do not use markdown fences."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content


def generate_tests(spec_text):
    prompt = f"""
You are generating validation tests for MindDoc, a mental health support and mood tracking app.

Given this specification:
{spec_text}

Generate validation tests in JSON.

Rules:
- Each requirement must have at least 1 test scenario
- Prefer 2 test scenarios per requirement when possible
- Each test object must include:
  - test_id
  - requirement_id
  - scenario
  - steps
  - expected_result
- Return only a JSON array
- Do not include explanations

Example format:
[
  {{
    "test_id": "T_auto_1",
    "requirement_id": "FR_auto_1",
    "scenario": "User logs daily mood successfully",
    "steps": [
      "Open the app",
      "Navigate to the mood tracking section",
      "Select a mood and submit"
    ],
    "expected_result": "The mood entry is saved successfully."
  }}
]
"""
    return call_groq(prompt)


def save_tests(json_text, path):
    data = json.loads(json_text)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    print("Loading automated specification...")
    spec_text = load_spec(SPEC_FILE)

    print("Generating automated tests...")
    tests_json = generate_tests(spec_text)

    print("Saving automated tests...")
    save_tests(tests_json, OUTPUT_FILE)

    print("Done.")
    print(f"Saved tests to {OUTPUT_FILE}")
