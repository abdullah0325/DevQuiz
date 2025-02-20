
import streamlit as st
import requests

# FastAPI Backend URL
API_URL = "http://127.0.0.1:8000/"  # Update if deployed

# List of programming languages
LANGUAGES = ["Python", "Java", "C++", "JavaScript", "Go", "Rust", "Swift", "Kotlin", "PHP"]

# Sidebar for Navigation
st.sidebar.title("⚙️ Settings")
language = st.sidebar.selectbox("Select Language", LANGUAGES)

# Initialize session state
if "mcqs" not in st.session_state:
    st.session_state.mcqs = []
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False

# Fetch MCQs from FastAPI
if st.sidebar.button("Generate Quiz"):
    st.session_state.quiz_submitted = False  # Reset submission status
    st.session_state.user_answers = {}  # Reset previous answers
    with st.spinner("Fetching MCQs..."):
        try:
            response = requests.get(API_URL, params={"language": language})
            response.raise_for_status()
            st.session_state.mcqs = response.json()

            if not st.session_state.mcqs:
                st.warning("⚠️ No MCQs available. Try another language.")
            else:
                st.success(f"✅ Quiz for {language} generated! Answer the questions below.")
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Error fetching MCQs: {e}")

# Title & UI Styling
st.markdown(
    """
    <style>
        body { font-family: 'Arial', sans-serif; }
        .mcq-card {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 10px;
        }
        .correct-answer {
            color: green;
            font-weight: bold;
        }
        .wrong-answer {
            color: red;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("📚 MCQ Quiz Generator")
st.write("Generate and attempt quizzes for different programming languages.")

# Display Quiz
if st.session_state.mcqs:
    st.subheader(f"📝 Quiz: {language}")

    for idx, mcq in enumerate(st.session_state.mcqs):
        st.write(f"**{idx+1}. {mcq['question']}**")
        options = mcq["options"]

        # Store user's selected answer
        st.session_state.user_answers[idx] = st.radio(
            f"Select an answer for Question {idx+1}",
            options,
            key=f"q{idx}"
        )

    # Submit Button
    if st.button("Submit Quiz"):
        st.session_state.quiz_submitted = True  # Mark quiz as submitted

# Display Results After Submission
if st.session_state.quiz_submitted:
    correct_count = 0
    st.subheader("🎯 Quiz Results")

    for idx, mcq in enumerate(st.session_state.mcqs):
        user_choice = st.session_state.user_answers.get(idx, "No Answer")
        correct_answer = mcq["correct_answer"]

        st.write(f"**{idx+1}. {mcq['question']}**")

        if user_choice == correct_answer:
            correct_count += 1
            st.success(f"✅ Your answer: {user_choice} (Correct)")
        else:
            st.error(f"❌ Your answer: {user_choice} (Incorrect)")
            st.info(f"✅ Correct answer: {correct_answer}")

    # Show final score
    total_questions = len(st.session_state.mcqs)
    score = (correct_count / total_questions) * 100
    st.subheader(f"🏆 Your Score: {correct_count}/{total_questions} ({score:.2f}%)")

