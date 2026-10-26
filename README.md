# Road Safety Policy Agent

## Problem definition
Why do road deaths rise despite stricter rules, and which enforcement-focused
policies could reduce them? Based on TOI editorial "Sense & Licence".

## Technology stack
- Python 3.x, OpenAI-compatible SDK
- LLM: [model name] via [provider], used for reasoning and tool calling
- Tool-calling agent loop (max 8 steps), 4 tools: fatality stats, enforcement
  gap, traffic-law lookup, policy options
- Streamlit UI (optional)
- Compute: CPU only locally; LLM runs on provider's servers

## Design principles
- DRY: all facts live in data.py
- Orthogonality: tools, prompts, agent loop and UI are separate modules
- Small iterations: tools tested one by one before the agent loop
- Grounding: the agent must call tools and only cite returned numbers
- Transparency: every policy includes justification, impact and trade-offs
- Neutrality: governance analysis only

## Limitations
- Evidence base is small (article + MV Act figures); [list any you verified]
- Penalty figures should be verified against official sources
- Policy suggestions are not legal advice

## Links
- Task 1 website: [link]
- Task 2 fine-tuned model/notebook: [link]