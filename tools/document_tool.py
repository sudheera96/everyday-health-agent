from strands import tool
from pathlib import Path


@tool
def document_tool(document_path: str) -> str:
    """
    Extract structured information from a synthetic healthcare document.

    This prototype supports plain-text healthcare documents and is intended
    for synthetic or public information only.
    """

    path = Path(document_path)

    if not path.exists():
        return f"Document not found: {document_path}"

    if path.suffix.lower() != ".txt":
        return (
            "This prototype currently supports .txt healthcare documents."
        )

    text = path.read_text(encoding="utf-8").strip()

    if not text:
        return "The healthcare document is empty."

    fields = {
        "appointment_type": "",
        "provider": "",
        "date": "",
        "time": "",
        "reason": "",
        "instructions": [],
    }

    current_section = None

    for raw_line in text.splitlines():
        line = raw_line.strip()

        if not line:
            continue

        lower = line.lower()

        if lower.startswith("appointment type:"):
            fields["appointment_type"] = line.split(":", 1)[1].strip()

        elif lower.startswith("provider:"):
            fields["provider"] = line.split(":", 1)[1].strip()

        elif lower.startswith("date:"):
            fields["date"] = line.split(":", 1)[1].strip()

        elif lower.startswith("time:"):
            fields["time"] = line.split(":", 1)[1].strip()

        elif lower.startswith("reason for appointment:"):
            current_section = "reason"

        elif lower.startswith("instructions:"):
            current_section = "instructions"

        elif current_section == "reason":
            fields["reason"] = line
            current_section = None

        elif current_section == "instructions":
            fields["instructions"].append(line)

    result = [
        "DOCUMENT SUMMARY",
        "",
        f"Appointment Type: {fields['appointment_type']}",
        f"Provider: {fields['provider']}",
        f"Date: {fields['date']}",
        f"Time: {fields['time']}",
        f"Reason: {fields['reason']}",
        "",
        "Appointment Instructions:",
    ]

    for instruction in fields["instructions"]:
        result.append(f"- {instruction}")

    result.extend(
        [
            "",
            "SAFETY NOTE:",
            "This tool extracts information from the document.",
            "It does not diagnose conditions or provide treatment advice.",
            "For clinical questions or conflicting instructions, contact",
            "the healthcare provider or healthcare facility.",
        ]
    )

    return "\n".join(result)