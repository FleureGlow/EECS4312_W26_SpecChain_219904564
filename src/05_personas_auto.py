import json
import os
from groq import Groq

MODEL_NAME = "meta-llama/llama-4-scout-17b-16e-instruct"

INPUT_FILE = "data/reviews_clean.jsonl"
GROUPS_OUTPUT = "data/review_groups_auto.json"
PERSONAS_OUTPUT = "personas/personas_auto.json"
PROMPT_FILE = "prompts/prompt_auto.json"

MAX_REVIEWS_FOR_PROMPT = 120


def load_clean_reviews(path):
    reviews = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            reviews.append(json.loads(line))
    return reviews


def load_prompts(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def sample_reviews(reviews, limit=120):
    return reviews[:limit]


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
                "content": "Return only valid JSON. Do not include markdown fences."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content


def generate_review_groups(clean_reviews, grouping_prompt):
    review_payload = [
        {
            "review_id": r["review_id"],
            "cleaned_text": r["cleaned_text"]
        }
        for r in clean_reviews
    ]

    prompt = (
        f"{grouping_prompt}\n\n"
        f"Here are the cleaned reviews:\n"
        f"{json.dumps(review_payload, ensure_ascii=False, indent=2)}\n\n"
        f"Return a JSON array with exactly 5 groups."
    )

    raw_output = call_groq(prompt)
    return json.loads(raw_output)


def generate_personas(review_groups, persona_prompt):
    prompt = (
        f"{persona_prompt}\n\n"
        f"Here are the review groups:\n"
        f"{json.dumps(review_groups, ensure_ascii=False, indent=2)}\n\n"
        f"Return a JSON array with one persona per group."
    )

    raw_output = call_groq(prompt)
    return json.loads(raw_output)


def save_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    print("Loading cleaned reviews...")
    reviews = load_clean_reviews(INPUT_FILE)

    print("Loading prompts...")
    prompts = load_prompts(PROMPT_FILE)

    sampled_reviews = sample_reviews(reviews, MAX_REVIEWS_FOR_PROMPT)

    print("Generating automated review groups...")
    review_groups = generate_review_groups(
        sampled_reviews,
        prompts["review_grouping_prompt"]
    )
    save_json(review_groups, GROUPS_OUTPUT)

    print("Generating automated personas...")
    personas = generate_personas(
        review_groups,
        prompts["persona_generation_prompt"]
    )
    save_json(personas, PERSONAS_OUTPUT)

    print("Done.")
    print(f"Saved review groups to {GROUPS_OUTPUT}")
    print(f"Saved personas to {PERSONAS_OUTPUT}")

