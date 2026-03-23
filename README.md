📘 AI Deception Analyzer
🧠 Overview

The AI Deception Analyzer is a machine learning-based web application that analyzes input text to determine whether it is likely truthful or deceptive, along with detecting the emotional tone of the text.

This project applies Natural Language Processing (NLP) and Machine Learning techniques to study linguistic patterns often associated with deception and emotional expression.

🎯 Problem Statement

In daily life, it is often difficult to determine whether a statement is truthful or deceptive based solely on language. People frequently use subtle linguistic cues when lying, such as:

Over-explaining
Defensive language
Emotional manipulation
Vague or indirect statements

This project aims to address this challenge by building an AI system that can:

Analyze textual input
Predict deception likelihood
Identify emotional tone
Provide quick, interpretable results
💡 Why This Problem Matters

Understanding deception has real-world applications in:

Social interactions and communication
Online content moderation
Customer feedback analysis
Fraud detection and security systems

This project demonstrates how AI can assist in interpreting human language, making it a practical application of course concepts in Machine Learning and NLP.

⚙️ Tech Stack
🔹 Backend
Python
FastAPI
scikit-learn
pandas
numpy
joblib
🔹 Frontend
HTML
CSS
JavaScript
🧩 Features
✅ Deception detection using ML model
✅ Emotion classification (Positive, Negative, Neutral, Angry)
✅ Real-time predictions via API
✅ Interactive and modern UI
✅ Clean visualization of results
✅ Lightweight and fast execution
🏗️ Project Architecture
User Input → Frontend → FastAPI Backend → ML Model → Prediction Output → UI Display
Workflow:
User enters text in the UI
Frontend sends request to FastAPI backend
Text is vectorized using trained vectorizer.pkl
ML model (model.pkl) predicts deception probability
Emotion is detected using keyword-based logic
Results are returned and displayed on the frontend
📂 Project Structure
ai-deception-analyzer/
│
├── backend/
│   ├── main.py              # FastAPI server
│   ├── model.py             # ML model logic
│   ├── train.py             # Model training script
│   ├── utils.py             # Helper functions
│   ├── requirements.txt     # Dependencies
│   └── saved_model/
│       ├── model.pkl
│       └── vectorizer.pkl
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── run.py                   # Entry point to run the app
└── README.md
🚀 How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/codeliferitesh/ai-deception-analyzer.git
cd ai-deception-analyzer
2️⃣ Install Dependencies
cd backend
pip install -r requirements.txt
3️⃣ Train the Model
python train.py
4️⃣ Run the Application
python run.py
5️⃣ Open in Browser

Open your browser and go to:

http://127.0.0.1:8000
🧪 Example Inputs & Outputs
Input:
I swear I didn’t do anything wrong.
Output:
Truth: Low
Deception: High
Emotion: Neutral
Input:
Honestly, I was just there for a few seconds and then left immediately.
Output:
Truth: Low
Deception: High
Emotion: Defensive / Neutral
🔍 How It Works (Technical Insight)
Text is converted into numerical features using TF-IDF Vectorization
A trained classification model predicts deception probability
Emotion detection is performed using rule-based keyword matching
FastAPI handles communication between frontend and backend
📌 Design Decisions
TF-IDF was chosen for feature extraction due to its simplicity and effectiveness in text classification.
FastAPI was used for its speed and modern async capabilities.
A hybrid approach (ML + rule-based) was used for emotion detection to balance performance and simplicity.
The UI was designed to be minimal and intuitive for better user experience.
⚠️ Limitations
The model is trained on limited data and may not generalize perfectly
Emotion detection is keyword-based and not deeply semantic
Cannot guarantee accurate real-world deception detection (AI assists, not replaces judgment)
🚀 Future Improvements
Integration of advanced models like BERT or transformer-based NLP models
Training on larger and more diverse datasets
Improved emotion detection using deep learning
Adding visualization charts (graphs, confidence bars)
User authentication and history tracking
Deployment on cloud (AWS / Render / Vercel)
🧠 What I Learned
Practical implementation of NLP and ML concepts
Building and training a classification model
Working with APIs using FastAPI
Structuring a full-stack AI application
Handling real-world challenges like data limitations and model accuracy
👨‍💻 Author

Ritesh Kumar Verma
Roll No: 25BAI11426

❤️ Acknowledgement

This project was developed as part of the Fundamentals of AI and ML (BYOP) course. It demonstrates practical understanding of machine learning concepts and their real-world application.

✨ Conclusion

The AI Deception Analyzer showcases how machine learning can be applied to analyze human language and extract meaningful insights. While it does not replace human judgment, it provides a strong foundation for understanding how AI can assist in interpreting communication patterns.

💖 Footer

Made with ❤️ by Ritesh Kumar Verma