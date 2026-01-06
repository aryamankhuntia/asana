import os
from pathlib import Path
from openai import OpenAI

client = OpenAI(api_key=os.getenv("LLM_API_KEY"))

PROMPTS_DIR = Path("prompts")


def llm_available() -> bool:
    return os.getenv("LLM_API_KEY") is not None


def load_prompt(prompt_filename: str) -> str:
    prompt_path = PROMPTS_DIR / prompt_filename
    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")
    return prompt_path.read_text()


def generate_examples(
    prompt_filename: str,
    n: int = 20,
    temperature: float = 0.8,
) -> list[str] | None:
    """
    Generates a list of short text examples using ChatGPT.
    Returns None if LLM is unavailable.
    """
    if not llm_available():
        return None

    prompt = load_prompt(prompt_filename)

    system_message = (
        "You generate realistic text used in enterprise project management tools. "
        "Be concise, informal, and varied."
    )

    user_message = f"""
{prompt}

Return EXACTLY {n} items as a numbered list.
Do not include explanations or extra text.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # fast, cheap, good enough
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},
        ],
        temperature=temperature,
    )

    raw_text = response.choices[0].message.content.strip()

    examples = []
    for line in raw_text.splitlines():
        line = line.strip()
        if not line:
            continue
        cleaned = line.lstrip("0123456789. )-").strip()
        if cleaned:
            examples.append(cleaned)

    return examples[:n] if examples else None
