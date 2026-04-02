import streamlit as st

st.title("LabSync AI Agent")

# Inputs
user_input = st.text_area("Paste your code here")
plan_input = st.text_area("Enter your project idea / plan")

if st.button("Generate"):

    # ================= IDEA GENERATOR =================
    if plan_input:
        plan = plan_input.lower()

        if "student" in plan:
            ideas = [
                "Add login system",
                "Track student progress",
                "Include reminders",
                "Add performance dashboard"
            ]
        elif "app" in plan:
            ideas = [
                "Improve UI/UX",
                "Add authentication",
                "Optimize performance",
                "Add notifications"
            ]
        elif "ai" in plan:
            ideas = [
                "Use ML models",
                "Improve accuracy",
                "Add real-time predictions",
                "Smart recommendations"
            ]
        else:
            ideas = [
                "Define clear problem",
                "Add unique feature",
                "Improve usability",
                "Focus on user experience"
            ]
    else:
        ideas = ["No plan provided"]

    # ================= SMART TIME PLANNER =================
    if plan_input:
        if "ai" in plan:
            schedule = [
                "Research AI concepts → 1 hour",
                "Plan model logic → 1 hour",
                "Implement core functionality → 2 hours",
                "Test and debug → 1 hour",
                "Optimize and improve → 1 hour"
            ]
        elif "app" in plan:
            schedule = [
                "Define app features → 1 hour",
                "Design UI layout → 1 hour",
                "Develop main functionality → 2 hours",
                "Test application → 1 hour",
                "Improve UI/UX → 1 hour"
            ]
        elif "student" in plan:
            schedule = [
                "Understand requirements → 1 hour",
                "Plan structure → 1 hour",
                "Develop modules → 2 hours",
                "Test functionality → 1 hour",
                "Final review → 1 hour"
            ]
        else:
            schedule = [
                "Understand problem → 30 minutes",
                "Plan solution → 1 hour",
                "Implement code → 2 hours",
                "Test output → 30 minutes",
                "Improve logic → 1 hour"
            ]
    else:
        schedule = ["No plan provided"]

    # ================= LANGUAGE DETECTION =================
    if "print" in user_input and "def" not in user_input:
        lang = "Python"
    elif "class" in user_input:
        lang = "Java"
    else:
        lang = "Programming"

    # ================= ALGORITHM DETECTION =================
    if "if" in user_input:
        algorithm = [
            "Start",
            "Check condition",
            "Execute if block",
            "Stop"
        ]
    elif "for" in user_input or "while" in user_input:
        algorithm = [
            "Start",
            "Initialize loop",
            "Check condition",
            "Execute loop body",
            "Repeat until condition fails",
            "Stop"
        ]
    elif "print" in user_input:
        algorithm = [
            "Start",
            "Write print statement",
            "Execute program",
            "Display output",
            "Stop"
        ]
    else:
        algorithm = [
            "Start",
            "Write program logic",
            "Execute program",
            "Display result",
            "Stop"
        ]

    # ================= ERROR DETECTION =================
    if "if" in user_input and ":" not in user_input:
        error_msg = "⚠️ Syntax error detected: Missing ':' in if statement."
    else:
        error_msg = "✅ No major syntax errors detected."

    # ================= RESULT & CONCLUSION =================
    if "⚠️" in error_msg:
        result = "The program contains errors and did not execute successfully."
        conclusion = f"The {lang} program needs correction before successful execution."
    else:
        result = "The program was successfully executed and expected output was obtained."
        conclusion = f"The given problem is successfully implemented using {lang}."

    # ================= OUTPUT =================

    # Idea Suggestions
    st.subheader("Project Idea Suggestions")
    for idea in ideas:
        st.write("• " + idea)

    # Time Planner
    st.subheader("Smart TODO Planner (Time-based)")
    for task in schedule:
        st.write("• " + task)

    # Code Explanation
    st.subheader("Code Explanation")
    st.write(f"This is a {lang} program demonstrating basic logic and execution flow.")

    # Error Detection
    st.subheader("Error Detection")
    st.write(error_msg)

    # Lab Record
    st.subheader("Lab Record")
    st.write("**Aim:** To write and execute a program.")
    st.write(f"**Objective:** To understand logic using {lang}.")

    st.write("**Algorithm:**")
    for step in algorithm:
        st.write("• " + step)

    st.write("**Program:**")
    st.code(user_input)

    st.write("**Explanation:**")
    st.write(f"This program demonstrates key {lang} concepts.")

    st.write("**Result:**")
    st.write(result)

    st.write("**Conclusion:**")
    st.write(conclusion)

    st.write("**Viva Questions:**")
    st.write("• What is the purpose of this program?")
    st.write("• What concepts are used?")
    st.write("• How can it be improved?")

    # TODO Suggestions
    st.subheader("TODO Suggestions")
    todos = [
        "Fix syntax errors",
        "Improve readability",
        "Add comments",
        "Optimize logic"
    ]
    for t in todos:
        st.write("• " + t)

    # Resume Output
    st.subheader("Resume Output")
    resume = [
        f"Developed a {lang} based application",
        "Improved problem-solving and debugging skills"
    ]
    for r in resume:
        st.write("• " + r)