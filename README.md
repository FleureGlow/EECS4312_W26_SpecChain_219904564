# SpecChain Pipeline – EECS 4312

## Application Studied

This project analyzes user reviews of a mental health mobile application (MindDoc).  
The main goal is to extract user needs from reviews and transform them into structured software artifacts such as personas, requirements, and validation tests.

---

## Dataset

- Raw dataset size: 1500 reviews  
- Cleaned dataset size: 1410 reviews  
- Files:
  - data/reviews_raw.jsonl
  - data/reviews_clean.jsonl

---

## Project Structure

- data/ → review datasets and grouped data
- personas/ → personas (manual, auto, hybrid)
- spec/ → specifications (manual, auto, hybrid)
- tests/ → validation tests (manual, auto, hybrid)
- metrics/ → evaluation metrics
- prompts/ → prompts for automated pipeline
- src/ → scripts for pipeline execution
- reflection/ → final reflection


---

## Pipelines

### Manual Pipeline

The manual pipeline was created through human analysis of a subset of user reviews.

Steps:
1. Reviews were grouped into themes  
2. Personas were created  
3. Requirements were derived  
4. Tests were written  

Artifacts:
- data/review_groups_manual.json
- personas/personas_manual.json
- spec/spec_manual.md
- tests/tests_manual.json

The manual pipeline cannot be re-executed automatically because it relies on human judgment.  

To verify results:
python src/08_metrics.py


---

### Automated Pipeline

The automated pipeline uses an LLM to generate artifacts.

How to run:
---

### Automated Pipeline

The automated pipeline uses an LLM to generate artifacts.

How to run:

export GROQ_API_KEY="myAPIKey"
python src/run_all.py


This script performs:
- Collect reviews  
- Clean reviews  
- Generate personas and groups  
- Generate specifications  
- Generate tests  
- Compute metrics  
- Validate repository  

Outputs:
- data/review_groups_auto.json
- personas/personas_auto.json
- spec/spec_auto.md
- tests/tests_auto.json
- metrics/metrics_auto.json

---

### Hybrid Pipeline

The hybrid pipeline refines automated outputs manually.

Results:
- data/review_groups_hybrid.json
- personas/personas_hybrid.json
- spec/spec_hybrid.md
- tests/tests_hybrid.json

To recompute metrics:
python src/08_metrics.py


---

## Metrics

To compute metrics:
python src/08_metrics.py


Results:
- metrics/metrics_manual.json
- metrics/metrics_auto.json
- metrics/metrics_hybrid.json
- metrics/metrics_summary.json

---

## Validation

To verify repository structure:
python src/00_validate_repo.py


---

## Reproducibility

The automated pipeline can be reproduced using:
python src/run_all.py


---

## Key Findings

- Automated pipeline is fast but more ambiguous  
- Manual pipeline is higher quality but not scalable  
- Hybrid pipeline provides the best balance  

---

## Author

Fatima Dieng
Student ID: 219904564
