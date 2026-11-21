
import streamlit as st
from chatbot import get_ai_response
from emergency import detect_emergency

st.set_page_config(
    page_title="Symptom Information Bot",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    .stApp {
        background: #f5f8fc;
    }

    .main .block-container {
        max-width: 1050px;
        padding-top: 2rem;
    }

    .hero {
        background: linear-gradient(120deg, #0b4f71, #168aad);
        padding: 1.6rem 1.8rem;
        border-radius: 18px;
        color: white;
        margin-bottom: 1.2rem;
    }

    .hero h1 {
        color: white;
        margin: 0;
        font-size: 2rem;
    }

    .hero p {
        color: #e8f6fb;
        margin: .45rem 0 0 0;
    }

    .notice {
        background: #fff8e6;
        border-left: 5px solid #e0a326;
        padding: .9rem 1rem;
        border-radius: 8px;
        color: #553f0b;
        margin: 1rem 0;
    }

    .small-muted {
        color: #64748b;
        font-size: .88rem;
    }
</style>
""", unsafe_allow_html=True)


with st.sidebar:
    st.title("🩺 Symptom Bot")
    st.caption("Roll No. 56 | GenAI Mini Project")

    st.markdown("---")

    st.subheader("About this project")

    st.write(
        "An educational chatbot that provides general symptom "
        "information and suggests an appropriate type of "
        "healthcare professional."
    )

    st.markdown("---")

    st.subheader("Safety first")

    st.write(
        "This tool cannot diagnose, assess your personal risk, "
        "or replace a qualified healthcare professional."
    )

    if st.button("🗑️ Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.caption("Built with Python, Streamlit and Google Gemini.")


st.markdown("""
<div class="hero">
    <h1>Symptom Information Bot</h1>
    <p>
        Understand symptoms in simple language and learn which
        healthcare professional may be appropriate.
    </p>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="notice">
    <strong>Medical information notice:</strong>
    This chatbot provides general educational information only.
    It does not diagnose conditions, prescribe treatment, or replace
    professional medical advice. For personal concerns, contact a
    qualified healthcare professional. If you think someone may be
    experiencing a medical emergency, contact local emergency
    services immediately.
</div>
""", unsafe_allow_html=True)


with st.expander("How to use this chatbot"):
    st.markdown("""
    1. Describe the symptom(s), how long they have been present,
       and any relevant context.
    2. Do not include your full name, address, phone number,
       or other identifying details.
    3. Read the general information and specialist suggestion.
    4. Contact a healthcare professional for advice about your
       own situation.
    """)


if "messages" not in st.session_state:
    st.session_state.messages = []


st.subheader("Ask about a symptom")


examples = [
    "What general information is available about a mild headache?",
    "I have had a sore throat and cough for two days. What type of doctor should I consult?",
    "What does recurring heartburn generally mean?"
]


cols = st.columns(len(examples))

for i, example in enumerate(examples):
    if cols[i].button(f"Example {i+1}", use_container_width=True):
        st.session_state.pending_prompt = example


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


user_prompt = st.chat_input(
    "Describe your symptom in your own words..."
)


if "pending_prompt" in st.session_state:
    user_prompt = st.session_state.pop("pending_prompt")


if user_prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": user_prompt
    })

    with st.chat_message("user"):
        st.markdown(user_prompt)


    emergency_result = detect_emergency(user_prompt)


    with st.chat_message("assistant"):

        if emergency_result["flagged"]:

            answer = (
                "**⚠️ POTENTIAL MEDICAL EMERGENCY**\n\n"
                "Your message contains wording that may be associated "
                "with a medical emergency.\n\n"
                "**Please contact local emergency services or go to "
                "the nearest emergency department immediately.** "
                "Do not wait for an online chatbot response.\n\n"
                "This is a precautionary safety alert, not a diagnosis. "
                "The chatbot cannot determine whether a symptom is safe."
            )

            st.error(answer)

        else:

            with st.spinner("Preparing general information..."):

                try:

                    answer = get_ai_response(
                        user_prompt=user_prompt,
                        conversation=st.session_state.messages[:-1]
                    )

                except Exception:
                    answer = (
                        "I couldn't connect to the AI service. "
                        "Please check your Gemini API key, internet "
                        "connection, and model availability. "
                        "Please try again later or consult a "
                        "qualified healthcare professional."
                    )

            st.markdown(answer)


    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })


st.markdown("---")

st.markdown(
    '<p class="small-muted">'
    'For education only • Not a diagnostic tool • '
    'Do not use this app to decide whether emergency care is needed.'
    '</p>',
    unsafe_allow_html=True
)
