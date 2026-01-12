# app.py
import streamlit as st
import requests
from db import init_db, insert_ticket, fetch_all_tickets

# -------------------------
# Page setup
# -------------------------
st.set_page_config(page_title="AI Ticket Analyzer", layout="centered")

# Initialize database
init_db()

st.title("🧠 AI Ticket Analyzer (Agentic AI + MCP)")
st.write(
    "Paste a customer support ticket below to analyze it using a "
    "client–server MCP-based agentic AI system."
)

# -------------------------
# Input
# -------------------------
ticket_text = st.text_area(
    "Support Ticket",
    height=200,
    placeholder="Example: My payment was deducted but order ID 12345 was not confirmed..."
)

# -------------------------
# Analyze Button
# -------------------------
if st.button("Analyze Ticket"):
    if not ticket_text.strip():
        st.warning("Please enter a ticket.")
    else:
        with st.spinner("Analyzing using MCP agent pipeline..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/analyze",
                    json={"text": ticket_text},
                    timeout=60
                )
                response.raise_for_status()
                result = response.json()
            except Exception as e:
                st.error(f"Backend error: {e}")
                st.stop()

        # -------------------------
        # Extract QA info (HIDDEN from UI)
        # -------------------------
        qa = result.get("qa_validation", {})

        # -------------------------
        # Store result in DB
        # -------------------------
        insert_ticket(
            ticket_text=ticket_text,
            category=result.get("category"),
            entities=result.get("entities"),
            summary=result.get("summary"),
            validated=qa.get("valid", False),
            confidence=qa.get("confidence", 0.0)
        )

        st.success("Analysis Complete")

        # -------------------------
        # Display Results (NO validation shown)
        # -------------------------
        st.subheader("📌 Category")
        st.write(result.get("category"))

        st.subheader("🔍 Extracted Entities")
        st.json(result.get("entities", []))

        st.subheader("📝 Summary")
        st.write(result.get("summary"))

# -------------------------
# Stored Tickets Section
# -------------------------
st.divider()
st.subheader("📦 Stored Tickets (Demo History)")

rows = fetch_all_tickets()

if rows:
    for row in rows:
        st.markdown(
            f"""
            **Ticket ID:** {row[0]}  
            **Category:** {row[2]}  
            **Summary:** {row[4]}
            """
        )
else:
    st.info("No tickets stored yet.")
