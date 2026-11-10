import asyncio, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src" / "llm_wiki"))
from ingest import ingest_source, IngestResult

SOURCES = [
    "raw/papers/rag-original.txt",
    "raw/articles/rag-in-practice.txt",
    "raw/articles/rag-limitations.txt",
]

async def main():
    for src in SOURCES:
        print(f"\n\n========== INGESTING {src} ==========\n")
        async for chunk in ingest_source(src):
            if chunk.startswith("__RESULT__:"):
                r = IngestResult(**json.loads(chunk[11:]))
                print(f"\n[done] {r.title} — {len(r.pages_written)} pages\n")
            else:
                print(chunk, end="", flush=True)

if __name__ == "__main__":
    asyncio.run(main())