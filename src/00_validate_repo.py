from pathlib import Path


REQUIRED_DIRECTORIES = [
    "data",
    "personas",
    "spec",
    "tests",
    "metrics",
    "reflection",
    "prompts",
    "src",
]

REQUIRED_FILES = [
    "README.md",
    "data/reviews_raw.jsonl",
    "data/reviews_clean.jsonl",
    "data/dataset_metadata.json",
    "data/review_groups_manual.json",
    "data/review_groups_auto.json",
    "data/review_groups_hybrid.json",
    "personas/personas_manual.json",
    "personas/personas_auto.json",
    "personas/personas_hybrid.json",
    "spec/spec_manual.md",
    "spec/spec_auto.md",
    "spec/spec_hybrid.md",
    "tests/tests_manual.json",
    "tests/tests_auto.json",
    "tests/tests_hybrid.json",
    "metrics/metrics_manual.json",
    "metrics/metrics_auto.json",
    "metrics/metrics_hybrid.json",
    "metrics/metrics_summary.json",
    "prompts/prompt_auto.json",
    "src/00_validate_repo.py",
    "src/01_collect_or_import.py",
    "src/02_clean.py",
    "src/05_personas_auto.py",
    "src/06_spec_generate.py",
    "src/07_tests_generate.py",
    "src/08_metrics.py",
    "src/run_all.py",
]


def main():
    project_root = Path(".")
    missing = []

    print("Checking required directories...")
    for directory in REQUIRED_DIRECTORIES:
        path = project_root / directory
        if path.is_dir():
            print(f"[OK] Directory exists: {directory}")
        else:
            print(f"[MISSING] Directory missing: {directory}")
            missing.append(directory)

    print("\nChecking required files...")
    for file_path in REQUIRED_FILES:
        path = project_root / file_path
        if path.is_file():
            print(f"[OK] File exists: {file_path}")
        else:
            print(f"[MISSING] File missing: {file_path}")
            missing.append(file_path)

    print("\nValidation summary")
    if missing:
        print("Repository validation failed.")
        print("Missing items:")
        for item in missing:
            print(f" - {item}")
    else:
        print("Repository validation passed. All required files and folders exist.")


if __name__ == "__main__":
    main()
