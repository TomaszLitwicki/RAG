from pathlib import Path
import yaml

BASE_DIR = Path(__file__).resolve().parent.parent
CHUNKS_DIR = BASE_DIR / "chunks"
MANIFEST_PATH = CHUNKS_DIR / "00_manifest_index.md"

if CHUNKS_DIR.exists():
    pass
else:
    raise RuntimeError ("Chunk's folder does not exist")


def front_matter_and_body (text: str) -> tuple[dict, str]:
    text = text.strip()

    if not text.startswith("---"):
        return {}, text

    parts = text.split("---", 2)

    if len(parts) < 3:
        return {}, text

    yaml_part = parts[1].strip()
    body_part = parts[2].strip()

    metadata = yaml.safe_load(yaml_part) or {}

    return metadata, body_part


def load_markdown_chunk (file_path: Path) -> dict:
    text = file_path.read_text(encoding="UTF-8")
    metadata, body = front_matter_and_body(text)

    chunk = {
        "source_file": file_path.stem,
        "content": body,
        **metadata,
    }

    return chunk


def load_manifest () -> dict:
    manifest = load_markdown_chunk(MANIFEST_PATH)

    return manifest

def load_all_chunks () -> list[dict]:
    chunks = []
    for plik in CHUNKS_DIR.rglob("*.md"):
        if plik.name.startswith("00"):
            continue

        chunk = load_markdown_chunk(plik)
        chunks.append(chunk)

    return chunks


if __name__ == '__main__':
    chunks = load_all_chunks()
    manifest = load_manifest()

    print(manifest)

    # for chunk in chunks:
    #     print("=" * 60)
    #     print("ID:", chunk.get("id"))
    #     print("CATEGORY:", chunk.get("category"))
    #     print("TAGS:", chunk.get("tags"))
    #     print("FILE:", chunk.get("source_file"))
    #     print("CONTENT PREVIEW:\n", chunk.get("content", "")[:100])