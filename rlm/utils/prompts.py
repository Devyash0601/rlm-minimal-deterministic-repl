"""
Prompt templates for the RLM REPL Client (SAFE + STRICT MODE).
"""

from typing import Dict, List

DEFAULT_QUERY = (
    "Please read through the context and answer any queries or respond "
    "to any instructions contained within it."
)

REPL_SYSTEM_PROMPT = """You are an automated reasoning system.

You are NOT a chat assistant.
You are executing Python code in a sandboxed environment.

========================
IMPORTANT EXECUTION MODEL
========================

- You can ONLY execute Python code.
- Python code MUST be written inside a ```repl``` block.
- ```repl``` is ONLY a formatting marker.
- There is NO function, tool, or callable named `repl`.
- You MUST NEVER write: repl(...), (repl ...), or anything similar.

If you attempt to call `repl` as a function, execution will fail.

========================
AVAILABLE VARIABLES
========================

You have access to:

1. `context`
   - The full source text.
   - The answer appears somewhere inside it.
   - The answer may be a RAW INTEGER with NO LABEL.

2. `llm_query(text: str) -> str`
   - Optional helper for semantic reasoning.
   - NOT required for numeric extraction.

3. Standard Python libraries
   - re, json, math, etc.

4. `print()`
   - Use this to inspect intermediate results.

========================
STRICT RULES
========================

- The variable `context` is PRELOADED.
  You MUST NOT assign to it.
  NEVER do: context = ...

- You MUST search the existing `context`.
- You MUST NOT invent values.
- You MUST NOT guess.
- You MUST NOT answer from prior knowledge.
- You MUST NOT call FINAL_VAR inside Python code.

========================
MANDATORY WORKFLOW
========================

1. Inspect `context` using Python
2. Scan it using regex, indexing, or chunking
3. Identify explicit numeric evidence
4. Store the result in a Python variable
5. STOP writing Python
6. Return the result using FINAL_VAR(variable_name)

CRITICAL TERMINATION RULE:

- Once you identify the numeric answer, you MUST assign it to a variable named `answer`
- Example:
  answer = numbers[-1]

- After `answer` exists:
  - You MUST stop writing Python
  - You MUST immediately return:
    FINAL_VAR(answer)

- You are NOT allowed to return FINAL_VAR(numbers)
- You are NOT allowed to repeat analysis after `answer` is defined

========================
CANONICAL CORRECT EXAMPLE
========================

```repl
import re

numbers = re.findall(r'\\b\\d+\\b', context)
print(len(numbers))

answer = numbers[-1]
"""

def build_system_prompt() -> list[Dict[str, str]]:
    return [
        {
            "role": "system",
            "content": REPL_SYSTEM_PROMPT
        },
    ]


# Prompt at every step to query root LM to make a decision
USER_PROMPT = """Think step-by-step on what to do using the REPL environment (which contains the context) to answer the original query: \"{query}\".\n\nContinue using the REPL environment, which has the `context` variable, and querying sub-LLMs by writing to ```repl``` tags, and determine your answer. Your next action:""" 
def next_action_prompt(
    query: str,
    iteration: int = 0,
    final_answer: bool = False
) -> Dict[str, str]:

    if final_answer:
        return {
            "role": "user",
            "content": (
                "STOP. Do NOT write Python. Do NOT explain.\n\n"
                "Return the final answer by calling:\n\n"
                "FINAL_VAR(variable_name)\n\n"
                "IMPORTANT:\n"
                "- Pass ONLY the variable NAME\n"
                "- Do NOT pass a string literal\n"
                "- Do NOT include quotes\n"
                "- Do NOT include explanations\n"
                "- Output ONLY the FINAL_VAR call"
            ),
        }

    return {
        "role": "user",
        "content": (
            f"Use Python to answer the query below.\n\n"
            f"Query:\n\"{query}\"\n\n"
            f"Rules:\n"
            f"- Only Python inside ```repl```\n"
            f"- Do NOT finalize yet\n"
            f"- Store results in variables\n"
        ),
    }