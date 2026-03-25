import re
from typing import Any
import unicodedata
from services.loader import load_manifest, load_all_chunks


def normalize_text(text:str) -> str:
    text = str(text).lower().strip()
    text = unicodedata.normalize("NFKD", text)
    text = "".join(char for char in text if not unicodedata.combining(char))
    return text


def normalize_source_name(name: str) -> str:
    name = normalize_text(name)
    if name.endswith(".md"):
        name = name[:-3]
    return name


def tokenize(text: str) -> list[str]:
    normalized_text = normalize_text(text)
    return re.findall(r"[a-z0-9+\-#]+", normalized_text)


def safe_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [normalize_text(item) for item in value]
    return []


def get_manifest_section(manifest: dict, key: str, default: Any):
    value = manifest.get(key)
    if value is None:
        return default
    return value


def count_keyword_matches(question_tokens: set[str], keywords: list[str]) -> int:
    count = 0

    for token in question_tokens:
        for keyword in keywords:
            if token.startswith(keyword):
                count += 1
                break
    return count


def detect_query_type(question: str, manifest: dict) -> str:
    question_tokens = set(tokenize(question))

    intent_keywords = get_manifest_section(manifest, "intent_keywords", {})
    best_intent = "unknown_type"
    best_score = 0

    for intent_name, keywords in intent_keywords.items():
        score = count_keyword_matches(question_tokens, keywords)

        if score > best_score:
            best_score = score
            best_intent = intent_name

    return best_intent


def get_preferred_categories(query_type: str, manifest: dict) -> list[str]:
    intent_categories = get_manifest_section(manifest, "intent_categories", {})
    return intent_categories.get(query_type, [])


def get_preferred_sources(query_type: str, manifest: dict) -> list :
    query_routing = get_manifest_section(manifest, "query_routing", {})
    preferred = query_routing.get(query_type, [])

    if preferred:
        return [normalize_source_name(item) for item in preferred]

    canonical_order = get_manifest_section(manifest, "canonical_order", [])
    return [normalize_source_name(item) for item in canonical_order]


def score_chunk(question: str, chunk: dict, preferred_sources: list[str], preferred_categories: list[str]) -> int:
    score = 0
    question_tokens = set(tokenize(question))

    source_file = normalize_text(chunk.get("source_file",""))
    category = normalize_text(chunk.get("category",""))
    body = normalize_text(chunk.get("content",""))
    tags = safe_list(chunk.get("tags"))

    if source_file in preferred_sources:
        position = preferred_sources.index(source_file)
        score = 12 - (position * 2)

    if category and category in preferred_categories:
        score += 6

    for token in question_tokens:
        for tag in tags:
            if token.startswith(tag):
                score += 5
                break

    for token in question_tokens:
        if len(token) < 3:
            continue

        occurrences = body.count(token)
        if occurrences > 0:
            score += min(occurrences, 5)

    return score


def retrieve_chunks (question: str, chunks: list[dict], manifest: dict, top_k = 3, min_score: int = 15) -> list[dict]:
    query_type = detect_query_type(question, manifest)
    preferred_source = get_preferred_sources(query_type, manifest)
    preferred_categories = get_preferred_categories(query_type, manifest)

    scored_chunks = []

    for chunk in chunks:
        chunk_score = score_chunk(question, chunk, preferred_source,preferred_categories)

        if chunk_score > min_score:
            scored_chunks.append(
                {
                    **chunk,
                    "score": chunk_score,
                    "query_type": query_type,
                }
            )

    def sort_key(item: dict, preferred_sources: list[str]) -> tuple[int, int]:
        score_value = item.get("score", 0)

        if item["source_file"] in preferred_sources:
            source_priority = -preferred_sources.index(item["source_file"])
        else:
            source_priority = -100

        return score_value, source_priority

    scored_chunks.sort(key=lambda item: sort_key(item, preferred_source), reverse=True)

    return scored_chunks[:top_k]


def format_sources(selected_chunks: list[dict]) -> str:
    if not selected_chunks:
        return "No matching sources."

    lines = []
    for chunk in selected_chunks:
        lines.append(f"- {chunk.get('source_file')} score: {chunk.get('score')} ")

    return "\n".join(lines)


if __name__ == '__main__':
    ask = "Jaki styl pracy ma Tomasz?"
    ask = "Czy tomasz lubi psy?"
    ask = "Dlaczego zmienia branżę"
    ask = "Dlaczego konie?"
    manifest = load_manifest()
    chunks = load_all_chunks()

    print(ask)

    query_type = detect_query_type(ask, manifest)
    print(f'Query type : {query_type}')

    preferred_sources = get_preferred_sources(query_type, manifest)
    print(f'Prefered source : {preferred_sources}')

    preferred_categories = get_preferred_categories(query_type, manifest)
    print(f'Prefered categories : {preferred_categories}')

    for i in range (8):
        score = score_chunk(ask, chunks[i], preferred_sources, preferred_categories)
        print(f'chunk 0{i+1} Score = {score}')

    selected_chunks = retrieve_chunks(ask,chunks, manifest,)
    for i in selected_chunks:
        print(f'{i["source_file"]} - {i["score"]}')

    print()
    display_sources = format_sources(selected_chunks)
    print(display_sources)

