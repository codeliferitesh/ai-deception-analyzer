📘 AI Deception Analyzer (CLI-Based)
🧠 Overview

The AI Deception Analyzer is a command-line (CLI) based application that uses Machine Learning and Natural Language Processing (NLP) to analyze input text and determine:

Whether the text is truthful or deceptive
The emotional tone of the text (Positive, Negative, Angry, Neutral)

This project is fully executable in a terminal environment, without any graphical interface, as required.

🎯 Problem Statement

In real-life communication, identifying whether a statement is truthful or deceptive is difficult. People often use subtle language patterns when lying.

This project aims to build an AI system that:

Accepts text input via terminal
Predicts deception probability
Detects emotional tone
Stores and displays previous results
⚙️ Requirements
🔹 Software Requirements

Make sure the following are installed:

Python (version 3.8 or above)
pip (Python package manager)
📦 Installation & Setup (Step-by-Step)
1️⃣ Clone the Repository
git clone https://github.com/codeliferitesh/ai-deception-analyzer.git
cd ai-deception-analyzer
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Train the Model (IMPORTANT – First Time Only)
python backend/train.py

This will create:

backend/saved_model/model.pkl
backend/saved_model/vectorizer.pkl
4️⃣ Run the Application
python run.py
💻 How to Use (CLI Instructions)

After running the program, you will see:

🧠 AI DECEPTION ANALYZER (CLI VERSION)
Available Commands:
Command	Description
analyze	Analyze input text
history	View past results
help	Show all commands
exit	Exit the program
▶️ Example Usage
👉 Enter command: analyze

📝 Enter text: I swear I didn’t do anything wrong

🔍 RESULT:
Truth Probability     : 0.30
Deception Probability : 0.70
Emotion               : Neutral 😐
📜 View History
👉 Enter command: history

Displays all previous analyses stored in history.json.

📂 Project Structure
ai-deception-analyzer/
│
├── backend/
│   ├── __init__.py
│   ├── cli.py              # CLI logic
│   ├── model.py            # ML prediction
│   ├── train.py            # Model training
│   ├── utils.py            # Emotion detection
│   └── saved_model/
│       ├── model.pkl
│       └── vectorizer.pkl
│
├── history.json            # Stores results
├── run.py                  # Main entry point
├── requirements.txt
└── README.md
🔍 How the System Works
User enters text via CLI
Text is converted to numerical features using TF-IDF Vectorization
A Logistic Regression model predicts:
Truth probability
Deception probability
Emotion is detected using keyword-based logic
Results are displayed and stored in history.json
⚠️ Important Notes
Always run the project from the root folder
Do NOT run files directly inside the backend folder
Model must be trained before first use
⚠️ Limitations
Small dataset → limited accuracy
Emotion detection is rule-based
Not suitable for critical real-world decisions
🚀 Future Improvements
Use advanced NLP models (BERT, Transformers)
Improve dataset size and accuracy
Add voice input support
Add batch text analysis
Deploy as cloud-based service
👨‍💻 Author

Ritesh Kumar Verma
Roll No: 25BAI11426

❤️ Acknowledgement

This project was developed as part of the Fundamentals of AI and ML (CSA2001) course under guidance of MK Jayanti Mam.

💖 Final Note

This project demonstrates a complete CLI-based AI application, including:

Machine Learning model
Data processing
Command-line interaction
Data persistence