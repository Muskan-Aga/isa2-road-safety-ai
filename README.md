# ISA2 Road Safety AI: Assignment A ("Sense & Licence", TOI)

**Problem:** Why do road deaths rise despite stricter rules, and which enforcement-focused policies could reduce them?

## Tasks
1. **Website:** explainer on fatality trend, India vs Vietnam vs Singapore, enforcement gap. *(tool and link)*
2. **Fine-tuned LLM** (`llm-finetuning/`): road-safety and traffic-law assistant.
3. **Policy agent** (repo root): tool-calling agent that recommends enforcement policies with trade-offs.

## Task 2: LLM (SFT + QLoRA)
- Base model: Qwen2.5-1.5B-Instruct, 4-bit NF4
- Data: self-built, 95 Q&A pairs (86 train / 9 held-out), `llm-finetuning/road_safety_sft.jsonl`
- LoRA: r=16, alpha=32, all 7 projection modules (18.46M trainable params, 1.18%)
- Training: 5 epochs, batch 2 x grad-accum 4, lr 2e-4; loss 2.96 -> 0.65
- Memory: 1.15 GB at load, 2.09 GB peak
- Adapter: `llm-finetuning/road_safety_lora.zip`
- Compute: first run on Colab GPU (outputs saved); re-run on Kaggle GPU when Colab became unavailable
- Limitations: small dataset, some answers still wrong, penalty figures unverified

## Task 3: Agent
- LLM: openai/gpt-oss-120b via Groq; plain Python tool-calling loop (max 8 steps)
- 4 tools over an evidence base in `data.py`; output: recommendation, justification, impact, trade-offs
- Iterations: run 1 invented percentages and flipped a comparison; fixed with prompt rules and evidence corrections

## Design principles
DRY (facts in `data.py`), orthogonality (tools / prompts / loop separate), small iterations, evidence grounding, held-out evaluation, neutrality.

## Run the agent
pip install -r requirements.txt, create .env with LLM_API_KEY, LLM_BASE_URL, LLM_MODEL, then python agent.py
