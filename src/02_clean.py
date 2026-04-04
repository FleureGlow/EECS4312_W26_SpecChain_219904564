"""cleans raw data & make clean dataset"""

import json
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def clean_text(text):
    if not text:
        return ""

    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    words = text.split()
    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words and len(word) > 2
    ]

    return " ".join(words)


def load_and_clean_reviews():
    cleaned_reviews = []
    seen_texts = set()

    with open("data/reviews_raw.jsonl", "r", encoding="utf-8") as f:
        for line in f:
            review = json.loads(line)
            raw_text = review.get("text", "").strip()

            if not raw_text:
                continue

            if len(raw_text) < 10:
                continue

            if raw_text in seen_texts:
                continue

            seen_texts.add(raw_text)

            cleaned_text = clean_text(raw_text)

            if not cleaned_text:
                continue

            cleaned_reviews.append({
                "review_id": review.get("review_id"),
                "rating": review.get("rating"),
                "date": review.get("date"),
                "cleaned_text": cleaned_text
            })

    return cleaned_reviews


def save_cleaned_reviews(cleaned_reviews):
    with open("data/reviews_clean.jsonl", "w", encoding="utf-8") as f:
        for review in cleaned_reviews:
            f.write(json.dumps(review, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    print("Cleaning reviews...")
    cleaned_reviews = load_and_clean_reviews()
    save_cleaned_reviews(cleaned_reviews)
    print(f"Saved {len(cleaned_reviews)} cleaned reviews to data/reviews_clean.jsonl")
