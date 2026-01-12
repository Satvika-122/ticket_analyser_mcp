# 🧠 AI Ticket Analyzer (MCP-Based Agentic AI)

A client–server **AI Ticket Analyzer** built using **FastAPI**, **Streamlit**, and **Model Context Protocol (MCP)**.  
This system analyzes customer support tickets using **multiple collaborating AI agents** with a shared context, ensuring modularity, reliability, and explainability.

---

## 🚀 Live Demo

👉 **Streamlit App (Live):**  
https://satvika-122-ticket-analyser-mcp-app-mcp-client-server-l92cug.streamlit.app/

---

## 🏗️ Architecture Overview

Streamlit (Client UI)
|
| HTTP POST /analyze
↓
FastAPI Server
|
↓
MCP Orchestrator
|
├── Classification Agent
├── Entity Extraction Agent
├── Summary Agent
└── QA / Validation Agent
|
↓
Shared TicketContext (MCP)
|
↓
JSON Response → Streamlit UI


---

## 🤖 Key Features

- Client–Server architecture (Streamlit + FastAPI)
- Model Context Protocol (MCP) for agent coordination
- Modular agent-based AI design
- Hybrid AI (rule-based + LLM fallback)
- Internal QA and confidence validation
- Clean and interactive Streamlit UI
- Production-ready backend structure

---

## 🧩 MCP Agents

| Agent | Responsibility |
|------|----------------|
| ClassificationAgent | Classifies tickets into Payment, Account, Technical, Delivery, or Other |
| EntityAgent | Extracts entities like Order ID, Transaction ID, Email, Phone |
| SummaryAgent | Generates structured natural-language summaries |
| QAAgent | Validates outputs and assigns confidence (internal use only) |

---

## 🧠 Model Context Protocol (MCP)

All agents operate on a **shared TicketContext**, enabling:

- Structured state sharing across agents  
- Deterministic and traceable execution  
- Explainable reasoning  
- Easy extensibility (RAG, HITL, streaming)  

Each agent:
- Reads required fields from context  
- Updates only its responsible fields  
- Returns the updated context  

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** FastAPI  
- **AI Models:**  
  - `google/flan-t5-base` (classification)  
  - `dslim/bert-base-NER` (entity extraction)  
- **Protocol:** Model Context Protocol (MCP)  
- **Database:** SQLite (local demo storage)  
- **Language:** Python  

---

## ▶️ How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/Satvika-122/ticket_analyser_mcp.git
cd ticket_analyser_mcp
###2. Create and Activate Virtual Environment
python -m venv venv
.\venv\Scripts\Activate.ps1

###3. Install Dependencies
pip install -r requirements.txt

4. Start FastAPI Server
uvicorn backend.main:app --reload


Open in browser:

http://127.0.0.1:8000/docs

5. Start Streamlit Client
streamlit run app.py

🧪 Sample Input
My payment was deducted but order ID 12345 was not confirmed.

Sample Output

Category: Payment Issue

Entities: ORDER_ID → 12345

Summary:
Customer reports a payment-related issue, associated with order ID 12345.

🔐 Validation Strategy

QA agent runs internally in the backend

Confidence scores are stored but not displayed in UI

Prevents unreliable AI outputs

Supports future Human-in-the-Loop workflows

📌 Why This Project Matters

This project demonstrates:

Agentic AI system design

Clean separation of UI and intelligence

Safe AI practices with validation and fallbacks

Scalable architecture suitable for real-world support systems

👩‍💻 Author

Satvika Dwaram
AI & Data Science Undergraduate
Agentic AI | GenAI | MCP Systems

GitHub: https://github.com/Satvika-122

📜 License

This project is intended for educational and demonstration purposes.

🚀 Future Enhancements

Retrieval-Augmented Generation (RAG)

Human-in-the-Loop workflows

Cloud deployment (AWS / GCP / Hugging Face)

Real-time streaming responses


---

✅ **Ready to paste**  
✅ **Live link included**  
✅ **Recruiter & interview ready**

If you want next, I can:
- Add **screenshots section**
- Write **resume bullet points**
- Prepare a **2-minute demo explanation**
- Add **architecture diagram**

Just say **“next”** 🚀alyser_mcp/Ticket_Analyser
