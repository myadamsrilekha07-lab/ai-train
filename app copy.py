import streamlit as st
import ollama


st.set_page_config(
    page_title="AI Fake Customer Simulator",
    page_icon="🤖"
)

st.title("🤖 AI Fake Customer Simulator")

st.write(
    "Practice handling a customer complaint. "
    "The AI acts as the customer and you act as the customer-support agent."
)


customer_type = st.selectbox(
    "Select Customer Type",
    [
        "Angry Customer 😠",
        "Polite Customer 🙂",
        "Confused Customer 😕",
        "Impatient Customer 😤"
    ]
)

problem = st.selectbox(
    "Select Customer Problem",
    [
        "Late Delivery",
        "Refund Request",
        "Damaged Product",
        "Wrong Product"
    ]
)


if "conversation" not in st.session_state:
    st.session_state.conversation = []

if "started" not in st.session_state:
    st.session_state.started = False



if st.button("🚀 Start Conversation"):

    st.session_state.conversation = []
    st.session_state.started = True

    prompt = f"""
You are a real customer.

Customer type: {customer_type}
Customer problem: {problem}

Start a customer-service conversation.

Give ONLY the customer's first message.

Example style:
"I ordered a laptop seven days ago, but it still hasn't arrived.
I really need it urgently. Can you please check my order?"

Do not give a solution.
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    customer_message = response["message"]["content"]

    st.session_state.conversation.append(
        ("AI Customer", customer_message)
    )



if st.session_state.started:

    st.subheader("💬 Conversation")

    for speaker, message in st.session_state.conversation:

        if speaker == "AI Customer":
            st.info("👤 **AI Customer:**\n\n" + message)

        else:
            st.success("👩‍💻 **You (Support Agent):**\n\n" + message)


    
    user_message = st.text_input(
        "👩‍💻 Enter your response:",
        key="user_input"
    )

    if st.button("📨 Send Response"):

        if user_message.strip() == "":
            st.warning("Please enter a response.")

        else:

           
            st.session_state.conversation.append(
                ("You", user_message)
            )

            
            history = ""

            for speaker, message in st.session_state.conversation:

                history += f"{speaker}: {message}\n"


          
            prompt = f"""
You are the CUSTOMER in a customer-service training simulator.

Customer type:
{customer_type}

Customer problem:
{problem}

Here is the conversation:

{history}

The support agent has just replied.

Continue the conversation as the CUSTOMER.

Rules:
- You are NOT the support agent.
- Stay as the customer.
- React naturally to the agent's response.
- If the agent is helpful, become calmer.
- If the agent is rude or unhelpful, become more frustrated.
- Keep your response short.
"""

            response = ollama.chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            customer_reply = response["message"]["content"]

            st.session_state.conversation.append(
                ("AI Customer", customer_reply)
            )

            st.rerun()