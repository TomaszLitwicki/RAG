# Personal Landing Page with RAG

An AI-powered personal landing page: visitors ask questions in natural language and get
answers grounded in a curated knowledge base about my background, projects and skills —
instead of scrolling through a static CV page.

**Live: [tomaszlitwicki.pythonanywhere.com](https://tomaszlitwicki.pythonanywhere.com/)**

The retrieval layer is written from scratch — no vector database, no embedding API. Relevant
chunks are selected by a manifest-driven scoring system, and only those chunks are passed to
the language model, which is instructed to answer strictly from them.

---

## Why build retrieval by hand

The knowledge base is small and stable: nine curated documents about one person. At that
scale a vector store adds infrastructure and latency without improving answers, while a
transparent scoring function has a practical advantage — every answer comes with the sources
and scores that produced it, so when a reply is wrong it is obvious *why* it was wrong.

Building it this way also meant confronting the parts of RAG that an embedding API usually
hides: intent detection, source ranking, relevance thresholds and grounding.

---

## How it works

```
question
   │
   ├─► intent detection      keywords from the manifest → query type
   │
   ├─► routing               query type → ordered list of preferred sources
   │
   ├─► scoring               each chunk scored on 4 signals
   │
   ├─► threshold + top-K     below the cut-off, nothing is passed on
   │
   └─► generation            selected chunks → LLM, answer + source list
```

### 1. Knowledge base

Content lives in `chunks/` as Markdown files with YAML front matter:

```markdown
---
id: projects_01
category: projects
type: anchor_chunk
language: pl
audience: recruiter
tags:
  - horse
  - owner
  - flask
  - sqlite
---

Chunk body in Markdown…
```

Editing the knowledge base means editing Markdown — no re-indexing step, no build.

### 2. Manifest

`chunks/00_manifest_index.md` is the control file for retrieval. It defines:

- **`canonical_order`** — the default ranking of sources when nothing more specific applies
- **`retrieval_priority`** — A/B/C tiers grouping sources by general importance
- **`intent_keywords`** — keyword sets that identify what a question is about
- **`query_routing`** — which sources to prefer, in order, for each intent
- **`intent_categories`** — which content categories match each intent

Retrieval behaviour is therefore configuration, not code: adding a new intent or reordering
sources is a change to one Markdown file.

### 3. Intent detection

The question is normalised (lower-cased, Polish diacritics folded), tokenised, and matched
against the manifest's keyword sets by prefix. Prefix matching handles inflection, which
matters in Polish — `projektami`, `projektów` and `projekt` all match the same keyword. The
highest-scoring intent wins; if nothing matches, retrieval falls back to canonical order.

### 4. Scoring

Every chunk is scored on four independent signals:

| Signal | Weight |
| :-- | :-- |
| Position in the routed source list for this intent | 12, decreasing by 2 per position |
| Chunk category matches the intent's categories | +3 |
| Question token matches a chunk tag (prefix) | +5 per tag |
| Question token occurs in the chunk body | +1 per occurrence, capped at 5 |

Combining routing with content matching means a question can pull in an off-route chunk when
the wording strongly points there, while routing still decides ties.

### 5. Threshold and grounding

Chunks scoring below the minimum are discarded, and the top 3 survivors go to the model. If
nothing clears the threshold, **no call to the model is made** — the page says it has no
sources for that question rather than letting the model improvise.

What does reach the model is constrained by a system prompt that requires answers drawn only
from the supplied context, forbids inventing facts, and explicitly forbids overstating
seniority, commercial experience or project scope. Grounding a portfolio assistant matters in
both directions: it must not invent, and it must not flatter.

Every answer is shown together with the sources and scores behind it.

---

## Tech stack

- **Python** · **Flask** · **Jinja2** — backend and templating
- **PyYAML** — front matter and manifest parsing
- **OpenAI API** — answer generation
- **HTML / CSS** — frontend
- Deployed on **PythonAnywhere**

Flask routing follows the Post/Redirect/Get pattern — the answer is held in the session and
rendered after a redirect, so refreshing the page never re-submits a question.

---

## Project structure

```
.
├─ app.py                  # Flask routes, PRG flow
├─ services/
│  ├─ loader.py            # front matter parsing, chunk and manifest loading
│  ├─ retriever.py         # normalisation, intent detection, scoring, ranking
│  └─ llm.py               # context assembly, prompting, model call
├─ chunks/                 # knowledge base (Markdown + YAML front matter)
│  └─ 00_manifest_index.md # retrieval configuration
├─ templates/
├─ static/
└─ requirements.txt
```

Each service module runs standalone (`python -m services.retriever`) to inspect intent,
scores and selected sources for a given question without starting the web app.

---

## Running locally

```bash
git clone https://github.com/TomaszLitwicki/<repo>.git
cd <repo>

python -m venv .venv
source .venv/bin/activate        # Windows: .\.venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
FLASK_SECRET_KEY=any_long_random_string
```

Then:

```bash
python app.py
```

The app starts on `http://127.0.0.1:5000`. Without an API key it still loads and retrieves
sources, but reports that it cannot generate an answer.

---

## Roadmap

- Cache the knowledge base at startup instead of reloading it per request
- Graceful handling of API failures, with retrieved sources still shown
- Answer in the language of the question
- Unit tests for scoring and intent detection
- Optional embedding-based reranking as the knowledge base grows

---

Built by [Tomasz Litwicki](https://github.com/TomaszLitwicki)
