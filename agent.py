# agent.py
import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from prompts import SYSTEM_PROMPT
from tools.registry import TOOL_SCHEMAS, run_tool

load_dotenv()

client = OpenAI(
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
)
MODEL = os.getenv("LLM_MODEL")


def run_agent(question: str, max_steps: int = 8, verbose: bool = True) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]

    for step in range(max_steps):
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOL_SCHEMAS,
            tool_choice="auto",
            temperature=0.3,
        )
        msg = response.choices[0].message

        # No tool requested -> this is the final answer
        if not msg.tool_calls:
            return msg.content

        messages.append(msg)  # keep the assistant's tool request in history

        for call in msg.tool_calls:
            try:
                args = json.loads(call.function.arguments or "{}")
            except json.JSONDecodeError:
                args = {}
            if verbose:
                print(f"[step {step + 1}] tool -> {call.function.name}({args})")
            result = run_tool(call.function.name, args)
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": json.dumps(result),
                }
            )

    return "Stopped: reached the maximum number of steps without a final answer."


if __name__ == "__main__":
    q = (
        "Why do road deaths rise despite stricter rules, and which "
        "enforcement-focused policies could reduce them in India?"
    )
    print(run_agent(q))