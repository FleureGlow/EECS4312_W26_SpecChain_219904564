import json
import re
from pathlib import Path


BASE_DIR = Path(".")

AMBIGUOUS_WORDS = {
    "fast",
    "easy",
    "better",
    "user-friendly",
    "user friendly",
    "quick",
    "efficient",
    "simple",
    "intuitive",
    "meaningful",
    "useful",
    "small",
    "appropriate",
    "relevant",
    "personalized",
    "seamless",
    "smooth",
    "reliable",
}


def load_json(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def count_jsonl_lines(path: Path) -> int:
    count = 0
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                count += 1
    return count


def extract_requirements_from_markdown(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    pattern = re.compile(
        r"# Requirement ID:\s*(?P<req_id>[^\n]+)\n"
        r"- Description:\s*(?P<description>[^\n]+)\n"
        r"- Source Persona:\s*(?P<persona>[^\n]+)\n"
        r"- Traceability:\s*(?P<traceability>[^\n]+)\n"
        r"- Acceptance Criteria:\s*(?P<acceptance>[^\n]+)",
        re.MULTILINE,
    )

    requirements = []
    for match in pattern.finditer(text):
        requirements.append(
            {
                "requirement_id": match.group("req_id").strip(),
                "description": match.group("description").strip(),
                "persona": match.group("persona").strip(),
                "traceability": match.group("traceability").strip(),
                "acceptance_criteria": match.group("acceptance").strip(),
            }
        )

    return requirements


def count_ambiguous_requirements(requirements):
    ambiguous_count = 0

    for req in requirements:
        combined_text = (
            req["description"] + " " + req["acceptance_criteria"]
        ).lower()

        if any(word in combined_text for word in AMBIGUOUS_WORDS):
            ambiguous_count += 1

    return ambiguous_count


def get_unique_review_ids_from_groups(groups):
    review_ids = set()

    for group in groups:
        if isinstance(group, dict):
            if "review_ids" in group and isinstance(group["review_ids"], list):
                for review_id in group["review_ids"]:
                    review_ids.add(str(review_id))
            elif "reviews" in group and isinstance(group["reviews"], list):
                for review in group["reviews"]:
                    if isinstance(review, dict) and "review_id" in review:
                        review_ids.add(str(review["review_id"]))

    return review_ids


def compute_pipeline_metrics(
    reviews_clean_file: Path,
    review_groups_file: Path,
    personas_file: Path,
    spec_file: Path,
    tests_file: Path,
):
    dataset_size = count_jsonl_lines(reviews_clean_file)

    review_groups = load_json(review_groups_file)
    personas = load_json(personas_file)
    tests = load_json(tests_file)
    requirements = extract_requirements_from_markdown(spec_file)

    if not isinstance(review_groups, list):
        raise ValueError(f"{review_groups_file} must contain a JSON array.")
    if not isinstance(personas, list):
        raise ValueError(f"{personas_file} must contain a JSON array.")
    if not isinstance(tests, list):
        raise ValueError(f"{tests_file} must contain a JSON array.")

    persona_count = len(personas)
    requirements_count = len(requirements)
    tests_count = len([test for test in tests if isinstance(test, dict)])

    used_review_ids = get_unique_review_ids_from_groups(review_groups)
    review_coverage_ratio = (
        round(len(used_review_ids) / dataset_size, 3) if dataset_size > 0 else 0.0
    )

    traceable_requirements = [
        req
        for req in requirements
        if req["persona"] and req["traceability"]
    ]
    traceability_ratio = (
        round(len(traceable_requirements) / requirements_count, 3)
        if requirements_count > 0
        else 0.0
    )

    requirement_ids = {req["requirement_id"] for req in requirements}
    tested_requirement_ids = {
        test["requirement_id"]
        for test in tests
        if isinstance(test, dict) and "requirement_id" in test
    }

    testable_count = len(requirement_ids.intersection(tested_requirement_ids))
    testability_rate = (
        round(testable_count / requirements_count, 3)
        if requirements_count > 0
        else 0.0
    )

    ambiguity_count = count_ambiguous_requirements(requirements)
    ambiguity_ratio = (
        round(ambiguity_count / requirements_count, 3)
        if requirements_count > 0
        else 0.0
    )

    persona_to_requirement_links = len(traceable_requirements)
    requirement_to_test_links = sum(
        1
        for test in tests
        if isinstance(test, dict)
        and test.get("requirement_id") in requirement_ids
    )
    traceability_links = persona_to_requirement_links + requirement_to_test_links

    return {
        "dataset_size": dataset_size,
        "persona_count": persona_count,
        "requirements_count": requirements_count,
        "tests_count": tests_count,
        "traceability_links": traceability_links,
        "review_coverage_ratio": review_coverage_ratio,
        "traceability_ratio": traceability_ratio,
        "testability_rate": testability_rate,
        "ambiguity_ratio": ambiguity_ratio,
    }


def save_json(data, path: Path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def main():
    reviews_clean_file = BASE_DIR / "data" / "reviews_clean.jsonl"

    manual_metrics = compute_pipeline_metrics(
        reviews_clean_file=reviews_clean_file,
        review_groups_file=BASE_DIR / "data" / "review_groups_manual.json",
        personas_file=BASE_DIR / "personas" / "personas_manual.json",
        spec_file=BASE_DIR / "spec" / "spec_manual.md",
        tests_file=BASE_DIR / "tests" / "tests_manual.json",
    )
    save_json(manual_metrics, BASE_DIR / "metrics" / "metrics_manual.json")

    auto_metrics = compute_pipeline_metrics(
        reviews_clean_file=reviews_clean_file,
        review_groups_file=BASE_DIR / "data" / "review_groups_auto.json",
        personas_file=BASE_DIR / "personas" / "personas_auto.json",
        spec_file=BASE_DIR / "spec" / "spec_auto.md",
        tests_file=BASE_DIR / "tests" / "tests_auto.json",
    )
    save_json(auto_metrics, BASE_DIR / "metrics" / "metrics_auto.json")

    summary = {
        "manual": manual_metrics,
        "automated": auto_metrics,
    }

    hybrid_groups = BASE_DIR / "data" / "review_groups_hybrid.json"
    hybrid_personas = BASE_DIR / "personas" / "personas_hybrid.json"
    hybrid_spec = BASE_DIR / "spec" / "spec_hybrid.md"
    hybrid_tests = BASE_DIR / "tests" / "tests_hybrid.json"

    if (
        hybrid_groups.exists()
        and hybrid_personas.exists()
        and hybrid_spec.exists()
        and hybrid_tests.exists()
    ):
        try:
            hybrid_metrics = compute_pipeline_metrics(
                reviews_clean_file=reviews_clean_file,
                review_groups_file=hybrid_groups,
                personas_file=hybrid_personas,
                spec_file=hybrid_spec,
                tests_file=hybrid_tests,
            )
            save_json(hybrid_metrics, BASE_DIR / "metrics" / "metrics_hybrid.json")
            summary["hybrid"] = hybrid_metrics
        except Exception as e:
            print(f"Skipping hybrid metrics due to invalid hybrid files: {e}")

    save_json(summary, BASE_DIR / "metrics" / "metrics_summary.json")
    print("Metrics computed successfully.")


if __name__ == "__main__":
    main()
