import streamlit as st
import pickle
import numpy as np

# Page config
st.set_page_config(page_title="Mental Health AI", page_icon="🧠", layout="centered")

# Custom CSS (THIS MAKES IT BEAUTIFUL 🔥)
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #667eea, #764ba2);
}
.main {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 15px;
}
h1 {
    text-align: center;
    color: #4b0082;
}
.stButton>button {
    background-color: #6a11cb;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Title
st.markdown("<h1>🧠 Mental Health Risk Detector</h1>", unsafe_allow_html=True)

st.write("### 💬 Tell me how you feel today")

# Inputs
text = st.text_area("Enter your thoughts")

col1, col2 = st.columns(2)
with col1:
    sleep = st.slider("😴 Sleep Hours", 0, 12, 6)
with col2:
    screen = st.slider("📱 Screen Time (hrs)", 0, 12, 5)

# Button
if st.button("🔍 Analyze My Mental State"):
    text_vec = vectorizer.transform([text]).toarray()
    input_data = np.hstack((text_vec, [[sleep, screen]]))
    
    result = model.predict(input_data)

    # Output styling
    if result[0] == "High":
        st.error("⚠️ High Stress Detected")
        st.write("👉 Try reducing screen time & improving sleep")
    elif result[0] == "Medium":
        st.warning("⚡ Medium Stress Level")
        st.write("👉 Take breaks and relax")
    else:
        st.success("😊 You are doing well!")
