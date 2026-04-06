import subprocess
import sys
from pathlib import Path


SCRIPTS = [
    "src/01_collect_or_import.py",
    "src/02_clean.py",
    "src/05_personas_auto.py",
    "src/06_spec_generate.py",
    "src/07_tests_generate.py",
    "src/08_metrics.py",
    "src/00_validate_repo.py",
]


def run_script(script_path: str):
    print(f"\n=== Running {script_path} ===")
    result = subprocess.run(
        [sys.executable, script_path],
        text=True
    )

    if result.returncode != 0:
        print(f"ERROR: {script_path} failed with exit code {result.returncode}")
        sys.exit(result.returncode)

    print(f"Completed: {script_path}")


def main():
    print("Starting end-to-end pipeline run...")

    for script in SCRIPTS:
        if not Path(script).is_file():
            print(f"ERROR: Missing script: {script}")
            sys.exit(1)
        run_script(script)

    print("\nAll pipeline steps completed successfully.")


if __name__ == "__main__":
    main()
