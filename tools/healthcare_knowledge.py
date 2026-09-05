from strands import tool
from pathlib import Path


KNOWLEDGE_DIR = Path(__file__).parent.parent / "data" / "healthcare_knowledge"


@tool
def healthcare_knowledge(query: str) -> str:
    """
    Retrieve general healthcare preparation information from the
    local trusted knowledge base.

    Use this tool when a user asks about preparing for a healthcare
    appointment, test, procedure, or general healthcare visit.
    """

    if not KNOWLEDGE_DIR.exists():
        return "Healthcare knowledge base is not available."

    documents = list(KNOWLEDGE_DIR.glob("*.txt"))

    if not documents:
        return "No healthcare knowledge documents are available."

    query_words = set(query.lower().split())

    results = []

    for document in documents:
        text = document.read_text(encoding="utf-8")
        text_lower = text.lower()

        score = sum(
            1 for word in query_words
            if len(word) > 2 and word in text_lower
        )

        if score > 0:
            results.append((score, document.name, text))

    results.sort(reverse=True)

    if not results:
        return (
            "I could not find relevant information in the healthcare "
            "knowledge base."
        )

    output = ["Relevant healthcare information:"]

    for score, filename, text in results[:3]:
        output.append(f"\nSource: {filename}")
        output.append(text)

    return "\n".join(output)