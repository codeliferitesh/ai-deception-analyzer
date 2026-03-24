import joblib
import os

MODEL_PATH = "backend/saved_model/model.pkl"
VEC_PATH = "backend/saved_model/vectorizer.pkl"


def load_model():
    try:
        model = joblib.load(MODEL_PATH)
        vectorizer = joblib.load(VEC_PATH)
        return model, vectorizer
    except:
        print("⚠️ Model not found. Training new model...")
        import train
        model = joblib.load(MODEL_PATH)
        vectorizer = joblib.load(VEC_PATH)
        return model, vectorizer


model, vectorizer = load_model()


def predict(text):
    X = vectorizer.transform([text])
    prob = model.predict_proba(X)[0]

    return {
        "truth": float(prob[0]),
        "deception": float(prob[1])
    }