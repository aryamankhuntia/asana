# Asana RL Environment — Seed Data Generator

This repository generates a realistic SQLite dataset simulating how a large B2B SaaS company uses Asana for project management.  
The dataset is designed as seed data for reinforcement learning environments evaluating computer-use AI agents.

---

## Overview

- Simulates a company with thousands of employees using Asana across engineering, marketing, sales, operations, and HR.
- Emphasizes realistic task structure, ownership skew, due-date behavior, and temporal consistency.
- Natural language content (task titles, comments, project names) is generated from prompt-based text pools.

---

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Create a `.env` file:

DB_PATH=output/asana_simulation.sqlite
RANDOM_SEED=42
```

---

## Run

```bash
python -m src.main
```

This will generate `output/asana_simulation.sqlite`.

---

## Notes on LLM Usage

Prompt templates are stored under `prompts/`.
These prompts were used offline to generate reusable text pools committed under `text_pools/`, which are sampled during data generation.

This approach preserves prompt-driven realism while keeping the pipeline fully runnable without external APIs or large local models.

---

## Limitations

* Attachments and advanced automation rules are simplified.
* Dataset scale is configurable and may be reduced for faster local execution.
