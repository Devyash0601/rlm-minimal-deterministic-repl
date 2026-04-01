# Deterministic Recursive Language Models with Enforced REPL Termination

An extension of **Recursive Language Models (RLMs)** featuring deterministic execution, strict REPL constraints, and guaranteed termination for reliable long-context reasoning.

This repository is a research-oriented extension of the minimal RLM implementation originally released by **Alex Zhang**. It introduces formal termination conditions, deterministic execution guarantees, and model-agnostic local inference support (e.g., Ollama), while preserving the core recursive abstraction.

---

## 📄 Research & Publications

This work builds upon the original RLM framework and introduces deterministic control mechanisms.

* **Original RLM Paper:** [Recursive Language Models (arXiv:2512.24601)](https://arxiv.org/abs/2512.24601v1)
* **Deterministic Extension (Local PDF):** [Read the internal paper here](https://github.com/Devyash0601/rlm-minimal-deterministic-repl/blob/b0c9d44e4a194924d0df69f1559e2c1a15cd4cd7/deterministic_rlm_minimal.pdf)
* **Preprint / Technical Report:** [Zenodo Record 18317150](https://zenodo.org/records/18317150)

---

## 💡 Background & Attribution

This project is inspired by the foundational work of Alex Zhang:
* **Original RLM Codebase:** [github.com/alexzhang13/rlm](https://github.com/alexzhang13/rlm)
* **Original Blog Post:** [alexzhang13.github.io/blog/2025/rlm/](https://alexzhang13.github.io/blog/2025/rlm/)

All credit for the initial Recursive Language Model formulation and REPL-based design belongs to the original author. This repository extends those concepts to ensure reproducibility and safety in automated reasoning environments.

---

## 🚀 Key Contributions

The original `rlm-minimal` demonstrates that recursive reasoning via a REPL is possible. This project focuses on making it **reliable, deterministic, and publishable.**

### 1. Deterministic Termination
* The model must assign the final result to a variable named `answer`.
* Execution automatically halts the moment `answer` is defined in the local namespace.
* Prevents infinite loops and unbounded tool-call recursions.

### 2. Strict REPL Execution Model
* **Python-only execution:** No shell access or external side effects.
* **Immutable Context:** The source context is read-only to prevent hallucinated data modification.
* **Constraint Enforcement:** Prevents the model from "guessing" constants or calling termination variables prematurely within logic blocks.

### 3. Hard Separation of Reasoning vs. Output
* **REPL:** Solely for evidence gathering and computation.
* **Controller:** Responsible for state monitoring and final return.
* Eliminates "partial answers" or conversational filler during the reasoning phase.

### 4. Local & Offline Support
* Optimized for **Ollama** (e.g., `qwen2.5:7b`, `llama3`).
* No OpenAI API key required; fully compatible with air-gapped or private local environments.

---

## 🛠 Why This Matters

Recursive LMs are powerful, but unbounded recursion is computationally expensive and unpredictable. This project addresses three core weaknesses:

| Problem | Deterministic RLM Solution |
| :--- | :--- |
| **Infinite REPL Loops** | Deterministic termination hook |
| **Model-Dependent Stopping** | Controller-enforced halting |
| **Non-Reproducible Runs** | Strict execution constraints & deterministic seeds |

---

## 🔍 Example: Needle-in-a-Haystack (NIAH)

The included `main.py` demonstrates a stress test where the model must:
1.  Scan ~1 million lines of random text (the "haystack").
2.  Extract a single unlabeled integer (the "needle").
3.  Programmatically verify the integer and assign it to `answer`.
4.  **Terminate immediately** upon discovery.

This validates long-context handling, programmatic evidence extraction, and the reliability of the termination hook.

---

## 📈 Planned Extensions
* **Multi-depth recursive REPLs:** Nested reasoning loops for hierarchical tasks.
* **Formal Correctness Proofs:** Mathematical verification for termination conditions.
* **Program Synthesis Benchmarks:** Evaluating the RLM's ability to write complex logic to solve data-heavy problems.
* **RLM + Verifier Hybrids:** Integrating a secondary model to audit the REPL logic before execution.

---

## 📑 Citation

If you build on this work or use the deterministic extensions, please cite both the original paper and this technical extension:

```bibtex
@article{zhang2025rlm,
  title={Recursive Language Models},
  author={Zhang, Alex},
  journal={arXiv preprint arXiv:2512.24601},
  year={2025}
}

@software{deterministic_rlm_2026,
  author = {Devyash},
  title = {Deterministic REPL Extensions for Recursive Language Models},
  url = {[https://zenodo.org/records/18317150](https://zenodo.org/records/18317150)},
  year = {2026}
}
