# 🩺 Everyday Health Agent

An agentic healthcare appointment-preparation assistant built with **Strands Agents**, **Google Gemini**, and **Streamlit**.

The Everyday Health Agent helps users prepare for healthcare appointments by analyzing an uploaded appointment/referral document, retrieving general appointment-preparation guidance, generating a grounded checklist, and applying a healthcare safety review.

> **Hackathon prototype:** This project is designed for the Agents for Humans Hackathon and uses synthetic or public healthcare information only.

---

## 🎯 Problem

Preparing for a healthcare appointment can require patients to gather documents, medication and supplement information, appointment details, questions, and other instructions.

Important information may be distributed across appointment letters, referrals, and general preparation guidance. A useful assistant should be able to identify the appropriate tools for the user's request while keeping appointment-specific information grounded in the provided document.

---

## 💡 Solution

Everyday Health Agent uses an agentic workflow to:

1. Understand the user's request.
2. Analyze an uploaded appointment/referral document when relevant.
3. Retrieve general healthcare preparation information.
4. Generate an actionable preparation checklist.
5. Run a safety review.
6. Return a concise response that distinguishes document-specific information from general guidance.

The patient does **not** need to provide a file path or understand the underlying tools.

---

## 🏗️ Architecture

```text
                    ┌─────────────────────────┐
                    │        Patient          │
                    │ Upload + Natural Request│
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      Streamlit UI       │
                    │ Upload / Request / Result│
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      Strands Agent      │
                    │   Agentic Orchestration │
                    └────────────┬────────────┘
                                 │
                ┌────────────────┼────────────────┐
                │                │                │
                ▼                ▼                ▼
       ┌────────────────┐ ┌───────────────┐ ┌────────────────────┐
       │ Document Tool  │ │ Healthcare    │ │ Appointment        │
       │                │ │ Knowledge Tool│ │ Preparation Tool   │
       └────────────────┘ └───────────────┘ └────────────────────┘
                │                │                │
                └────────────────┼────────────────┘
                                 ▼
                       ┌──────────────────┐
                       │   Safety Check   │
                       └─────────┬────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ Grounded Patient Result │
                    │ Checklist + Sources     │
                    └─────────────────────────┘

                     Gemini 3.6 Flash
                     ↓
              Strands model provider
```

---

## 🤖 Agent Tools

### `document_tool`

Extracts structured information from a healthcare appointment document.

It identifies information such as:

- Appointment type
- Provider
- Date
- Time
- Reason for appointment
- Appointment-specific instructions

The prototype currently supports plain-text healthcare documents.

### `healthcare_knowledge`

Retrieves general appointment-preparation information from the local healthcare knowledge base.

This information is intentionally general and educational.

### `appointment_preparation`

Creates a practical appointment-preparation checklist using appointment-specific information and supported general preparation guidance.

### `safety_check`

Reviews the proposed response for potentially sensitive clinical requests and helps keep the response within the project's healthcare safety boundaries.

---

## 🔄 Example Agent Workflow

For an appointment-preparation request:

```text
User:
"Help me prepare for my appointment."

        ↓

Strands Agent
        ↓
Select appropriate tools
        ↓
Document Extraction
        ↓
Healthcare Knowledge Retrieval
        ↓
Appointment Checklist
        ↓
Safety Review
        ↓
Grounded Response
```

The application does not require the patient to manually select tools.

---

## 🧠 Grounding Strategy

The agent follows three information categories:

### 1. Document-Specific Information

Information extracted directly from the uploaded appointment document.

Examples:

- Provider
- Appointment date and time
- Appointment type
- Appointment-specific instructions

### 2. General Healthcare Guidance

Information retrieved from the local healthcare knowledge base.

### 3. Agent-Generated Organization

The structure used to organize the information into a readable checklist.

The agent is instructed not to invent appointment-specific facts. If information is unclear or potentially conflicts with general guidance, the user is directed to confirm it with the healthcare provider or healthcare facility.

---

## 🛡️ Healthcare Safety

This project is designed as a healthcare information-support prototype, not a clinical decision-making system.

The agent does **not**:

- Diagnose medical conditions
- Prescribe medication
- Recommend starting medication
- Recommend stopping medication
- Recommend changing medication
- Replace instructions from healthcare professionals

For diagnosis, treatment, medication decisions, or other clinical questions, users should consult a qualified healthcare professional.

---

## 🔐 Data Safety

This prototype is intended for:

- Synthetic healthcare information
- Public healthcare information

**Do not upload real patient-identifying information.**

The hackathon demonstration should use synthetic or anonymized demonstration documents.

---

## 🖥️ User Experience

The intended patient experience is simple:

```text
┌──────────────────────────────────────────────┐
│        🩺 Everyday Health Agent              │
│                                              │
│  Prepare for your healthcare appointment     │
│                                              │
│  Upload your appointment/referral document   │
│                                              │
│  What would you like help with?              │
│                                              │
│  "Help me prepare for my appointment."       │
│                                              │
│             [ 🩺 Prepare Me ]                │
└──────────────────────────────────────────────┘
```

The underlying temporary file path and implementation details are handled by the application and are not part of the patient-facing workflow.

---

## 🧪 Example

A synthetic appointment document can contain:

```text
Appointment Type: Cardiology Consultation
Provider: Dr. Taylor
Date: September 10, 2026
Time: 10:30 AM

Reason for Appointment:
Initial consultation regarding cardiovascular health.

Instructions:
Bring a current medication and supplement list.
Bring relevant previous medical records if available.
Bring your identification and insurance information.
Prepare questions or concerns you would like to discuss.
```

The agent can return:

- Appointment summary
- Appointment-specific instructions
- General preparation checklist
- Items to confirm with the provider
- Safety reminder
- Sources used

---

## ⚙️ Technology Stack

- **Python**
- **Strands Agents**
- **Google Gemini 3.6 Flash**
- **Streamlit**
- Python-based healthcare tools
- Local healthcare knowledge base

---

## 🚀 Setup

### 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd everyday-health-agent
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Set your API key as an environment variable.

Windows PowerShell:

```powershell
$env:GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
```

Do **not** commit API keys to GitHub.

### 5. Run the Streamlit application

```powershell
streamlit run streamlit_app.py
```

The application will open in your browser.

---

## 📁 Project Structure

```text
everyday-health-agent/
│
├── app.py
├── streamlit_app.py
├── orchestrator.py
├── requirements.txt
├── LICENSE
├── README.md
├── .gitignore
│
├── data/
│   ├── documents/
│   │   └── cardiology_appointment.txt
│   │
│   └── healthcare_knowledge/
│       └── appointment_preparation.txt
│
└── tools/
    ├── __init__.py
    ├── document_tool.py
    ├── healthcare_knowledge.py
    ├── appointment_tool.py
    └── safety_tool.py
```

---

## 📊 Evaluation Ideas

Potential evaluation metrics for future development include:

- Tool-selection accuracy
- Retrieval accuracy
- Response relevance
- Groundedness
- Unsupported-claim rate
- Unnecessary tool calls
- Latency
- Cost
- Safety-review performance

---

## 🔮 Future Improvements

Potential future enhancements include:

- PDF document extraction
- Additional healthcare document formats
- More specialized healthcare preparation tools
- Stronger retrieval and semantic search
- Automated evaluation datasets
- Production-grade authentication and privacy controls
- Deployment using cloud infrastructure
- More robust clinical-safety evaluation

These are future development directions and are not claims about the current prototype.

---

## 🏆 Hackathon Context

This project was created as a new AI agent prototype for the **Agents for Humans Hackathon**.

The project focuses on the Everyday Agents concept by applying agentic tool selection to a practical healthcare information-support workflow.

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE).

---

## ⚠️ Disclaimer

Everyday Health Agent is a prototype for educational and demonstration purposes. It does not provide medical diagnosis, treatment, or medication recommendations and should not replace advice from a qualified healthcare professional.
