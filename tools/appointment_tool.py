from strands import tool


@tool
def appointment_preparation(
    appointment_type: str,
    provider: str,
    date: str,
    time: str,
    reason: str,
    instructions: str,
) -> str:
    """
    Create a grounded healthcare appointment preparation checklist.

    The checklist uses appointment-specific information supplied by the
    document extraction tool. It does not diagnose conditions, prescribe
    treatment, or make medication recommendations.
    """

    checklist = []

    checklist.append("APPOINTMENT PREPARATION CHECKLIST")
    checklist.append("")

    # Appointment information extracted from the user's document.
    checklist.append("APPOINTMENT DETAILS")

    if appointment_type:
        checklist.append(f"- Appointment Type: {appointment_type}")

    if provider:
        checklist.append(f"- Provider: {provider}")

    if date:
        checklist.append(f"- Date: {date}")

    if time:
        checklist.append(f"- Time: {time}")

    if reason:
        checklist.append(f"- Reason: {reason}")

    # Only general preparation guidance supported by the knowledge base.
    checklist.append("")
    checklist.append("GENERAL PREPARATION")

    checklist.append(
        "☐ Review the reason for the appointment and any instructions "
        "provided by the healthcare organization."
    )

    checklist.append(
        "☐ Bring or have access to a current medication and supplement "
        "list, including names and doses when known."
    )

    checklist.append(
        "☐ Bring relevant medical records, referral information, or "
        "test results when requested."
    )

    checklist.append(
        "☐ Prepare a list of questions or concerns to discuss with "
        "the healthcare professional."
    )

    checklist.append(
        "☐ Bring identification, insurance information, and appointment "
        "details when required by the healthcare organization."
    )

    # Preserve the appointment-specific instructions from the document.
    if instructions:
        checklist.append("")
        checklist.append("APPOINTMENT-SPECIFIC INSTRUCTIONS")

        for instruction in instructions.split(";"):
            instruction = instruction.strip()

            if instruction:
                checklist.append(f"☐ {instruction}")

    checklist.append("")
    checklist.append("ITEMS TO CONFIRM")

    checklist.append(
        "☐ Confirm any appointment-specific preparation requirements "
        "with the healthcare provider or healthcare facility."
    )

    checklist.append(
        "☐ If the provider's instructions differ from this general "
        "guidance, follow the provider's instructions."
    )

    checklist.append("")
    checklist.append("SAFETY")

    checklist.append(
        "This tool provides general appointment-preparation information. "
        "It does not diagnose medical conditions, prescribe treatment, "
        "or recommend starting, stopping, or changing medication."
    )

    checklist.append(
        "For clinical questions or medication decisions, contact a "
        "qualified healthcare professional."
    )

    return "\n".join(checklist)