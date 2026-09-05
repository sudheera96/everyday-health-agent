import streamlit as st
import tempfile
from pathlib import Path

from app import agent


st.set_page_config(
    page_title="Everyday Health Agent",
    page_icon="🩺",
    layout="centered",
)


# -----------------------------
# Header
# -----------------------------

st.title("🩺 Everyday Health Agent")

st.markdown(
    """
    ### Prepare for your healthcare appointment

    Upload your appointment or referral document and tell the agent
    what you need help with.
    """
)

st.info(
    "For this prototype, use synthetic or public healthcare documents only. "
    "Do not upload real patient-identifying information."
)


# -----------------------------
# Document Upload
# -----------------------------

st.subheader("1. Upload your appointment document")

uploaded_file = st.file_uploader(
    "Choose an appointment or referral document",
    type=["txt"],
    help="Upload a synthetic or public healthcare document.",
)


# -----------------------------
# User Request
# -----------------------------

st.subheader("2. What would you like help with?")

user_request = st.text_area(
    "Your request",
    value="Help me prepare for my appointment.",
    height=100,
)


# -----------------------------
# Prepare Button
# -----------------------------

if st.button(
    "🩺 Prepare Me",
    type="primary",
    use_container_width=True,
):

    if uploaded_file is None:
        st.warning("Please upload your appointment document first.")

    elif not user_request.strip():
        st.warning("Please tell me what you would like help with.")

    else:

        # Save uploaded file to a temporary application-controlled location.
        # The patient never needs to know this path.
        suffix = Path(uploaded_file.name).suffix

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix,
        ) as temp_file:

            temp_file.write(uploaded_file.getvalue())
            temp_document_path = temp_file.name

        st.success("Document uploaded successfully.")

        # The document path is supplied internally to the agent.
        internal_request = f"""
User request:
{user_request}

Uploaded appointment document:
{temp_document_path}

Use the uploaded document as the primary source for
appointment-specific information.
"""

        with st.spinner("Preparing your appointment checklist..."):

            try:

                response = agent(internal_request)

                st.divider()

                st.subheader("✓ Your Appointment Preparation")

                response_text = str(response)

                # Hide internal temporary filesystem paths from the patient.
                response_text = response_text.replace(
                    temp_document_path,
                    "Your uploaded appointment document"
                )

                st.markdown(response_text)

            except Exception as e:

                error_text = str(e).lower()

                if "429" in error_text or "quota" in error_text:
                    st.error(
                        "The AI service has temporarily reached its request limit. "
                        "Please wait a moment and try again."
                    )
                else:
                    st.error(
                        "The agent could not complete the request. "
                        "Please try again."
                    )

                # Developer-only diagnostic information.
                with st.expander("Developer details"):
                    st.code(str(e))