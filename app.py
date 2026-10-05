import streamlit as st

st.set_page_config(
    page_title="AI Fake Customer Simulator",
    page_icon="🤖"
)

st.title("🤖 AI Fake Customer Simulator")
st.write("Practice handling different customer complaints.")

customers = {
    "Angry Customer": {
        "customer": "My order is very late! I ordered it 5 days ago. This is really frustrating!",
        "suggestions": [
            "I sincerely apologize for the delay. Let me check the status of your order.",
            "I'm sorry for the inconvenience. I understand how frustrating this must be.",
            "I apologize for the delay. I'll help you track your order and find a solution."
        ]
    },

    "Refund Customer": {
        "customer": "I received a damaged product and I want my money back.",
        "suggestions": [
            "I'm sorry that you received a damaged product. I'll help you with the refund process.",
            "I apologize for the problem. Please share your order details so I can assist with your refund.",
            "I'm sorry about this experience. We can check the order and arrange a replacement or refund."
        ]
    },

    "Wrong Product Customer": {
        "customer": "I ordered a black shirt, but you sent me a red shirt. What should I do?",
        "suggestions": [
            "I'm sorry for the mistake. I'll help you arrange a replacement for the correct product.",
            "I apologize for sending the wrong item. Please share your order number so we can fix this.",
            "Sorry about the mix-up. We'll check your order and help you get the correct shirt."
        ]
    },

    "Payment Problem Customer": {
        "customer": "Money was deducted from my account, but my order was not placed.",
        "suggestions": [
            "I'm sorry for the trouble. Let me help you check the payment and order status.",
            "I understand your concern. Please share the transaction details so we can investigate.",
            "Don't worry. I'll help you check whether the payment was successful and guide you through the next step."
        ]
    }
}

customer_type = st.selectbox(
    "Choose a customer:",
    list(customers.keys())
)

data = customers[customer_type]

st.subheader("👤 Customer")
st.info(data["customer"])

st.subheader("🤖 AI Suggested Responses")

for i, suggestion in enumerate(data["suggestions"], 1):
    st.write(f"Suggestion {i}: {suggestion}")

st.divider()

st.subheader("💬 Your Response")

user_response = st.text_area(
    "Type your response to the customer:"
)

if st.button("Submit Response"):
    if user_response.strip():
        st.success("Good response! Keep the customer calm and provide a solution.")
        st.write("Your response:", user_response)
    else:
        st.warning("Please type a response first.")