import streamlit as st
import ollama

st.set_page_config(
    page_title="AI Fake Customer Simulator",
    page_icon="🤖"
)

st.title("🤖 AI Fake Customer Simulator")

st.write(
    "Practice customer-support conversations using two AI agents. "
    "The Customer AI and Support Agent AI will automatically talk to each other."
)

customer_type = st.selectbox(
    "Select Customer Type",
    [
        "Angry Customer",
        "Polite Customer",
        "Confused Customer",
        "Impatient Customer",
        "Frustrated Customer"
    ]
)

turns = st.slider(
    "Number of Conversation Turns",
    min_value=4,
    max_value=20,
    value=10
)

if st.button("▶️ Start Conversation"):

    st.subheader("💬 AI-to-AI Conversation")

    # First message from Customer AI
    customer_prompt = f"""
You are a {customer_type} contacting customer support.

Start a realistic customer-service conversation.

Create a customer complaint or problem.
Keep the message natural and conversational.

Do not say that you are an AI.
Do not include "Customer:".
"""

    customer_response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": customer_prompt
            }
        ]
    )

    customer_message = customer_response["message"]["content"]

    # Conversation loop
    for i in range(turns):

        # Customer
        st.markdown("### 🤖 AI Customer")
        st.info(customer_message)

        
