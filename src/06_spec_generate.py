import json
import os
from groq import Groq

MODEL_NAME = "meta-llama/llama-4-scout-17b-16e-instruct"

PERSONAS_FILE = "personas/personas_auto.json"
OUTPUT_FILE = "spec/spec_auto.md"


def load_personas(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


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
                "content": "Return markdown only. Do not use code fences."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content


def generate_spec(personas):
    prompt = f"""
You are helping with software requirements engineering for MindDoc, a mental health support and mood tracking app.

Given these personas:
{json.dumps(personas, ensure_ascii=False, indent=2)}

Generate a structured specification in markdown.

Requirements:
- Write at least 10 requirements
- Every requirement must be appropriate for a mental health app
- Do NOT mention workouts, exercise, calories, meals, fitness tracking, or sports
- Each requirement must include:
  - Requirement ID
  - Description
  - Source Persona
  - Traceability
  - Acceptance Criteria

Use this exact format for each requirement:

# Requirement ID: FR_auto_1
- Description: [The system shall ...]
- Source Persona: [Persona Name]
- Traceability: [Derived from review group X]
- Acceptance Criteria: [Given ..., When ..., Then ...]

Make the requirements specific and testable.
Return only markdown.
"""
    return call_groq(prompt)


def save_spec(text, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    print("Loading personas...")
    personas = load_personas(PERSONAS_FILE)

    print("Generating automated specification...")
    spec = generate_spec(personas)

    save_spec(spec, OUTPUT_FILE)

    print("Done.")
    print(f"Saved spec to {OUTPUT_FILE}")
