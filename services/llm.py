from openai import OpenAI
from dotenv import load_dotenv
import os
from app import session

load_dotenv()
AI_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=AI_KEY)

CONTEX = ""

SYSTEM_PROMPT = """
        You are a grounded RAG assistant for Tomasz Litwicki's Personal Landing Page.
        Answer only from the provided context.
        Do not invent facts.
        Do not exaggerate seniority, commercial experience, or project scope.
        If the context is insufficient, say that clearly.
        Keep the answer factual, concise, and trustworthy.
        Use the same language as the user's question.
    """

def build_contex(selected_chunks: list[dict]) -> str:
    if not selected_chunks:
        return ""

    parts = []

    for chunk in selected_chunks:
        category = chunk.get("category", "unknow_category")
        score = chunk.get("score", "unknow_score")
        content = chunk.get("content", "").strip()

        block = (
            f"category: {category}\n"
            f"score: {score}\n"
            f"content: {content}"
        )

        parts.append(block)

    return "\n\n".join(parts)

def build_prompt(question, contex):
    prompt = (
        f"USER QUESTION: {question}"
        f"CONTEX: {contex}"
        "TASK:\n"
        "Answer the user's question using only the context above. "
        "If the answer is partially supported, say what is supported and what is uncertain. "
        "If the answer is not in the context, say that you cannot confirm it from the current knowledge base.")

    return prompt

def call_llm(question: str, selected_chunks: list[dict]) -> str:
    if not AI_KEY:
        return "BŁĄD PO STRONIE DEVELOPERA: Brak klucza OPEN AI KEY"

    contex = build_contex(selected_chunks)
    if contex == "":
        return "Brak odpowiednich źródeł na to pytanie. Model AI nie może odpowiedzieć."
    prompt = build_prompt(question, contex)

    response = client.responses.create(
        model="gpt-5-nano",
        instructions=SYSTEM_PROMPT,
        input=prompt
    )

    answer = str(response.output_text)
    if not answer:
        return "Model AI nie zwrócił poprawnej odpowiedzi... Spróbuj jeszcze raz"

    return answer

ask = session

if __name__ == "__main__":
    message = "Jaki jest główny projekt Tomasza"
    response = call_llm(message)
    print(type(response))

