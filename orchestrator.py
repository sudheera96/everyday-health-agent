from tools.document_tool import document_tool
from tools.healthcare_knowledge import healthcare_knowledge
from tools.appointment_tool import appointment_preparation
from tools.safety_tool import safety_check


def run_appointment_workflow(document_path: str) -> str:
    """
    Run the complete appointment-readiness workflow locally.

    Workflow:
    1. Extract appointment information.
    2. Retrieve general healthcare preparation guidance.
    3. Build an appointment checklist.
    4. Run a safety review.
    """

    print("\n[1/4] Extracting appointment document...")
    document_result = document_tool(document_path)

    print("[2/4] Retrieving healthcare preparation guidance...")
    knowledge_result = healthcare_knowledge(
        "How should a patient prepare for a healthcare appointment?"
    )

    print("[3/4] Creating appointment preparation checklist...")

    checklist = appointment_preparation(
        appointment_type="Cardiology Consultation",
        provider="Dr. Taylor",
        date="September 10, 2026",
        time="10:30 AM",
        reason="Initial consultation regarding cardiovascular health",
        instructions=(
            "Bring a current medication and supplement list;"
            "Bring relevant previous medical records if available;"
            "Bring identification and insurance information;"
            "Prepare questions or concerns"
        ),
    )

    print("[4/4] Running safety review...")

    safety_result = safety_check(
        user_request="Help me prepare for my cardiology appointment.",
        proposed_response=checklist,
    )

    return f"""
========================================
EVERYDAY HEALTH AGENT
APPOINTMENT READINESS RESULT
========================================

DOCUMENT INFORMATION
--------------------
{document_result}

GENERAL HEALTHCARE GUIDANCE
---------------------------
{knowledge_result}

PERSONALIZED CHECKLIST
----------------------
{checklist}

SAFETY REVIEW
-------------
{safety_result}

========================================
END OF WORKFLOW
========================================
"""


if __name__ == "__main__":
    result = run_appointment_workflow(
        "data/documents/cardiology_appointment.txt"
    )

    print(result)