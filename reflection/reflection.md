# Reflection

## Overview

My project explored 3 approaches for deriving software specifications from user reviews: manual, automated, and hybrid pipelines.

---

## Manual Pipeline

The manual pipeline used a careful interpretation of user feedback. Review groups, personas, and requirements were constructed based on human judgment.

Strengths:
- Accurate and careful interpretation of user intent
- Lower ambiguity in requirements
- Strong alignment with real user needs

Limitations:
- Very Time-consuming
- Limited scalability
- Smaller subset of reviews used

---

## Automated Pipeline

The automated pipeline used an LLM to generate artifacts quickly.

Strengths:
- Fast and scalable
- Consistent structure across artifacts
- Full traceability and testability achieved

Limitations:
- Higher ambiguity in requirements and possible confusion
- Generic outputs in some cases
- Less alignment with nuanced user needs

---

## Hybrid Pipeline

The hybrid pipeline combined automated generation with manual refinement.

Strengths:
- Reduced ambiguity compared to the automated pipeline
- Increased number of validation tests
- Maintained full traceability and testability
- Improved alignment with real user needs

---

## Metrics Comparison

- All pipelines produced the same number of personas and requirements.
- The automated pipeline had less tests but more ambiguity.
- The manual and hybrid pipelines produced more tests and clearer requirements.
- The hybrid pipeline produced the best balance between quality and scalability.

---

## Key Insights

- Automation is useful for generating initial drafts quickly.
- Human judgment is essential for refining and improving quality.
- Combining both approaches leads to the most effective results.

---

## Conclusion

The hybrid pipeline provided the best overall performance by leveraging automation while improving outputs through manual refinement. It reduced ambiguity, increased validation coverage, and maintained full traceability, making it the most effective approach.
