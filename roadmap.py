import streamlit as st

# Roadmap dictionary
roadmap = {
    "Computer Science": {
        1: ["Learn Python basics", "Start with Git & GitHub"],
        2: ["Data Structures & Algorithms", "SQL & Databases"],
        3: ["Web Development (HTML, CSS, JS)", "Linux basics"],
        4: ["Machine Learning basics", "OOP in Java/C++"],
        5: ["Deep Learning (TensorFlow/PyTorch)", "Cloud basics (AWS/GCP)"],
        6: ["AI/ML projects", "Cybersecurity fundamentals"],
        7: ["Advanced AI topics (NLP, CV)", "DevOps tools"],
        8: ["Capstone project", "Entrepreneurship & Startup skills"]
    },
    "Electronics": {
        1: ["Basic Electronics", "C Programming"],
        2: ["Digital Logic Design", "MATLAB basics"],
        3: ["Microcontrollers (Arduino)", "PCB Design"],
        4: ["Embedded Systems", "IoT basics"],
        5: ["VLSI Design", "Signal Processing"],
        6: ["Robotics basics", "Wireless Communication"],
        7: ["AI for Electronics", "FPGA programming"],
        8: ["Capstone project", "Startup & Innovation"]
    }
    # Later we’ll add Mechanical, Civil
}

# Streamlit UI
st.title("AI-Powered Student Skill Recommender")

branch = st.selectbox("Select your branch:", list(roadmap.keys()))
semester = st.slider("Select your semester:", 1, 8, 1)

# Recommendation logic
skills = roadmap[branch].get(semester, ["No roadmap available yet."])

st.subheader("Recommended Skills:")
for skill in skills:
    st.write("- " + skill)
