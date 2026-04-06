# SpecChain Pipeline – EECS 4312

## Application Studied

This project analyzes user reviews of a **mental health mobile application (MindDoc)**.  
Main goal of the project is to extract user needs from reviews and transform them into structured software artifacts such as personas, requirements, and validation tests.

---

## Dataset

- **Raw dataset size:** 1500 reviews  
- **Cleaned dataset size:** 1410 reviews  
- **Files:**
  - `data/reviews_raw.jsonl`
  - `data/reviews_clean.jsonl`

---

## Project Structure


data/ → review datasets and grouped data
personas/ → personas (manual, auto, hybrid)
spec/ → specifications (manual, auto, hybrid)
tests/ → validation tests (manual, auto, hybrid)
metrics/ → evaluation metrics
prompts/ → prompts for automated pipeline
src/ → scripts for pipeline execution
reflection/ → final reflection


---

## Pipelines

### Manual Pipeline

It was created through human analysis of a subset of user reviews.

The following steps were performed manually:

1. Reviews were examined and grouped into themes  
2. Personas were created based on these groups  
3. Software requirements were derived from personas  
4. Validation tests were written for each requirement  

Artifacts are stored in:

- `data/review_groups_manual.json`
- `personas/personas_manual.json`
- `spec/spec_manual.md`
- `tests/tests_manual.json`

### Reproducing Manual Results

The manual pipeline can't be re-executed automatically as it relies on human judgment.  
Hence, results can be verified by recomputing metrics:

```bash
python src/08_metrics.py

This will generate:
metrics/metrics_manual.json

Automated Pipeline

The automated pipeline uses an LLM to generate artifacts.

How to Run

export GROQ_API_KEY="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"
python src/run_all.py

This script performs:

Collect reviews
Clean reviews
Generate review groups and personas
Generate specifications
Generate validation tests
Compute metrics
Validate repository structure
Outputs
data/review_groups_auto.json
personas/personas_auto.json
spec/spec_auto.md
tests/tests_auto.json
metrics/metrics_auto.json


Hybrid Pipeline

The hybrid pipeline is created by refining automated outputs manually.

Artifacts are stored in:

data/review_groups_hybrid.json
personas/personas_hybrid.json
spec/spec_hybrid.md
tests/tests_hybrid.json
Recomputing Hybrid Metrics
python src/08_metrics.py

This generates:
metrics/metrics_hybrid.json

Metrics

To compute metrics for all pipelines:
python src/08_metrics.py

Results are stored in:
metrics/metrics_manual.json
metrics/metrics_auto.json
metrics/metrics_hybrid.json
metrics/metrics_summary.json
Validation

To verify repository structure:
python src/00_validate_repo.py


Reproducibility

The automated pipeline can be reproduced end-to-end using:
python src/run_all.py

This ensures all automated artifacts are regenerated correctly.

Key Findings
The automated pipeline is fast but produces more ambiguous requirements
The manual pipeline produces higher-quality outputs but is less scalable
The hybrid pipeline achieves the best balance between quality and efficiency

Fatima Dieng Student ID: 219904564
