"""
OpenAI Client wrapper replaced with Ollama (qwen2.5).
"""

import subprocess


class OpenAIClient:
    def __init__(self, api_key=None, model: str = "qwen2.5:7b"):
        # api_key ignored, kept only for compatibility
        self.model = model

    def completion(self, messages, max_tokens=None, **kwargs) -> str:
        if isinstance(messages, list):
            prompt = "\n".join(
                f"{m['role'].upper()}: {m['content']}"
                for m in messages
            )
        else:
            prompt = messages

        try:
            result = subprocess.run(
                ["ollama", "run", self.model],
                input=prompt,
                text=True,
                capture_output=True,
                check=True
            )
            return result.stdout.strip()

        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Ollama error: {e.stderr}")