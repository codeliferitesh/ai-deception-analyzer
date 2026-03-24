import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

os.makedirs("backend/saved_model", exist_ok=True)

data = {
    "text": [
        "I swear I did not do anything wrong",
        "Trust me I am honest",
        "I am telling the truth",
        "I stole the money",
        "I lied about it",
        "I took it secretly"
    ],
    "label": [0,0,0,1,1,1]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer(ngram_range=(1,2))
X = vectorizer.fit_transform(df["text"])
y = df["label"]

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "backend/saved_model/model.pkl")
joblib.dump(vectorizer, "backend/saved_model/vectorizer.pkl")

print("✅ Model trained")