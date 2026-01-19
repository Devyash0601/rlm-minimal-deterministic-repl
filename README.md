# Deterministic Recursive Language Models with Enforced REPL Termination

An extension of Recursive Language Models (RLMs) with deterministic execution, strict REPL constraints, and guaranteed termination.

This repository is a research-oriented extension of the minimal Recursive Language Model (RLM) implementation originally released by Alex Zhang  ￼.
It introduces deterministic execution guarantees, formal termination conditions, and model-agnostic local inference support (e.g. Ollama), while preserving the core RLM abstraction.

⸻

## Background & Attribution

This work is directly inspired by and built on top of:
	•	Original RLM codebase: https://github.com/alexzhang13/rlm
	•	RLM paper: https://arxiv.org/abs/2512.24601v1
	•	Original blog post: https://alexzhang13.github.io/blog/2025/rlm/

All credit for the original Recursive Language Model formulation, conceptual framework, and initial REPL-based design belongs to Alex Zhang.
This repository does not replace the original work — it extends it with additional guarantees required for reproducible, long-context reasoning.

⸻

## What This Project Adds 

The original rlm-minimal demonstrates that recursive reasoning via a REPL is possible.

This project focuses on making it reliable, deterministic, and publishable.

 Key Contributions
	1.	Deterministic Termination
	•	The model must assign the final result to a variable named answer
	•	Execution automatically halts once answer exists
	•	Prevents infinite loops and unbounded tool calls
	2.	Strict REPL Execution Model
	•	Python-only execution
	•	context is immutable
	•	No guessing, no hallucinated constants
	•	No calling of FINAL_VAR inside REPL code
	3.	Hard Separation of Reasoning vs Output
	•	REPL = evidence gathering
	•	Controller = termination + final return
	•	Eliminates ambiguous “partial answers”
	4.	Local / API-Free Model Support
	•	Works with Ollama-based models (e.g. qwen2.5:7b)
	•	No OpenAI API key required
	•	Fully offline compatible
	5.	Failure-Resistant Control Logic
	•	If the model finds the answer but fails to call FINAL_VAR,
the controller enforces termination safely.

## Why This Matters (Research Perspective)
Recursive LMs are powerful , but unbounded recursion is dangerous.
This project addresses three core weaknesses in early RLM systems:
Problems:
1) Infinite REPL loops
2) Model dependent stopping
3) non reproducible run
Solutions:
1) Deterministic termination hook
2) Controller enforced halting
3) Strict execution contraints

## Example: Needle-in-a-Haystack (NIAH)

The included main.py demonstrates a classic stress test:
	•	Generate ~1 million lines of random text
	•	Insert a single unlabeled integer
	•	Ask the RLM to find it

The system must:
	1.	Scan the context programmatically
	2.	Extract numeric evidence
	3.	Assign it to answer
	4.	Terminate immediately

This example validates:
	•	Long-context handling
	•	Deterministic halting
	•	Correct REPL behavior

## Planned extensions:
	•	Multi-depth recursive REPLs
	•	Formal correctness proofs for termination
	•	Program synthesis benchmarks
	•	RLM + verifier hybrids
	•	Comparison against ReAct / Toolformer-style agents

  ## Citation 
  If you build on this work, please cite the original RLM paper and clearly distinguish extensions.
  @article{zhang2025rlm,
  title={Recursive Language Models},
  author={Zhang, Alex},
  journal={arXiv preprint arXiv:2512.24601},
  year={2025}
}

## Acknowledgements
	•	Alex Zhang — original RLM formulation and implementation
	•	Open-source LLM community
	•	Ollama for local inference tooling
