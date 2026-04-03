# mental-health-ai
AI-based Mental Health Risk Detection system using NLP and behavioral data (sleep &amp; screen usage) to predict stress levels
🚀 Project Overview

This project aims to detect early signs of stress or mental health risk in students by analyzing:

📝 User text input (thoughts/messages)
😴 Sleep duration
📱 Screen time

The system classifies risk levels into:

✅ Low
⚡ Medium
⚠️ High
🧠 Technologies Used
Python
Scikit-learn
Streamlit
Pandas
NumPy
⚙️ Features
🔍 Text analysis using NLP (TF-IDF)
📊 Behavioral data analysis (sleep & screen time)
🤖 Machine Learning model (classification)
🖥️ Interactive web interface (Streamlit)
🎨 Aesthetic and user-friendly UI
📁 Project Structure
mental_health_ai/
│── app.py
│── model.py
│── data.csv
│── README.md
▶️ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/sharau09/mental-health-ai/blob/main/README.md
2️⃣ Install dependencies
pip install pandas numpy scikit-learn streamlit
3️⃣ Train the model
python model.py
4️⃣ Run the app
streamlit run app.py
📊 Example Output
Input: "I feel very stressed and tired"
Sleep: 4 hours
Screen Time: 9 hours

👉 Output: High Risk ⚠️

⚠️ Disclaimer

This project is for educational purposes only and does not provide medical diagnosis. It is intended as a support tool for early awareness.

💡 Future Improvements
Add real dataset for better accuracy
Improve model performance
Deploy online (Streamlit Cloud / AWS)
Add user login & tracking system

💼 Author
sharau jagtap
