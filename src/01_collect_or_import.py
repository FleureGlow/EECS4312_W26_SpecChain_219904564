"""imports or reads your raw dataset; if you scraped, include scraper here"""

from google_play_scraper import reviews, Sort
import json

# App ID for MindDoc (Google Play)
APP_ID = "com.minddoc.app"

# Number of reviews you want (try 1500–3000)
NUM_REVIEWS = 1500

def collect_reviews():
    all_reviews = []
    count = 0
    continuation_token = None

    while count < NUM_REVIEWS:
        result, continuation_token = reviews(
            APP_ID,
            lang='en',
            country='ca',
            sort=Sort.NEWEST,
            count=200,
            continuation_token=continuation_token
        )

        if not result:
            break

        for r in result:
            review = {
                "review_id": str(r.get("reviewId")),
                "rating": r.get("score"),
                "date": str(r.get("at")),
                "text": r.get("content")
            }
            all_reviews.append(review)
            count += 1

            if count >= NUM_REVIEWS:
                break

    return all_reviews


def save_reviews(reviews_list):
    with open("data/reviews_raw.jsonl", "w", encoding="utf-8") as f:
        for r in reviews_list:
            f.write(json.dumps(r) + "\n")


if __name__ == "__main__":
    print("Collecting reviews...")
    data = collect_reviews()
    save_reviews(data)
    print(f"Saved {len(data)} reviews to data/reviews_raw.jsonl")
