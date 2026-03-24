from pathlib import Path
import yaml

obecny_folder = Path.cwd()
folder_chankow = obecny_folder.parent / "chunks"

if folder_chankow.exists():
    print("Chunks folder exists")
else:
    raise RuntimeError ("Chunk's folder does not exist")

print(folder_chankow)

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
        "body": body,
        **metadata,
    }

    return chunk

def load_all_chunks () -> list[dict]:
    chunks = []
    for plik in folder_chankow.rglob("*.md"):
        if plik.name.startswith("00"):
            continue

        chunk = load_markdown_chunk(plik)
        chunks.append(chunk)

    return chunks


if __name__ == '__main__':
    chunks = load_all_chunks()

    for chunk in chunks:
        print("=" * 60)
        print("ID:", chunk.get("id"))
        print("CATEGORY:", chunk.get("category"))
        print("TAGS:", chunk.get("tags"))
        print("FILE:", chunk.get("source_file"))
        print("CONTENT PREVIEW:\n", chunk.get("body", "")[:100])