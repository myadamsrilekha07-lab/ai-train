import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="AI Fake Customer Simulator",
    page_icon="🤖"
)

st.title("🤖 AI Fake Customer Simulator")

st.write(
    "The AI Customer and AI Support Agent will automatically "
    "have a conversation."
)

# Customer type
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

# Number of conversation turns
turns = st.slider(
    "Number of Conversation Turns",
    min_value=4,
    max_value=20,
    value=10
)

# Start conversation
if st.button("▶️ Start Conversation"):

    st.subheader("💬 AI-to-AI Conversation")

    # Connect to Groq using the API key stored in Streamlit Secrets
    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )

    # First customer message
    customer_prompt = (
        "You are a "
        + customer_type
        + " contacting customer support. "
        "Start a realistic customer-service complaint. "
        "Keep it natural and conversational. "
        "Do not say you are an AI. "
        "Do not use 'Customer:' as a label."
    )

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": customer_prompt
            }
        ]
    )

    customer_message = response.choices[0].message.content

    # Conversation loop
    for i in range(turns):

        # Customer
        st.markdown("### 🤖 AI Customer")
        st.info(customer_message)

        # Support Agent
        support_prompt = (
            "You are a professional customer-support agent. "
            "Respond naturally to the customer's message. "
            "Be polite, helpful and professional. "
            "Try to solve the customer's problem. "
            "Ask for information when necessary. "
            "Do not say you are an AI. "
            "Do not use 'Support Agent:' as a label.\n\n"
            "Customer message:\n"
            + customer_message
        )

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": support_prompt
                }
            ]
        )

        support_message = response.choices[0].message.content

        st.markdown("### 🤖 AI Support Agent")
        st.success(support_message)

        # Customer responds again
        if i < turns - 1:

            next_customer_prompt = (
                "You are a "
                + customer_type
                + " customer. "
                "Continue the conversation naturally. "
                "Respond to the support agent's message. "
                "You can ask questions, show frustration, "
                "provide information, accept the solution, "
                "or thank the support agent. "
                "Keep the conversation realistic. "
                "Do not say you are an AI. "
                "Do not use 'Customer:' as a label.\n\n"
                "Support Agent message:\n"
                + support_message
            )

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "user",
                        "content": next_customer_prompt
                    }
                ]
            )

            customer_message = response.choices[0].message.content

    st.success("✅ Conversation completed!")

