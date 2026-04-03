import streamlit as st
import ollama

# ================= PAGE CONFIG =================
st.set_page_config(page_title="LabSync AI", layout="wide")

st.title("🚀 LabSync AI Agent")

# ================= STREAM FUNCTION =================
def stream_ai(prompt):
    response = ollama.chat(
        model="phi3",  # ⚡ faster model
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )

    output = ""
    placeholder = st.empty()

    for chunk in response:
        content = chunk['message']['content']
        output += content
        placeholder.markdown(output)

    return output

# ================= TABS =================
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["📘 Notes", "🧠 Planner", "💻 Code Analyzer", "⚙️ Code Generator", "💬 Chat"]
)

# ================= TAB 1: NOTES =================
with tab1:
    topic = st.text_input("Enter Topic")

    if topic:
        col1, col2, col3, col4 = st.columns(4)

        if col1.button("Notes"):
            st.subheader("📘 Notes")
            stream_ai(f"Explain {topic} with definition, parts, working, and applications.")
            st.code("Start → Input → Process → Output → End")

        if col2.button("Article"):
            st.subheader("📰 Article")
            stream_ai(f"Write a detailed article on {topic}.")

        if col3.button("Essay"):
            st.subheader("📝 Essay")
            stream_ai(f"Write an academic essay on {topic} with introduction, body, and conclusion.")

        if col4.button("Summary"):
            st.subheader("📄 Summary")
            stream_ai(f"Give a short bullet-point summary of {topic}.")

# ================= TAB 2: PLANNER =================
with tab2:
    plan = st.text_area("Enter your project / idea")

    if st.button("Generate Plan"):
        if plan:
            st.subheader("🕒 Smart Plan")
            stream_ai(f"Create a step-by-step hourly plan for {plan}.")
            st.code("Idea → Research → Design → Develop → Test → Improve")

# ================= TAB 3: CODE ANALYZER =================
with tab3:
    code = st.text_area("Paste your code")

    if st.button("Analyze Code"):
        if code:
            st.subheader("💻 Code Analysis")
            stream_ai(f"Analyze this code:\n{code}\nExplain errors and fixes.")

# ================= TAB 4: CODE GENERATOR =================
with tab4:
    code_topic = st.text_input("Enter topic for code")
    lang = st.selectbox("Language", ["Python", "Java", "C++"])

    if st.button("Generate Code"):
        if code_topic:
            st.subheader("💻 Generated Code")
            stream_ai(f"Generate a {lang} program for {code_topic} with comments.")

# ================= TAB 5: CHAT =================
with tab5:
    user_msg = st.text_input("Ask anything")

    if st.button("Send"):
        if user_msg:
            st.subheader("💬 AI Response")
            stream_ai(f"Answer clearly: {user_msg}")