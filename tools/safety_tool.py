from strands import tool


@tool
def safety_check(user_request: str, proposed_response: str) -> str:
    """
    Check a healthcare response for potentially unsafe clinical guidance.
    """

    risky_terms = [
        "diagnose me",
        "what is my diagnosis",
        "do i have",
        "what condition do i have",
        "prescribe me",
        "what medication should i take",
        "should i start taking",
        "should i stop taking",
        "should i change my medication",
        "increase my medication",
        "decrease my medication",
        "stop taking my medication",
        "start taking my medication",
        "change my medication",
        "chest pain",
        "difficulty breathing",
        "can't breathe",
        "severe bleeding",
        "suicide",
        "overdose",
    ]

    request_lower = user_request.lower()
    response_lower = proposed_response.lower()

    detected = [
        term
        for term in risky_terms
        if term in request_lower or term in response_lower
    ]

    if detected:
        return (
            "SAFETY REVIEW: CLINICAL REVIEW RECOMMENDED\n\n"
            f"Potentially sensitive topics detected: {', '.join(detected)}\n\n"
            "The response should remain general and educational. "
            "It should not diagnose a condition, prescribe treatment, "
            "or recommend starting, stopping, or changing medication.\n\n"
            "The user should be directed to an appropriate qualified "
            "healthcare professional for clinical decisions."
        )

    return (
        "SAFETY REVIEW: PASSED\n\n"
        "No obvious high-risk clinical decision terms were detected. "
        "The response should still remain general educational information "
        "and should not replace professional medical advice."
    )