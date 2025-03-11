import base64
import time # for the time
import streamlit as st # for web interface
import random #to pick question randomly


    # Pick a random question from the list
st.title("📝Quiz Application")
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    return encoded_string

# Adding fox image as background (LEFT SIDE)
fox_image_base64 = get_base64_image("quiz.jpg")  # Use uploaded file

st.markdown(
    f"""
    <style>
    .stApp {{
        background: url("data:image/png;base64,{fox_image_base64}") no-repeat left center;
        background-size: cover; /* Ensures full screen */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Define a list of questions and answers


questions = [
    {
        "question": "Which programming language is known as the ‘mother of all languages’?",
        "options": ["Python", "C", "Java", "Assembly"],
        "answer": "C"
    },
    {
        "question": "What does HTML stand for?",
        "options": ["Hyper Text Markup Language", "High Tech Modern Language", "Hyperlink and Text Management Language", "Home Tool Markup Language"],
        "answer": "Hyper Text Markup Language"
    },
    {
        "question": "Who is the founder of Microsoft?",
        "options": ["Steve Jobs", "Elon Musk", "Bill Gates", "Mark Zuckerberg"],
        "answer": "Bill Gates"
    },
    {
        "question": "What does ‘RAM’ stand for in computing?",
        "options": ["Random Access Memory", "Readable Access Memory", "Real-time Application Machine", "Rapid Allocation Memory"],
        "answer": "Random Access Memory"
    },
    {
        "question": "What year was the first iPhone released?",
        "options": ["2005", "2007", "2010", "2012"],
        "answer": "2007"
    },
    {
        "question": "Which of the following is NOT a database management system?",
        "options": ["MySQL", "PostgreSQL", "MongoDB", "ReactJS"],
        "answer": "ReactJS"
    },
    {
        "question": "What is the main function of an Operating System?",
        "options": ["To display websites", "To manage hardware and software resources", "To design graphics", "To write documents"],
        "answer": "To manage hardware and software resources"
    },
    {
        "question": "Which company developed the Java programming language?",
        "options": ["Microsoft", "Sun Microsystems", "Google", "Apple"],
        "answer": "Sun Microsystems"
    },
    {
        "question": "What does CSS stand for?",
        "options": ["Computer Styling System", "Cascading Style Sheets", "Code Styling Structure", "Creative Sheet System"],
        "answer": "Cascading Style Sheets"
    },
    {
        "question": "Which of these is a version control system?",
        "options": ["Git", "Docker", "Kubernetes", "Jenkins"],
        "answer": "Git"
    }
]

# to store browser memory in ts we use STATES but in python using streamlit we use st.session_state (funtion) to sore data in broweser

if "current_question" not in st.session_state:
    # to chhose random question
    st.session_state.current_question = random.choice(questions)


# to display question and answer
question= st.session_state.current_question


# to display selected option and check answer
st.subheader(question["question"])

selected_option = st.radio("🤔Choose your Option",question["options"],key="answer")

# to check and display result
if st.button("✅Submit Answer"):
    
    if selected_option == question["answer"]:
        st.success("✅ Correct! You've earned 1 point")
        st.balloons()
    else:
        st.error("❌ Incorrect! the Correct answer is: " + question["answer"])
    st.session_state.current_question = random.choice(questions)

    time.sleep(5)
    st.session_state.current_question =random.choice(questions)
    # to display the next questions
    st.rerun()