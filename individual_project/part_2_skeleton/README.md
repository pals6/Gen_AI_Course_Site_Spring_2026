# RAG + POML Code Documentation Chatbot

This project implements a Retrieval-Augmented Generation (RAG) chatbot that answers questions from Python, Java, and JavaScript documentation PDFs.
It integrates Groq LLM APIs via LangChain (`ChatGroq`) in a custom orchestration pipeline for contextual response generation and LLM-as-a-judge evaluation.

## What This Project Does

- Builds vector collections from local PDF docs using ChromaDB.
- Routes each user question to the correct language collection.
- Retrieves relevant chunks from the selected collection.
- Generates answers with selectable prompting techniques via POML templates.
- Supports LLM-as-a-judge for model and prompting-technique comparisons.

## Repository Layout

- `ingest_files/` - Source PDFs used for retrieval.
- `rag_ingestion/ingest_documents.py` - PDF parsing, chunking, and Chroma ingestion.
- `rag_ingestion/chroma_db/` - Persisted Chroma vector store.
- `chatbot/main.py` - CLI entry point and menu for all run modes.
- `chatbot/rag_pipeline.py` - Routing, retrieval, answer generation, and comparisons.
- `chatbot/prompt_renderer.py` - Renders POML prompts with runtime context.
- `chatbot/prompts/route.poml` - Routing prompt.
- `chatbot/prompts/answer.poml` - Answer prompt techniques.
- `chatbot/prompts/judge.poml` - Judge prompt.
- `.env.example` - Example env file format.

## Prerequisites

- Python 3.10+ recommended
- A Groq API key

## Setup

Run from this folder (`individual_project/part_2_skeleton`):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Then edit `.env`:

```env
GROQ_API_KEY=your_groq_api_key_here
```

## Build the Vector Store

```bash
python rag_ingestion/ingest_documents.py
```

This creates or updates the collections:

- `python_book`
- `java_book`
- `javascript_book`

Note: `chatbot/main.py` can also prompt you to build the vector store automatically if it is missing.

## Run the Chatbot

```bash
python chatbot/main.py
```

You will choose one mode:

1. Single Model and Single Prompting Technique
2. Compare Multiple Models using one Prompting Technique
3. Compare Multiple Prompting Techniques using one Model

## Prompting Techniques

Configured in `chatbot/prompt_renderer.py`:

- `zero_shot`
- `few_shot`
- `cot`
- `advanced` (currently labeled "Ethical Considerations")

## Where to Customize

- Change selected models in `chatbot/rag_pipeline.py`.
- Edit routing/answer/judge behavior in `chatbot/prompts/*.poml`.
- Tune chunking settings in `rag_ingestion/ingest_documents.py`.
- Update `COMPARISON_MODELS`, `ROUTER_MODEL`, and `JUDGE_MODEL` in `chatbot/rag_pipeline.py`.

## Troubleshooting

- Missing API key: ensure `.env` exists and includes `GROQ_API_KEY`.
- Empty retrieval or bad answers: rebuild vectors with `python rag_ingestion/ingest_documents.py`.
- Collection mismatch errors: ensure embedding model name is consistent between ingestion and retrieval code.

## Assignment Notes

- This is a skeleton project and still contains TODO comments for students.
- Keep your final write-up focused on model choice, chunking, retrieval quality, prompting strategy, and judge results.
